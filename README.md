# Tetris Game Instructions

## Installation
   # Tetris Game Instructions

   ## Installation

   This project is a Python `pygame` Tetris implementation. You can run it directly with Python, or use the included `npm` script which simply invokes Python.

   1. Clone the repository:
      ```bash
      git clone https://github.com/sanniv01/Cero.git
      cd Cero
      ```

   2. Create a virtual environment (recommended) and install dependencies:
      ```bash
      python -m venv .venv
      # Windows
      .venv\Scripts\activate
      # macOS / Linux
      source .venv/bin/activate
      pip install -r requirements.txt
      ```

   3. Alternatively, if you prefer `npm`/`node`, you can still run the game with `npm start` because a small `package.json` script is provided that runs the Python file.

   ## Playing the Game

   1. Start the game:
      ```bash
      # using python directly
      python tetris.py

      # or via npm (runs the same command)
      npm start
      ```

   2. Use the arrow keys to move the Tetris pieces.
   3. Rotate the pieces using the up arrow key.
   4. Clear lines by completing horizontal rows with no gaps.

   Enjoy playing Tetris!