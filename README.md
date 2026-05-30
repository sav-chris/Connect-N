Connect‑N Game Framework
A Python framework for building AI players using Minimax and Alpha‑Beta pruning

# 📌 Overview
This project implements a configurable Connect‑N game engine in Python.
It supports:

#### 🚹 **Human players**

#### 🎲 **Random players**

#### 👩‍🎓 **Student‑implemented AI players (e.g., Minimax, Alpha‑Beta)**

#### 🐢 **Handicapped game series**

#### 🧟‍♂️**Custom board sizes**

The game logic is fully implemented in Connect_N_Board, while students implement their AI in your_player.py.

# 🎮 Game Rules
Connect‑N is a generalization of Connect‑4:

Two players alternate dropping stones into columns.

Stones fall to the lowest empty cell.

A player wins by forming a line of N consecutive stones:

horizontally

vertically

diagonally (both directions)

In this implementation:

```python
NWIN = 4
```
So the default is Connect‑4, but the board size is customizable.

# 📁 Project Structure
Code
```
.
├── connect_n.py        # Main game engine
├── your_player.py      # Where you implement your AI
└── README.md           # This file
```

# 🧠 Player Types

#### 🎲 **RandomPlayer**
Chooses a random legal move.

#### 🚹 **HumanPlayer**
Prompts the user for a column number.

#### StudentPlayer_Example / MinMax / AlphaBeta
These are implemented in your_player.py.
They use algorithms such as:

#### 🧮 **Minimax**

#### ** $ \alpha \beta $ Alpha‑Beta pruning**

#### 🧠 **Heuristic evaluation functions**

# ▶️ Running the Game
Play a single game (AI vs Human)
```python
if __name__ == '__main__':
    run_single_game()
```
Run a handicapped series
```python
run_HandicappedGameSeries()
```

# 🧠 Minimax Algorithm Explained
Minimax is a classic adversarial search algorithm used in two‑player games.

### 🎯 Goal
Choose the move that maximizes your chance of winning, assuming the opponent plays optimally.

### 🔍 How Minimax Works
Minimax explores the game tree:

MAX nodes → AI’s turn (tries to maximize utility)

MIN nodes → Opponent’s turn (tries to minimize utility)

At each leaf node, the algorithm evaluates the board using a utility function.

Then values propagate upward:

MAX chooses the maximum child value

MIN chooses the minimum child value

### 📊 Example Minimax Tree (Depth 2)
```Code
                 MAX (AI)
               /     |     \
             3       5      2
           / | \   / | \   / | \
         3  1  3  5  5  4  2  2  1
```
Leaves = utility values

MIN nodes choose the minimum of their children

MAX chooses the maximum of the MIN results

So MAX chooses 5 → the best achievable outcome.

### 🧮 Utility Function (Heuristic Evaluation)
When the game tree is too large to search fully, Minimax stops at a depth limit and evaluates the board.

A typical utility function for Connect‑N might consider:

Positive scores for AI:
+100000 for a win

+1000 for 3‑in‑a‑row

+10 for 2‑in‑a‑row

Negative scores for opponent:
−100000 if opponent wins

−1000 for opponent 3‑in‑a‑row

−10 for opponent 2‑in‑a‑row

Board‑centric heuristics
Prefer center columns

Prefer moves that create multiple threats

Penalize moves that allow opponent forks

A simple example:

```python
def evaluate(board):
    score = 0
    score += 1000 * count_segments(board, colour, length=3)
    score += 10   * count_segments(board, colour, length=2)
    score -= 1000 * count_segments(board, -colour, length=3)
    score -= 10   * count_segments(board, -colour, length=2)
    return score
```

### ⚡ Alpha‑Beta Pruning (Optional Enhancement)
Alpha‑Beta pruning improves Minimax by skipping branches that cannot affect the final decision.

This reduces the number of nodes explored from:

$O(b^d)$ → worst case

$O(b^(d/2))$ → best case

Where:

$b$ = branching factor

$d$ = depth

This allows deeper searches with the same computation time.

### 🌳 Full Minimax Tree Example (with Alpha‑Beta)
```Code
                     MAX
          α=-∞ β=∞
           /      \
       MIN         MIN
   α=-∞ β=∞     α=-∞ β=∞
    / | \          / | \
   3  5  2        4  6  1
```
Alpha‑Beta will prune branches that cannot improve the outcome.

###  🧪 Example Flow of a Game
AI receives a board state via getMove(board)

AI runs Minimax (or Alpha‑Beta)

AI returns the best column index

Game engine validates and applies the move

Game continues until:

a player wins

the board is full (draw)

a player returns an illegal move (loss)

# 📘 Summary
This project provides:

A complete Connect‑N engine

A framework for implementing AI players

Support for Minimax and Alpha‑Beta pruning

Tools for testing AI performance

It is ideal for assignments in:

AI

Game theory

Adversarial search

Heuristic evaluation
