import os
import re
import datetime

# 存储不需要修改的文件相对路径列表
exclude_files = ["update/index.md", "index.md"]


def update_markdown_files(dir_path):
    # 获取指定目录下的所有文件和子目录
    items = os.listdir(dir_path)

    for item in items:
        # 获取当前文件或目录的完整路径
        item_path = os.path.join(dir_path, item)

        if os.path.isdir(item_path):
            # 如果是目录，递归调用自身
            update_markdown_files(item_path)
        elif item.endswith(".md"):
            # 如果是Markdown文件，进行处理
            relative_path = os.path.relpath(item_path, start=dir_path)
            if relative_path not in exclude_files:
                with open(item_path, "r+", encoding="utf-8") as f:
                    lines = f.readlines()

                    # 获取文件的创建时间和修改时间
                    create_time = datetime.datetime.fromtimestamp(
                        os.path.getctime(item_path)
                    ).strftime("%Y-%m-%d")
                    modify_time = datetime.datetime.fromtimestamp(
                        os.path.getmtime(item_path)
                    ).strftime("%Y-%m-%d")

                    # 检查文件中是否已经有修改日期和创建日期的数据
                    has_update_date = False
                    has_create_date = False
                    for line in lines:
                        if re.match(
                            r':material-clock-edit-outline:{ title="修改日期" } \d{4}-\d{2}-\d{2}',
                            line.strip(),
                        ):
                            has_update_date = True
                        elif re.match(
                            r':material-clock-plus-outline:{ title="创建日期" } \d{4}-\d{2}-\d{2}',
                            line.strip(),
                        ):
                            has_create_date = True

                    # 更新或添加日期数据
                    if has_update_date and has_create_date:
                        # 已经有日期数据，检查是否需要更新
                        for i in range(len(lines)):
                            if re.match(
                                r':material-clock-edit-outline:{ title="修改日期" } \d{4}-\d{2}-\d{2}',
                                lines[i].strip(),
                            ):
                                if (
                                    lines[i].strip()
                                    == f':material-clock-edit-outline:{{ title="修改日期" }} {modify_time}'
                                ):
                                    print(f"{relative_path} 日期已是最新\n")
                                    break
                                else:
                                    lines[i] = (
                                        f':material-clock-edit-outline:{{ title="修改日期" }} {modify_time}\n'
                                    )
                                    f.seek(0)
                                    f.writelines(lines)
                                    print(
                                        f"{relative_path} 日期已修改，修改后的日期为：{modify_time}\n"
                                    )
                                    break
                    elif has_update_date and not has_create_date:
                        # 已经有修改日期，但没有创建日期，覆盖原有数据
                        for i in range(len(lines)):
                            if re.match(
                                r':material-clock-edit-outline:{ title="修改日期" } \d{4}-\d{2}-\d{2}',
                                lines[i].strip(),
                            ):
                                lines[i] = (
                                    f':material-clock-edit-outline:{{ title="修改日期" }} {modify_time}\n'
                                )
                                f.seek(0)
                                f.writelines(lines)
                                print(
                                    f"{relative_path} 已覆盖原有修改日期数据，修改后的日期为：{modify_time}\n"
                                )
                                break
                    else:
                        # 没有日期数据，添加日期数据
                        lines.extend(
                            [
                                f'\n---\n\n:material-clock-edit-outline:{{ title="修改日期" }} {modify_time}\n:material-clock-plus-outline:{{ title="创建日期" }} {create_time}\n'
                            ]
                        )
                        f.seek(0)
                        f.writelines(lines)
                        print(f"{relative_path} 无日期，已添加\n")


if __name__ == "__main__":
    # 获取当前目录下的docs目录路径
    docs_dir = os.path.join(os.getcwd(), "docs")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    update_markdown_files(docs_dir)
    input("按Ctrl+c退出程序...")
