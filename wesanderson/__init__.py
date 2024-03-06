"""
A small package of color palettes from Wes Anderson movies.

Based on Karthik Ram's version for R: https://github.com/karthik/wesanderson
"""
import wesanderson.__package_info__ as package_info
from functools import lru_cache
from collections import namedtuple

FilmPalette = namedtuple('FilmPalette', ['Film', 'Palette'])

__authors__ = package_info.__authors__
__version__ = package_info.__version__


color_palettes = {
    "Bottle Rocket": [
        ["#A42820", "#5F5647", "#9B110E", "#3F5151", "#4E2A1E", "#550307", "#0C1707"],
        ["#FAD510", "#CB2314", "#273046", "#354823", "#1E1E1E"],
    ],
    "Rushmore": [
        ["#E1BD6D", "#EABE94", "#0B775E", "#35274A" ,"#F2300F"],
    ],
    "The Royal Tenenbaums": [
        ["#899DA4", "#C93312", "#FAEFD1", "#DC863B"],
        ["#9A8822", "#F5CDB4", "#F8AFA8", "#FDDDA0", "#74A089"],
    ],
    "The Life Aquatic with Steve Zissou": [
        ["#3B9AB2", "#78B7C5", "#EBCC2A", "#E1AF00", "#F21A00"],
    ],
    "Darjeeling Limited": [
        ["#FF0000", "#00A08A", "#F2AD00", "#F98400", "#5BBCD6"],
        ["#ECCBAE", "#046C9A", "#D69C4E", "#ABDDDE", "#000000"],
    ],
    "Hotel Chevalier": [
        ["#446455", "#FDD262", "#D3DDDC", "#C7B19C"],
    ],
    "Fantastic Mr. Fox": [
        ["#DD8D29", "#E2D200", "#46ACC8", "#E58601", "#B40F20"],
    ],
    "Moonrise Kingdom": [
        ["#F3DF6C", "#CEAB07", "#D5D5D3", "#24281A"],
        ["#798E87", "#C27D38", "#CCC591", "#29211F"],
        ["#85D4E3", "#F4B5BD", "#9C964A", "#CDC08C", "#FAD77B"],
    ],
    "Castello Cavalcanti": [
        ["#D8B70A", "#02401B", "#A2A475", "#81A88D", "#972D15"],
    ],
    "The Grand Budapest Hotel": [
        ["#F1BB7B", "#FD6467", "#5B1A18", "#D67236"],
        ["#E6A0C4", "#C6CDF7", "#D8A499", "#7294D4"],
    ],
    "Isle of Dogs": [
        ["#9986A5", "#79402E", "#CCBA72", "#0F0D0E", "#D9D0D3", "#8D8680"],
        ["#EAD3BF", "#AA9486", "#B6854D", "#39312F", "#1C1718"],
    ],
    "The French Dispatch": [
        ["#90D4CC", "#BD3027", "#B0AFA2", "#7FC0C6", "#9D9C85"],
    ],
}


@lru_cache(maxsize=1)
def _color_palettes_tuples():
    """Returns a list of named tuples. eg
    [
        FilmPalette(Film="Bottle Rocket", Palette=[colors]),
        ...
    ]
    """
    color_palettes_list = []
    for film, palettes in color_palettes.items():
        for palette in palettes:
            color_palettes_list.append(FilmPalette(film, palette))

    return color_palettes_list

color_palettes_tuples = _color_palettes_tuples()

def _clean_string(string):
    string = string.replace('.', '')
    string = string.lower()

    words_to_remove = ['the', 'of', 'with']
    string = " ".join([word for word in string.split() if word not in words_to_remove])

    return string


def film_palette(film, palette=0):
    """
    Returns a color palette for a Wes Anderson movie title.

    Tries to be generous with the title names.

    Some of the films have multiple color palettes.

    By default, the first one is returned.

    You can get a specific color palette by passing an index to the `palette` argument.
    You can get all of the color palettes for a film by passing None to the `palette` argument.
    """
    clean_film = _clean_string(film)
    clean_film_titles = [_clean_string(film_title) for film_title in color_palettes.keys()]

    film_index = None
    if clean_film in clean_film_titles:
        film_index = clean_film_titles.index(clean_film)
    else:
        clean_film_words = set(clean_film.split())
        clean_film_titles_as_words = [set(cft.split()) for cft in clean_film_titles]

        set_overlapping_indexes = []
        for i, clean_film_title_words in enumerate(clean_film_titles_as_words):
            if clean_film_title_words & clean_film_words:
                set_overlapping_indexes.append(i)

        if len(set_overlapping_indexes) == 1:
            film_index = set_overlapping_indexes.pop()

    film_title = list(color_palettes.keys())[film_index]

    film_palettes = color_palettes[film_title]
    if palette is None:
        return film_palettes

    palette = palette if palette in range(len(film_palettes)) else 0

    return film_palettes[palette]
