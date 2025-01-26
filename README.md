# AI Chess Game (AICG)

AI Chess Game (AICG) is a web-based chess game powered by a Stockfish AI engine. Players can make moves against the AI, visualize the chessboard in real-time, and reset the game as needed. This project leverages Python, Flask, and Chess libraries to provide an engaging and interactive chess-playing experience.

---

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [How to Play](#how-to-play)
6. [Technologies Used](#technologies-used)
7. [License](#license)

---

## Features

- Interactive chessboard rendered dynamically using SVG.
- Player vs. AI gameplay with moves based on the Stockfish engine.
- Real-time validation of user moves.
- AI opponent responds automatically after a short delay.
- Instructions for players on how to input moves using UCI format.
- Reset functionality to start a new game.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.7 or later)
- pip (Python package manager)
- Stockfish chess engine

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/<your-username>/AI-Chess.git
    cd AI-Chess
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Download the Stockfish engine (if not already downloaded) and note the path to the executable.

---

## Usage

1. Update the `STOCKFISH_PATH` variable in the `app.py` file to point to your Stockfish executable.

    ```python
    STOCKFISH_PATH = "C:\\path\\to\\your\\stockfish\\executable"
    ```

2. Run the Flask application:

    ```bash
    python app.py
    ```

3. Open a web browser and navigate to `http://127.0.0.1:5000/` to start playing.

---

## How to Play

- Enter your moves in **UCI (Universal Chess Interface)** format, such as:
  - `e2e4`: Move a piece from e2 to e4.
  - `g1f3`: Move a knight from g1 to f3.
- After entering your move, the AI will make its move automatically after a short delay.
- Use the **Reset Game** button to restart the game at any time.

### Example Gameplay

1. Input: `e2e4`
2. AI Response: `e7e5`
3. Input: `g1f3`
4. AI Response: `b8c6`

---

## Technologies Used

- **Python**: Backend logic and AI integration.
- **Flask**: Web framework for serving the application.
- **Stockfish**: Powerful open-source chess engine.
- **HTML, CSS**: Frontend UI design.
- **SVG**: Chessboard rendering.
- **Chess Library**: Chessboard representation and move validation.

---

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork this repository and submit a pull request or open an issue.

---

## Acknowledgments

- [Stockfish](https://stockfishchess.org/) for the chess engine.
- [Chess Python Library](https://python-chess.readthedocs.io/en/latest/) for chess-related utilities.
- Inspiration from the global chess community!
