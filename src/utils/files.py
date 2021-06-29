from pathlib import Path


def get_main_dir():
    # Get path to project main directory
    main_directory = Path(__file__).resolve().parents[2]
    return main_directory
