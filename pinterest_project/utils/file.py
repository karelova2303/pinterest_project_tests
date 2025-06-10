from pathlib import Path
import pinterest_project


def abs_path_from_project(relative_path: str):
    return (
        Path(pinterest_project.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )


def path_images(file_name):
    return str(Path(__file__).parent.parent.parent.joinpath(f'resources/images/{file_name}'))