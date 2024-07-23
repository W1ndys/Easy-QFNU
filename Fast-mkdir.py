# 用于快速创建文件和目录
# Author: https://github.com/W1ndys

import os
import time

# 从外部文件读取路径
with open("paths.md", "r", encoding="utf-8") as file:
    lines = file.read().splitlines()

# 提取有效的文件路径和标题，并在路径前添加docs/
files_to_create = []
for line in lines:
    # 忽略Markdown注释、HTML注释和空行
    if (
        line.strip().startswith("#")
        or line.strip().startswith("<!--")
        or not line.strip()
    ):
        continue
    # 处理Markdown列表项并提取路径和标题
    if line.strip().startswith("-"):
        parts = line.strip().split(":")
        if len(parts) == 2:
            title = parts[0].strip()[1:].strip()  # 获取标题
            file_path = "docs/" + parts[1].strip()  # 获取路径
            files_to_create.append((file_path, title))

# 遍历文件路径列表，创建文件和目录
for file_path, title in files_to_create:
    # 获取目录路径
    dir_path = os.path.dirname(file_path)

    # 如果目录不存在，创建目录
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"目录已创建: {dir_path}")

    # 如果文件不存在，创建文件并写入内容
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"---\ncomments: true\n---\n\n# {title}\n\n> 内容施工中...")
        print(f"文件已创建: {file_path}")
    else:
        print(f"文件已存在，跳过创建: {file_path}")


print("所有文件和目录创建完成！程序将在5秒后退出。")

time.sleep(5)
