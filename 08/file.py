# get  path

# dunder properties, methods

# relative path
# __file__
import os
import pathlib


print(__file__)
# e:\Mega\gostudypro@gmail.com\Devops_2079_04Aug2025\CourseLessons\Lesson_008_29Aug2025\LessonFiles\Files_Folders_Access\script1.py
print(__file__.split("\\"))
# ['e:', 'Mega', 'gostudypro@gmail.com', 'Devops_2079_04Aug2025', 'CourseLessons', 'Lesson_008_29Aug2025', 'LessonFiles', 'Files_Folders_Access', 'script1.py']
print(__file__.split("\\")[-1])
print("\\".join(__file__.split("\\")[:-1]))
# e:\Mega\gostudypro@gmail.com\Devops_2079_04Aug2025\CourseLessons\Lesson_008_29Aug2025\LessonFiles\Files_Folders_Access

print("\\".join(__file__.split("\\")[:-1] + ["NEW_FOLDER"]))
# e:\Mega\gostudypro@gmail.com\Devops_2079_04Aug2025\CourseLessons\Lesson_008_29Aug2025\LessonFiles\Files_Folders_Access\NEW_FOLDER

print(os.sep)
print(os.sep.join(__file__.split(os.sep)[:-1] + ["NEW_FOLDER"]))

# absolute path
abs_path = r"c:\temp" # prefix r -> raw string, 


# modules: os, pathlib

# os
PROJECT_ROOT_PATH = os.path.dirname(__file__) # -> string
print(PROJECT_ROOT_PATH)
NEW_FILE_PATH = os.path.join(PROJECT_ROOT_PATH, "data_files", "test1.txt") # -> string
print(NEW_FILE_PATH)
# \LessonFiles\Files_Folders_Access\data_files\test1.txt

# pathlib
PROJECT_ROOT = pathlib.Path(__file__).parent # -> Path object
PROJECT_ROOT.joinpath("data_files", "test1.txt") 
PROJECT_ROOT.joinpath("data_files").joinpath("test1.txt") # -> Path object
print()

