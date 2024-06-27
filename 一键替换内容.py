import os
import re


def replace_contact_author(content):
    """
    将内容中的所有'【联系作者】'替换为'**联系作者**'。
    """
    return re.sub(r"-------------曲阜-------------", "### 曲阜", content)


def process_file(file_path):
    """
    处理单个Markdown文件，将'【联系作者】'替换为'**联系作者**'。
    """
    print(f"正在处理文件: {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    new_content = replace_contact_author(content)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_content)
    print(f"文件处理完成: {file_path}")


def process_directory(directory_path):
    """
    递归处理目录中的所有Markdown文件。
    """
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                process_file(file_path)
    print(f"目录处理完成: {directory_path}")


if __name__ == "__main__":
    directory_path = os.getcwd()  # 使用当前目录
    print(f"开始处理目录: {directory_path}")
    process_directory(directory_path)
    print("所有文件处理完成")
