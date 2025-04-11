import chess
import matplotlib.pyplot as plt
import chess.svg
import io
import cairosvg

def render_board(board: chess.Board, size=400):
    svg_data = chess.svg.board(board=board, size=size)
    png_data = cairosvg.svg2png(bytestring=svg_data, output_width=size, output_height=size)
    img = plt.imread(io.BytesIO(png_data), format='png')

    plt.figure(figsize=(size/100, size/100))
    plt.imshow(img)
    plt.axis('off')
    plt.tight_layout()
    plt.show()
