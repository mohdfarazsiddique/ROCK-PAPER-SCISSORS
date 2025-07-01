# 🪨 Rock Paper Scissors Game - Python

A simple, beginner-friendly implementation of the classic **Rock, Paper, Scissors** game in Python. This is a terminal-based game where the player competes against the computer. It uses randomization, basic logic, and clean input handling — perfect for anyone starting their Python journey.

---

## 🎮 How to Play

- Run the Python file in your terminal.
- You’ll be asked to enter your choice:
  - `r` for Rock
  - `p` for Paper
  - `s` for Scissors
- The computer will also make a random choice.
- The winner is determined based on standard game rules.

---

## 💡 Game Logic

Each input is mapped to a number:
- `r` → 1 (Rock)
- `p` → 2 (Paper)
- `s` → 3 (Scissors)

The winner is calculated using this logic:

```python
if (computer - user == -1 or computer - user == 2):
    print("You win!")
elif (computer - user == 1 or computer - user == -2):
    print("You lose!")
else:
    print("It's a draw!")
```

This approach eliminates the need for multiple nested `if-else` blocks and keeps the code elegant and concise.

---

## 🛠️ Technologies Used

- Python 3
- `random` module for computer's choice
- Dictionaries for input mapping and reverse lookup
- Simple CLI interaction

---

## 💻 How to Run

Make sure Python is installed on your machine.

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/mohdfarazsiddique/ROCK-PAPER-SCISSORS.git
```

### 🔹 Step 2: Run the Game

```bash
cd ROCK-PAPER-SCISSORS
python rock_paper_scissor.py
```

---

## 🚀 Future Improvements

- Add a score counter for multiple rounds
- Loop the game until the user exits
- Handle invalid input with better feedback
- Build a GUI version using `tkinter`
- Add sound or animations for fun

---

## 👤 Author

**Md Faraz Siddique**  
GitHub: [@mohdfarazsiddique](https://github.com/mohdfarazsiddique)

---


## 🌟 Star This Repo

If you found this entertaining, consider giving it a ⭐ on GitHub — it motivates me to build more cool stuff!  :3