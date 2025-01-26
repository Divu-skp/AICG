import tkinter as tk
import chess
from PIL import Image, ImageTk
import random

# Initialize the chess board
board = chess.Board()

# Create a dictionary for piece images
piece_images = {
    "K": "chess_images/white_king.png", "Q": "chess_images/white_queen.png", "R": "chess_images/white_rook.png",
    "B": "chess_images/white_bishop.png", "N": "chess_images/white_knight.png", "P": "chess_images/white_pawn.png",
    "k": "chess_images/black_king.png", "q": "chess_images/black_queen.png", "r": "chess_images/black_rook.png",
    "b": "chess_images/black_bishop.png", "n": "chess_images/black_knight.png", "p": "chess_images/black_pawn.png"
}

# Function to load images
def load_image(piece):
    try:
        image = Image.open(piece_images[piece])
        image = image.resize((60, 60), Image.Resampling.LANCZOS)  # Resize with LANCZOS for high-quality resizing
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image for {piece}: {e}")
        return None

# Create the main window
window = tk.Tk()
window.title("Chess Game")

# Initialize a canvas for drawing the board
canvas = tk.Canvas(window, width=480, height=480)
canvas.pack()

# To store the selected square
selected_square = None

# To store the image references and prevent garbage collection
image_references = {}

# Draw the chessboard with dark blue and light blue squares
def draw_board():
    for row in range(8):
        for col in range(8):
            # Alternate between dark blue and light blue for the board squares
            color = "dark blue" if (row + col) % 2 == 0 else "light blue"
            canvas.create_rectangle(col*60, row*60, (col+1)*60, (row+1)*60, fill=color)


# Draw the pieces on the board
def draw_pieces():
    global image_references  # We need this to keep track of images and prevent garbage collection
    image_references.clear()  # Clear previous references
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_str = piece.symbol()
            image = load_image(piece_str)
            if image:  # Ensure image was loaded
                row, col = divmod(square, 8)
                x_center = col * 60 + 30  # Center position on the square
                y_center = row * 60 + 30  # Center position on the square
                
                # Draw a border around the piece
                canvas.create_rectangle(x_center - 32, y_center - 32, x_center + 32, y_center + 32, outline="black", width=2)

                # Place the piece image inside the square
                canvas.create_image(x_center, y_center, image=image)
                
                image_references[square] = image  # Store the image reference

# Handle player moves
def make_move(event):
    global selected_square

    # Get the row and column of the clicked square
    col, row = event.x // 60, event.y // 60
    square = row * 8 + col  # Convert to square index

    if selected_square is None:
        # Store the first square selected by the player (starting square)
        selected_square = square
    else:
        # Ensure the start and end squares are different
        if selected_square == square:
            selected_square = None  # Reset selected square if the same square is clicked again
            return  # Do nothing if the same square is clicked again
        
        # Convert the starting and ending squares to UCI format (e.g., e2e4)
        start_square = selected_square
        end_square = square
        
        # Calculate UCI coordinates from the square index
        start_file = chr(start_square % 8 + ord('a'))  # 'a' to 'h'
        start_rank = 8 - (start_square // 8)  # 1 to 8
        end_file = chr(end_square % 8 + ord('a'))  # 'a' to 'h'
        end_rank = 8 - (end_square // 8)  # 1 to 8

        # Create UCI string (e.g., "e2e4")
        uci_move = f"{start_file}{start_rank}{end_file}{end_rank}"
        
        # Validate the move before applying it
        try:
            move = chess.Move.from_uci(uci_move)
            if move in board.legal_moves:
                board.push(move)
                draw_board()
                draw_pieces()
        except chess.InvalidMoveError:
            print(f"Invalid move: {uci_move}")
        
        selected_square = None  # Reset selected square for the next move

# AI move using random move for simplicity
def ai_move():
    # Find random legal move for the AI
    legal_moves = list(board.legal_moves)
    move = random.choice(legal_moves)
    board.push(move)
    draw_board()
    draw_pieces()

# Add event binding for mouse click
canvas.bind("<Button-1>", make_move)

# Initial drawing of the board and pieces
draw_board()
draw_pieces()

# Run the Tkinter event loop
window.mainloop()
