# Connect-4-AI
This is for an AI class (CPSC 481) at CSUF 
file structure 
connect4_ai/
how to launch 
cd connect4_ai
pip install -r requirements.txt
python main.py

you should see 
Welcome to Connect 4!
Choose mode:
1 - Play vs Our AI
2 - Play vs Online AI (placeholder)
Enter 1 or 2:


├── ai/
│   ├── minimax.py       # Our AI agent (Minimax + Alpha-Beta)
│   └── online_ai.py     # Placeholder for external/online AI (optional later)
├── game/
│   ├── board.py         # Board creation, move logic, win checking (your current code cleaned up)
│   └── game_loop.py     # Running a game between Human vs AI or AI vs AI
├── gui/
│   └── gui.py           # Simple GUI using Tkinter
├── main.py              # Entry point to select mode: play Human vs AI, AI vs AI
├── evaluation.py        # Compares our AI and the online version
├── README.md            # Project overview and instructions
├── requirements.txt     # External libraries (ex: numpy, tkinter [built-in], maybe online AI deps)
└── assets/              # (optional) For future images, icons if you want
