# ♟️ AI Chess Showdown: Minimax vs Alpha-Beta

Welcome to an exciting AI Chess simulation where two legendary algorithms — **Minimax** and **Alpha-Beta Pruning** — battle it out on the board. This project visualizes their decisions, compares their performance, and even lets you relive the match through generated videos and timing graphs.

---

## 👥 Team: SmartThinkers

| Name         | Roll Number |
|--------------|-------------|
| Dharmendra Chauhan | CS24M115      |
| Kodela Phanindra    | cs24m121     |

---

## 🎯 Project Overview

This project simulates a full chess match between two AI strategies:

- **Minimax Algorithm**
- **Alpha-Beta Pruning (Optimized Minimax)**

Each AI selects its best move based on material evaluation at a configurable search depth. Moves are recorded as images and stitched into a video, while per-move timing is plotted for algorithmic comparison.

---

## 🧠 Evaluation Function

Simple material-based evaluation:

- Pawn = 1  
- Knight = 3  
- Bishop = 3  
- Rook = 5  
- Queen = 9  
- King = 0 (not counted in score)

Score = `White's total - Black's total`.

---

## 🖥️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/dharmendrac443/AI_Assignment-3.git
cd AI_Assignment-3
```
**To run this file**
>pip install -r requirements.txt

>python3 main.py