import os
import re

def remove_comments_true(file_path):
    with open(file_path, "r+", encoding="utf-8") as file:
        content = file.read()
        match = re.search(r"^---\n(.*?)\n---\n", content, re.DOTALL)
        if match:
            metadata = match.group(1)
            if "comments: true" in metadata:
                new_metadata = metadata.replace("comments: true", "comments: false")
                updated_content = content.replace(metadata, new_metadata)
                file.seek(0)
                file.write(updated_content)
                file.truncate()
                print(f"{os.path.relpath(file_path)} 已关闭评论")
            else:
                print(f"{os.path.relpath(file_path)} 已没有开启的评论")
        else:
            print(f"{os.path.relpath(file_path)} 没有元数据")


def main():
    print(
        "此操作会递归遍历当前目录下的docs目录下所有Markdown文件并关闭评论，请提前做好备份，按Enter开始运行。"
    )
    input()
    docs_dir = os.path.join(os.getcwd(), "docs")
    for root, dirs, files in os.walk(docs_dir):
        for file_name in files:
            if file_name.endswith(".md"):
                file_path = os.path.join(root, file_name)
                remove_comments_true(file_path)

    input("全部执行完毕，按Enter退出")


if __name__ == "__main__":
    main()
