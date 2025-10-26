# Path objects represent filesystem paths in an object-oriented way
from pathlib import Path

# the folder needs to be scanned
folder_path = 'sample_directory'
root = Path(folder_path) # Convert string path to Path object

# prepare output file path in Downloads folder
downloads = Path.home() / "Downloads" # get user's Downloads folder
output_file = downloads / "project_export.txt" # full output file path

# scan all directories and files
all_entries = list(root.rglob("*")) 
# rglob() returns a generator of all files and directories recursively
# '*' matches everything
# list(...) converts generator to a list so we can iterate multiple times if needed

# 'with open(...) as ...' safely opens a file and closes it automatically
with open(output_file, "w", encoding="utf-8") as out: # w' mode overwrites the file if it exists
    for entry in all_entries: # iterate over all files and directories found
        rel_path = entry.relative_to(root) # relative_to() converts absolute path to path relative to the project root
        
        # is_file() checks if the path is a file
        if entry.is_file():
            try:
                content = entry.read_text(encoding="utf-8").strip() # read_text() reads file contents as text; strip() removes extra whitespace/newlines at start/end
                if not content: # In Python, strings have truthy or falsy values: "" → False, "something" → True
                    content = "empty file." # if file is empty, we give it a placeholder
            except (UnicodeDecodeError, FileNotFoundError): # handle errors safely (encoding issues or missing file)
                content = "[Could not read file]"
            out.write(f"{rel_path}:\n{content}\n\n") # write the relative path and its content into the output file
        # is_dir() checks if the path is a directory
        elif entry.is_dir():
            # check if directory is empty: .iterdir() returns a generator, not a list. A generator is truthy by default — so if not entry.iterdir() will always be False.
            # any() will check if there is at least one file in that directory: If yes → any() returns True. If empty → any() returns False. So if not any(entry.iterdir()) correctly detects empty folders.
            if not any(entry.iterdir()): # iterdir() lists immediate entries in a directory; any(...) returns False if the directory has no files/folders
                out.write(f"{rel_path}:\n[empty folder]\n\n") # write placeholder for empty folder

# final message to user showing output file location
print(f"All files and empty folders exported to: {output_file}")
