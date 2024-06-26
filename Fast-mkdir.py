# 用于快速创建文件和目录
# Author: https://github.com/W1ndys

import os

# 从外部文件读取路径
with open("paths.md", "r") as file:
    lines = file.read().splitlines()

# 提取有效的文件路径，并在路径前添加docs/
files_to_create = []
for line in lines:
    # 忽略Markdown注释和空行
    if line.strip().startswith("#") or not line.strip():
        continue
    # 处理Markdown列表项
    if line.strip().startswith("-"):
        file_path = "docs/" + line.strip()[1:].strip()
        files_to_create.append(file_path)

# 遍历文件路径列表，创建文件和目录
for file_path in files_to_create:
    # 获取目录路径
    dir_path = os.path.dirname(file_path)

    # 如果目录不存在，创建目录
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"目录已创建: {dir_path}")

    # 如果文件不存在，创建文件
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("")
        print(f"文件已创建: {file_path}")
    else:
        print(f"文件已存在，跳过创建: {file_path}")
