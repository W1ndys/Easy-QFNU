import os
import re

# ANSI 转义码
BLUE = "\033[94m"
GREEN = "\033[92m"
ENDC = "\033[0m"


def add_comments_true(file_path, docs_dir):
    # 构建排除文件的路径列表
    exclude_paths = [
        os.path.join(docs_dir, "嵌入测试.md"),
        os.path.join(docs_dir, "update", "index.md"),
    ]

    # 排除不需要修改的文件
    if file_path in exclude_paths:
        print(f"{BLUE}跳过文件: {os.path.relpath(file_path)}{ENDC}")
        return

    with open(file_path, "r+", encoding="utf-8") as file:
        content = file.read()
        match = re.search(r"^---\n(.*?)\n---\n", content, re.DOTALL)
        if match:
            metadata = match.group(1)
            if "comments" in metadata:
                new_metadata = re.sub(r"comments:.*", "comments: true", metadata)
                updated_content = content.replace(metadata, new_metadata)
            else:
                new_metadata = "comments: true\n" + metadata
                updated_content = content.replace(metadata, new_metadata)
            file.seek(0)
            file.write(updated_content)
            file.truncate()
            print(f"{GREEN}{os.path.relpath(file_path)} 文件已执行完毕{ENDC}")
        else:
            updated_content = "---\ncomments: true\n---\n" + content
            file.seek(0)
            file.write(updated_content)
            file.truncate()
            print(f"{GREEN}{os.path.relpath(file_path)} 文件已执行完毕{ENDC}")


def main():
    print(
        "此操作会递归遍历当前目录下的docs目录下所有Markdown文件并修改，请提前做好备份，按Enter开始运行。"
    )
    input()
    docs_dir = os.path.join(os.getcwd(), "docs")

    for root, dirs, files in os.walk(docs_dir):
        for file_name in files:
            if file_name.endswith(".md"):
                file_path = os.path.join(root, file_name)
                add_comments_true(file_path, docs_dir)

    input("全部执行完毕，请按 Ctrl+C 退出")


if __name__ == "__main__":
    main()
