# open and read a file
f = open("sample_src/name_list.txt", "r") # "r" means read mode
lines = f.readlines() # reads all lines into a list
print(lines) # prints "['Alex\n', 'Bob\n', 'Jack\n', 'Jhon']"
f.close() # always close the file after use

# write a new file by copying content from another file
f = open("sample_src/name_list.txt", "r")
lines = f.readlines()
f.close()
f1 = open("sample_src/name_list_1.txt", "w") # "w" means write mode
f1.writelines(lines) # write the lines to the new file
f1.close()

# update content to an existing file
f = open("sample_src/name_list.txt", "r+") # "r+" means read and write mode
lines = f.readlines()
new_lines = []
for line in lines:
    new_line = "Hello " + line
    new_lines.append(new_line)
f.seek(0) # move the cursor to the beginning of the file
f.writelines(new_lines) # write the new lines to the file
f.close()

# open and read a binary file
f = open("sample_src/placeholder.png", "rb") # "rb" means read binary mode
print(f.readlines()) # read the file in binary mode
f.close()

# write a binary file by copying content from another binary file
f = open("sample_src/placeholder.png", "rb")
new_lines = f.readlines()
f.close()
f1 = open("sample_src/placeholder_1.png", "wb") # "wb" means write binary mode
f1.writelines(new_lines) # write the binary content to the new file
f1.close()

# with open statement to handle files: automatically closes the file after use
with open("sample_src/name_list.txt", "r") as f:
    print(f.readlines())


# --- This is a horizontal line for separation ---

# os module can be used to interact with the operating system
import os

file_path = 'sample_src/name_list.txt'

print(os.path.abspath(file_path))  # Get the absolute path of the file; prints "/Users/...noteverse/what_i_learnt/Python/0-basics/sample_src/name_list.txt"
print(os.path.basename(file_path)) # Get the base name of the file; prints "name_list.txt"
print(os.path.dirname(file_path))  # Get the directory name of the file; prints "sample_src"
print(os.path.exists(file_path))   # Check if the file exists; prints True
print(os.path.isdir(file_path))  # Check if the path is a directory; prints False
print(os.path.getsize(file_path))  # Get the size of the file in bytes; prints the size as an integer; e.g., 42

file_path2 = os.path.join("random_name", "name_list.txt")  # Join directory and file name into a full path
print(file_path2)  # prints "random_name/name_list.txt"

# create a new directory
file_path3 = os.path.join("sample_src", "new_dir")
os.mkdir(file_path3)

# remove the created directory
os.rmdir(file_path3)
