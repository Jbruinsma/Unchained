import random


def randomize_playlist(playlist, start_index: int = 0) -> list:
    selected_piece = playlist.music_pieces[start_index]
    remaining_pieces = playlist.music_pieces[:start_index] + playlist.music_pieces[start_index + 1:]
    random.shuffle(remaining_pieces)
    queue = [selected_piece] + remaining_pieces
    return queue