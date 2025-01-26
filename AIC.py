import chess
import chess.engine
import chess.svg
from flask import Flask, render_template_string, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Stockfish engine path (updated)
STOCKFISH_PATH = "your_file_path_goes_here!!!"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Chess Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        h1 {
            font-size: 36px;
            color: #444;
        }
        #game-container {
            display: flex;
            align-items: flex-start;
            justify-content: center;
            gap: 40px;
            margin-top: 20px;
        }
        #instructions {
            max-width: 300px;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        #instructions ul {
            text-align: left;
            margin: 0;
            padding-left: 20px;
        }
        #instructions h3 {
            margin-bottom: 10px;
        }
        #controls {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
        }
        #board-container {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        #board {
            margin: 10px auto;
        }
        input {
            font-size: 16px;
            width: 300px;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 8px;
            margin-bottom: 10px;
        }
        button {
            font-size: 16px;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            background-color: #0078d7;
            color: white;
            margin: 5px 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        button:hover {
            background-color: #005ea2;
        }
        svg {
            width: 400px;
            height: auto;
        }
        #status {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>AI Chess Game</h1>
    <div id="game-container">
        <div id="instructions">
            <h3>How to Play:</h3>
            <p>
                - Enter your move in UCI (Universal Chess Interface) format.<br>
                - Examples:
                <ul>
                    <li><strong>e2e4</strong>: Move a piece from e2 to e4.</li>
                    <li><strong>g1f3</strong>: Move a knight from g1 to f3.</li>
                </ul>
                - After your move, the AI will make its move automatically after a short delay.<br>
                - Press "Reset Game" to restart the game at any time.
            </p>
        </div>
        <div id="board-container">
            <div id="board"></div>
            <p id="status">Game in progress...</p>
        </div>
        <div id="controls">
            <input type="text" id="user-move" placeholder="Enter your move (e.g., e2e4)">
            <button onclick="makeUserMove()">Make Move</button>
            <button onclick="resetGame()">Reset Game</button>
        </div>
    </div>

    <script>
        async function updateBoard() {
            const response = await fetch('/board');
            const data = await response.json();
            document.getElementById('board').innerHTML = data.svg;
            document.getElementById('status').innerText = data.status;
        }

        async function makeUserMove() {
            const move = document.getElementById('user-move').value;
            const response = await fetch('/user-move', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ move }),
            });

            if (response.ok) {
                document.getElementById('user-move').value = '';
                updateBoard();
                setTimeout(() => makeAIMove(), 2000);  // Delay AI move by 2 seconds
            } else {
                alert('Invalid move. Try again.');
            }
        }

        async function makeAIMove() {
            await fetch('/ai-move', { method: 'POST' });
            updateBoard();
        }

        async function resetGame() {
            await fetch('/reset', { method: 'POST' });
            updateBoard();
        }

        updateBoard();
    </script>
</body>
</html>
"""

# Initialize chess board
game_board = chess.Board()

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/board")
def get_board():
    board_svg = chess.svg.board(game_board)
    status = "Game in progress..."
    if game_board.is_checkmate():
        status = "Checkmate! Game over."
    elif game_board.is_stalemate():
        status = "Stalemate! Game over."
    elif game_board.is_insufficient_material():
        status = "Draw due to insufficient material."
    elif game_board.is_game_over():
        status = "Game over!"

    return jsonify({"svg": board_svg, "status": status})

@app.route("/user-move", methods=["POST"])
def user_move():
    global game_board
    if not game_board.is_game_over():
        data = request.get_json()
        move = data.get("move")

        try:
            chess_move = chess.Move.from_uci(move)
            if chess_move in game_board.legal_moves:
                game_board.push(chess_move)
                return "", 204
            else:
                return "Invalid move", 400
        except ValueError:
            return "Invalid move format", 400
    else:
        return "Game over", 400

@app.route("/ai-move", methods=["POST"])
def ai_move():
    global game_board
    if not game_board.is_game_over():
        result = engine.play(game_board, chess.engine.Limit(time=0.5))
        game_board.push(result.move)
    return "", 204

@app.route("/reset", methods=["POST"])
def reset_game():
    global game_board
    game_board = chess.Board()
    return "", 204

if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        engine.quit()
