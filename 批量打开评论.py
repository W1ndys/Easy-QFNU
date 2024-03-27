import os
import re


def add_comments_true(file_path):
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
            print(f"{os.path.relpath(file_path)} 文件已执行完毕")
        else:
            updated_content = "---\ncomments: true\n---\n" + content
            file.seek(0)
            file.write(updated_content)
            file.truncate()
            print(f"{os.path.relpath(file_path)} 文件已执行完毕")


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
                add_comments_true(file_path)

    input("全部执行完毕，按Enter退出")


if __name__ == "__main__":
    main()
