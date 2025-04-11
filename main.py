import chess
import time
import os
import shutil
import imageio.v2 as imageio
import matplotlib.pyplot as plt

from minimax import minimax
from alphabeta import alphabeta
from chess_utils import render_board
from evaluation import evaluate_board

# --- Save each board state as an image ---
def save_frame(board, move_number):
    import cairosvg
    import chess.svg
    svg_data = chess.svg.board(board=board, size=400)
    png_data = cairosvg.svg2png(bytestring=svg_data, output_width=400, output_height=400)
    with open(f"frames/frame_{move_number:03d}.png", "wb") as f:
        f.write(png_data)


# --- Create video from frames ---
def make_video(name):
    images = []
    for i in sorted(os.listdir("frames")):
        if i.endswith(".png"):
            images.append(imageio.imread(f"frames/{i}"))
    os.makedirs("videos", exist_ok=True)
    imageio.mimsave(f"videos/{name}.mp4", images, fps=1)
    shutil.rmtree("frames")


# Global dictionary to store all move times
timing_results = {}

# Modify run_game function to capture and plot move times
def run_game(ai_name, ai_func, depth):
    board = chess.Board()
    move_number = 0
    move_times = []  # To store per-move time
    os.makedirs("frames", exist_ok=True)

    while not board.is_game_over() and move_number < 60:
        print(f"\nMove {move_number + 1}: {ai_name}")
        start_time = time.time()

        if ai_name == "Minimax":
            _, move = ai_func(board, depth, True)
        else:
            _, move = ai_func(board, depth, float('-inf'), float('inf'), True)

        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Time taken: {elapsed:.2f} seconds")
        move_times.append(elapsed)

        if move is None:
            break
        board.push(move)
        save_frame(board, move_number)
        move_number += 1

    print("Game Over:", board.result())
    save_frame(board, move_number)
    make_video(ai_name)

    timing_results[ai_name] = move_times

    # Save individual timing plots too
    plt.figure(figsize=(10, 4))
    plt.plot(move_times, marker='o')
    plt.title(f"Time per move ({ai_name} at depth {depth})")
    plt.xlabel("Move Number")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"videos/{ai_name}_timing_plot.png")
    plt.close()


# Run both games
run_game("Minimax", minimax, 4)
run_game("AlphaBeta", alphabeta, 4)

# --- Combined Timing Plot ---
plt.figure(figsize=(12, 5))
for ai_name, times in timing_results.items():
    plt.plot(times, marker='o', label=ai_name)

plt.title("Comparison of Move Times (Minimax vs AlphaBeta)")
plt.xlabel("Move Number")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("videos/combined_timing_plot.png")
plt.show()
