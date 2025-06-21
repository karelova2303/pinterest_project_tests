from pathlib import Path


def path_images(file_name):
    return str(Path(__file__).parent.parent.parent.joinpath(f'resources/images/{file_name}'))