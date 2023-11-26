import os
from pprint import pprint
import re

def getNotes(directory):
    note_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
            else:
                continue
            with open(file_path, "r", encoding="utf-8") as f:
                first_line = f.readline().strip()
                if first_line.startswith("#!") and first_line[2:].strip().startswith(
                    "https://zhuanlan.zhihu.com/p/"
                ):
                    note_link = first_line[2:].strip()
                    print(f"FIND: {file_path}, {note_link}")
                else:
                    continue
                pattern = r"^#\s+(.*)$"
                headings = re.findall(pattern, f.read(), flags=re.MULTILINE)
                if len(headings) == 0:
                    print(f"ERROR: {file_path} has no heading")
                    continue
            note_files.append((file_path, headings[0], note_link))
    return sorted(note_files, key=lambda x: x[1])

README = "# 笔记目录\n\n"

README+= "## 技术笔记\n\n"
for note in getNotes("./技术笔记"):
    README += f"[{note[1]}]({note[2]})\n\n"

README+= "## 学习笔记\n\n"
for note in getNotes("./学习笔记"):
    README += f"[{note[1]}]({note[2]})\n\n"

README+= "## 想法\n\n"
for note in getNotes("./想法"):
    README += f"[{note[1]}]({note[2]})\n\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(README)

# print(README)