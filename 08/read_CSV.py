# CSV - Comma Separated Values

import pathlib


DATA_FOLDER = pathlib.Path(__file__).parent.joinpath("data")
SOURCE_FILE = DATA_FOLDER.joinpath("users.csv")

with open(SOURCE_FILE) as f:
    string_from_file = f.read()
    pass

print(string_from_file)

with open(SOURCE_FILE) as f:
    users = [  f.readlines()]
    pass

print(string_from_file)
for user in users:
    print(user)

#add new user

users.append(['125','Fon','Fonzales','fondra1x@patch.com','male','167.46.28.214'])

for user in users:
    print(user)