import sys
import os
from datetime import datetime

directories = []
file_name = ""

current_mode = None
for i in range(1, len(sys.argv)):
    if sys.argv[i] == "-d":
        current_mode = "dir"
    elif sys.argv[i] == "-f":
        current_mode = "file"
    else:
        if current_mode == "dir":
            directories.append(sys.argv[i])
        elif current_mode == "file" and not file_name:
            file_name = sys.argv[i]

if directories != []:
    folder_path = os.path.join(*directories)
    os.makedirs(folder_path, exist_ok=True)

if file_name:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines = []
    line_number = 1
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        formatted_line = f"{line_number} {line}\n"
        content_lines.append(formatted_line)
        line_number += 1

    full_path = os.path.join(*directories, file_name)

    if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
        with open(full_path, "a") as file:
            file.write("\n")

    with open(full_path, "a") as file:
        file.write(f"{timestamp}\n")
        file.writelines(content_lines)
