# CSV - Comma Separated Values

import pathlib


DATA_FOLDER = pathlib.Path(__path__).joinpath("data")
SOURCE_FILE = DATA_FOLDER.joinpath("users.csv")

with open(SOURCE_FILE) as f:
    

    pass