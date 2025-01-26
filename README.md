# AI Chess (AIC) ♟️

AI Chess (AIC) is a web-based chess game powered by a Stockfish AI engine. Players can make moves against the AI, visualize the chessboard in real-time, and reset the game as needed. This project leverages Python, Flask, and Chess libraries to provide an engaging and interactive chess-playing experience.

---

## Table of Contents 📑

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [How to Play](#how-to-play)
6. [Technologies Used](#technologies-used)
7. [License](#license)

---

## Features

- 🖼️ Interactive chessboard rendered dynamically using SVG.
- 🤖 Player vs. AI gameplay with moves based on the Stockfish engine.
- ✅ Real-time validation of user moves.
- ⏱️ AI opponent responds automatically after a short delay.
- 📜 Instructions for players on how to input moves using UCI format.
- 🔄 Reset functionality to start a new game.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- 🐍 Python (3.7 or later)
- 📦 pip (Python package manager)
- ⚙️ Stockfish chess engine

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

### Step-by-Step Example

1. **Start the game:**
   - The chessboard will appear, and you can input your first move.
     
   Start Screen

![image](https://github.com/user-attachments/assets/662788e9-5777-4808-b6c8-63c8a4ca073a)


2. **Make your move:**
   - Example: Enter `e2e4` and press "Make Move."
     
   Player Move

![image](https://github.com/user-attachments/assets/97491191-ce11-489c-b971-031c8651ea0c)


3. **AI makes its move:**
   - The AI will respond automatically. Example: `c7c5`.
     
   AI Move

![image](https://github.com/user-attachments/assets/f951be73-7277-4750-87c8-7bed9a32e476)


4. **Continue playing:**
   - Input moves and watch the AI play against you.
     
   Gameplay

![image](https://github.com/user-attachments/assets/508e07c3-2474-4520-8adb-50e668a3bb51)


5. **Reset the game:**
   - Press the "Reset Game" button to start a new match.
   Reset Screen

![image](https://github.com/user-attachments/assets/f96c2439-3faf-4c41-8111-ade15f2e21fc)


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

## Acknowledgments 🙌

- [Stockfish](https://stockfishchess.org/) for the chess engine.
- [Chess Python Library](https://python-chess.readthedocs.io/en/latest/) for chess-related utilities.
- Inspiration from the global chess community!
