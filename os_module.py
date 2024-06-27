import os

cwd = os.getcwd()
print(cwd)

files = os.listdir()
print("Files in current directory:", files)

new_dir = "test_directory"
os.mkdir(new_dir)
print(f"Directory '{new_dir}' created.")

if os.path.exists(new_dir):
    if os.path.isdir(new_dir):
        print(f"'{new_dir}' is a directory.")
    else:
        print(f"'{new_dir}' is a file.")
