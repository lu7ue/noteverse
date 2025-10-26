# I'm following a tutorial on working with files in Python, here is the link: https://realpython.com/working-with-files-in-python/

# Table of Contents(of the tutorial):
# Python’s “with open(…) as …” Pattern
# Getting a Directory Listing
# Getting File Attributes
# Making Directories
# Filename Pattern Matching
# Traversing Directories and Processing Files
# Making Temporary Files and Directories
# Deleting Files and Directories
# Copying, Moving, and Renaming Files and Directories
# Archiving
# An Easier Way of Creating Archives
# Reading Multiple Files
# Conclusion

# not every topic is included here, only the ones I found might be useful for my project.

# --- opening, reading and writing files in Python ---
# use Python’s “with open(…) as …” pattern to open a text file and read its contents
with open('sample_directory/file3.txt', 'r') as file:
    data = file.read()
    print(data)

# pass in w as an argument to write data to a text file, it will replace any existing content
with open('sample_directory/file3.txt', 'w') as file:
    data = 'I will overwrite any existing content in the file3.txt.'
    file.write(data)
    print(data)

# pass in a as an argument to append data to a text file, it will add the new content to the end of the file
with open('sample_directory/file3.txt', 'a') as file:
    data = '\nThis line will be added to the end of the file3.txt.'
    file.write(data)
    print(data)

# note:
# The variable after 'as' is just a name you choose. They all mean: assign the opened file object to this variable.

# --- this is a horizontal line to separate different examples ---
# --- get information about files and directories ---

# there are multiple ways to work with file paths in Python:
# 1. os.listdir() - Returns a string array of all the objects' names in the directory
# 2. os.scandir() - Returns an iterator of all the objects, which include file attribute and path information
# 3. pathlib.Path.iterdir()	 - same as os.scandir(), but uses the pathlib module

import os
entries1 = os.listdir('sample_directory/')
print('Now we are listing the entries using os.listdir():')
for entry in entries1:
    print(entry)

entries2 = os.scandir('sample_directory/')
print('Now we are listing the entries using os.scandir():')
for entry in entries2:
    print(entry.name)

from pathlib import Path
print('Now we are listing the entries using pathlib.Path.iterdir():')
entries3 = Path('sample_directory/')
for entry in entries3.iterdir():
    print(entry.name)

# way 2 and way 3 return more information about each entry, such as its name, path, whether it is a file or directory, etc.
# notice: there is no .path attribute in pathlib.Path objects, since the object itself represents the path
entries4 = Path('sample_directory/')
print('Now we are listing the entries with more details using pathlib.Path.iterdir():')
for entry in entries4.iterdir():
    print(f'Name: {entry.name}, Path: {entry}, Is File: {entry.is_file()}, Is Dir: {entry.is_dir()}')

# here are some useful methods of pathlib.Path objects:
# .iterdir() - returns an iterator of all the objects in the directory
# .name - get the name of the file or directory
# .parent - get the parent directory of the path
# .suffix - get the suffix (file extension) of the file, eg. '.txt', '.py'
# .stem - get the name of the file without the suffix
# .resolve() - returns the absolute path of the file or directory
# .is_file() - returns True if the path is a file
# .is_dir() - returns True if the path is a directory
# .exists() - returns True if the file or directory exists
# .stat().st_size - returns the size of the file in bytes
# .stat().st_mtime - returns the time of last modification
# .stat().st_ctime - returns the time of creation
# .read_text(encoding='utf-8') - read the contents of a text file

# --- this is a horizontal line to separate different examples ---

# --- creating files and directories ---
# --- creating a single directory ---
import os
# if the directory already exists, it will raise a FileExistsError; 
# if the parent directory does not exist, it will raise a FileNotFoundError; 
# if the directory is not existing, it will create the directory.
os.mkdir('sample_directory/new_directory')

from pathlib import Path
# same as os.mkdir();
# the difference is that Path.mkdir() has an optional argument exist_ok: if set to True, it will not raise an error if the directory already exists.
Path('sample_directory/another_new_directory').mkdir(exist_ok=True)

# note: 
# Using Path() converts a plain string path (like 'sample_directory') into a Path object, which has dozens of useful methods you can call
# .rglob(), .relative_to(), .read_text(), etc.

# --- creating nested(multiple) directories ---
import os
# if the parent directories do not exist, it will create all the necessary parent directories as well.
# mode argument is optional, it sets the permissions of the newly created directories (default is 0o777): read, write, execute for owner, group and others.
os.makedirs('sample_directory/2025/10/25', mode=0o770)

import pathlib
# same as os.makedirs();
# the difference is that Path.mkdir() has an optional argument parents: if set to True, it will create all the necessary parent directories as well.
# usually, both parents=True and exist_ok=True will be set together to avoid errors.
pathlib.Path('sample_directory/2026/11/26').mkdir(parents=True, exist_ok=True)

# --- this is a horizontal line to separate different examples ---
# --- matching file patterns ---

import glob
# Returns a list of strings, each is a file path that matches the pattern.
# * → matches any number of characters
# ? → matches a single character
# [abc] → matches a, b, or c
all_txt_files = glob.glob('sample_directory/*.txt')
print('Listing all .txt files using glob.glob():\n')
print(all_txt_files)
# output: 
# Listing all .txt files using glob.glob():
# ['sample_directory/file3.txt', 'sample_directory/file4.txt']

from pathlib import Path
# Returns a generator of Path objects, not a list.
# Each Path object can be used with all Path methods (.name, .suffix, .is_file(), etc.).
# has the same pattern matching rules as glob.glob().
all_csv_files = Path('sample_directory/').glob('*.csv')
print('Listing all .csv files using pathlib.Path.glob():\n')
print(all_csv_files)
print(list(all_csv_files)) # convert generator to list to see actual paths
# output:
# Listing all .csv files using pathlib.Path.glob():
# <generator object Path.glob at 0x10549f230>>
# [PosixPath('sample_directory/file2.csv')]

# note: the .glob only shows the files in the current directory, but the .rglob can search recursively in all subdirectories as well.
all_csv_files_recursive = Path('sample_directory/').rglob('*.csv')
print('Listing all .csv files recursively using pathlib.Path.rglob():\n')
print(all_csv_files_recursive)
print(list(all_csv_files_recursive)) # convert generator to list to see actual paths
# output:
# Listing all .csv files recursively using pathlib.Path.rglob():
# <generator object Path.rglob at 0x105467230>
# [PosixPath('sample_directory/file2.csv'), PosixPath('sample_directory/sub_dir/another_csv.csv')]

# --- this is a horizontal line to separate different examples ---
# --- traverse a directory tree recursively ---

# os.walk() is a generator that lets you traverse a directory tree recursively.
# It yields a tuple for each directory in the tree.
# Generator → doesn’t load all files at once; it yields one directory at a time, very memory-efficient for large projects.

import os

for dirpath, dirnames, filenames in os.walk('sample_directory'):
    print('Current directory:', dirpath) # String of current directory
    print('Subdirectories:', dirnames) # List of subdirectory names
    print('Files:', filenames) # List of file names in that directory
    print('---')

# skip directories by modifying dirnames in-place
for dirpath, dirnames, filenames in os.walk('sample_directory'):
    if '.git' in dirnames:
        dirnames.remove('.git')  # skip .git folder

# usually combined with os.path.join() to get full file paths
for dirpath, dirnames, filenames in os.walk('sample_directory'):
    for f in filenames:
        full_path = os.path.join(dirpath, f) # 'sample_directory/sub_dir' + '/' + 'file1.txt' → 'sample_directory/sub_dir/file1.txt'
        print(full_path)
# output:
# sample_directory/file3.txt
# sample_directory/file4.txt
# sample_directory/file2.csv
# sample_directory/file1.py
# sample_directory/sub_dir/bar.py
# sample_directory/sub_dir/foo.py
# sample_directory/sub_dir_b/file4.txt
# sample_directory/sub_dir_c/config.py
# sample_directory/sub_dir_c/file5.txt

# note:
# When you use Path objects, you can join paths with the / operator instead of os.path.join().
# For example: full_path = Path(dirpath) / f

# --- this is a horizontal line to separate different examples ---
# --- using Path.home() to get the user's home directory ---
from pathlib import Path
# Path.home() is a class method of pathlib.Path that returns the home directory of the current user 
# (e.g. /Users/yourname on macOS/Linux or C:\Users\yourname on Windows).
print(Path.home())
