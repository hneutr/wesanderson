import matplotlib.pyplot as plt
import os
from matplotlib.patches import Rectangle
from matplotlib.text import Text
import matplotlib as mpl
from pathlib import Path
import numpy as np

import wesanderson

COLOR_PALETTES_FIGURES_PATH = Path(__file__).parent.joinpath('wes_anderson_color_palettes.png')


def get_color_bar(colors, y, width, height):
    rectangles = []
    for i, color in enumerate(colors):
        x = width * i
        rectangle = Rectangle(
            xy=(x, y),
            width=width,
            height=height,
            color=color,
        )
        rectangles.append(rectangle)
    return rectangles


if __name__ == '__main__':
    color_palettes_tuples = wesanderson.color_palettes_tuples
    # We're going to make an ax for each color bar, and an extra ax to space out each movie
    movie_spacer_count = len(wesanderson.color_palettes.keys()) - 1
    color_palette_count = len(color_palettes_tuples)

    SWAB_HEIGHT = 1
    SWAB_WIDTH = 2
    largest_color_palette = max([len(cp_tuple.Palette) for cp_tuple in color_palettes_tuples])

    y = -.5 * SWAB_HEIGHT
    rectangles = []
    film_title_texts = []
    palette_texts = []
    for film, palettes in wesanderson.color_palettes.items():
        y += SWAB_HEIGHT * .5
        film_title_texts.append([y, film])

        for i, palette in enumerate(palettes):
            rectangles += get_color_bar(palette, y=y, width=SWAB_WIDTH, height=SWAB_HEIGHT)
            palette_texts.append([y + SWAB_HEIGHT / 2, i])
            y += 1.5 * SWAB_HEIGHT

    y -= SWAB_HEIGHT * 1.5

    ANNOTATION_Y_OFFSET = SWAB_HEIGHT / 4
    ANNOTATION_X_OFFSET = SWAB_WIDTH / 8

    lower_x_lim = 0 - ANNOTATION_X_OFFSET
    upper_x_lim = largest_color_palette * SWAB_WIDTH

    lower_y_lim = 0 - ANNOTATION_Y_OFFSET
    upper_y_lim = y + SWAB_HEIGHT

    fig_x_size = upper_x_lim - lower_x_lim
    fig_y_size = upper_y_lim - lower_y_lim

    y_to_x_ratio = fig_y_size / fig_x_size
    horizontal_size = 8
    vertical_size = horizontal_size * y_to_x_ratio * 3

    fig, ax = plt.subplots(1, figsize=(horizontal_size, vertical_size))
    for rectangle in rectangles:
        ax.add_patch(rectangle)

    for y, text in film_title_texts:
        ax.annotate(
            text=text,
            xy=(0, y - ANNOTATION_Y_OFFSET),
            ha='left',
            va='bottom',
            fontsize='x-large',
        )

    for y, text in palette_texts:
        ax.annotate(
            text=f"palette {text}",
            xy=(0 - ANNOTATION_X_OFFSET, y),
            ha='right',
            va='center',
            fontsize='x-large',
        )

    ax.set_xlim([lower_x_lim, upper_x_lim])
    ax.set_ylim([upper_y_lim, lower_y_lim])
    ax.axis('off')

    path = str(COLOR_PALETTES_FIGURES_PATH)
    plt.savefig(path, bbox_inches='tight')
    plt.clf()
    plt.close()
    # os.system(f'open {path}')
