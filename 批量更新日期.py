import os
import re
import datetime

# ANSI颜色码
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_DARK_GREEN = "\033[32m"
COLOR_PURPLE = "\033[95m"
COLOR_BLUE = "\033[94m"
COLOR_END = "\033[0m"


def print_color(text, color):
    print(f"{color}{text}{COLOR_END}")


def update_markdown_files(dir_path, exclude_paths):
    # 遍历docs目录下的所有文件
    for root, dirs, files in os.walk(dir_path):
        # 移除排除路径中的目录
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_paths]
        for file in files:
            # 获取文件的绝对路径
            file_path = os.path.join(root, file)

            # 判断文件路径是否在排除列表中
            if file_path in exclude_paths:
                print_color(f"\n跳过文件：{file_path}", COLOR_BLUE)
                continue

            if file.endswith(".md"):
                with open(file_path, "r+", encoding="utf-8") as f:
                    lines = f.readlines()

                    # 获取文件的创建时间和修改时间
                    create_time = datetime.datetime.fromtimestamp(
                        os.path.getctime(file_path)
                    ).strftime("%Y-%m-%d")
                    modify_time = datetime.datetime.fromtimestamp(
                        os.path.getmtime(file_path)
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
                                    print_color(
                                        f"\n{file_path} 日期已是最新\n", COLOR_GREEN
                                    )
                                    break
                                else:
                                    lines[i] = (
                                        f':material-clock-edit-outline:{{ title="修改日期" }} {modify_time}\n'
                                    )
                                    f.seek(0)
                                    f.writelines(lines)
                                    print_color(
                                        f"\n{file_path} 日期已修改，修改后的日期为：{modify_time}\n",
                                        COLOR_PURPLE,
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
                                print_color(
                                    f"\n{file_path} 已覆盖原有修改日期数据，修改后的日期为：{modify_time}\n",
                                    COLOR_PURPLE,
                                )
                                break
                    else:
                        # 没有日期数据，添加日期数据
                        lines.extend(
                            [
                                f'\n\n---\n\n:material-clock-edit-outline:{{ title="修改日期" }} {modify_time}\n:material-clock-plus-outline:{{ title="创建日期" }} {create_time}\n'
                            ]
                        )
                        f.seek(0)
                        f.writelines(lines)
                        print_color(f"\n{file_path} 无日期，已添加\n", COLOR_GREEN)


if __name__ == "__main__":
    # 获取当前目录下的docs目录路径
    docs_dir = os.path.join(os.getcwd(), "docs")
    # 构建排除文件的路径列表
    exclude_paths = [
        os.path.join(docs_dir, "update", "index.md"),
        os.path.join(docs_dir, "tags.md"),
        os.path.join(docs_dir, "嵌入测试.md"),
        # 添加要排除的目录
        os.path.join(docs_dir, "example_directory"),
        # os.path.join(docs_dir, "update"), # 排除更新日志的目录
    ]
    update_markdown_files(docs_dir, exclude_paths)
    input("按Ctrl+c退出程序...")
