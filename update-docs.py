import re
import datetime
import os
import requests


def get_github_file_info(repo_owner, repo_name, file_path, github_token):
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits?path={file_path}"
    headers = {"Authorization": f"token {github_token}"}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        commits = response.json()
        if commits:
            create_time = datetime.datetime.fromisoformat(
                commits[-1]["commit"]["committer"]["date"].replace("Z", "+00:00")
            ).strftime("%Y-%m-%d")
            update_time = datetime.datetime.fromisoformat(
                commits[0]["commit"]["committer"]["date"].replace("Z", "+00:00")
            ).strftime("%Y-%m-%d")
            return create_time, update_time
        else:
            print("未找到", file_path, "的提交记录。")
    else:
        print(f"错误：{response.status_code} - {response.text}")
    return None, None


def get_relative_path_from_docs(file_path):
    return "docs/" + file_path.split("docs/", 1)[-1] if "docs/" in file_path else None


def update_markdown_files(dir_path, exclude_paths, repo_owner, repo_name, github_token):
    for root, dirs, files in os.walk(dir_path):
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_paths]
        for file in files:
            file_path = os.path.join(root, file)

            if file_path in exclude_paths:
                print(f"跳过文件：{file_path}")
                continue

            if file.endswith(".md"):
                file_path = file_path.replace("\\", "/")  # 路径分隔符统一为/
                relative_path = get_relative_path_from_docs(file_path)
                if relative_path is None:
                    print(f"跳过非法路径文件：{file_path}")
                    continue
                create_time, update_time = get_github_file_info(
                    repo_owner, repo_name, relative_path, github_token
                )
                print("-----------------------------------------------------------")
                print(f"即将更新文件：{relative_path}\n")
                print(f"创建日期：{create_time}，更新日期：{update_time}\n")

                if create_time is None or update_time is None:
                    print(f"{file_path} 未找到Github的提交记录，跳过")
                    continue
                with open(file_path, "r+", encoding="utf-8") as f:
                    lines = f.readlines()
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

                    if has_update_date and has_create_date:
                        for i in range(len(lines)):
                            if re.match(
                                r':material-clock-edit-outline:{ title="修改日期" } \d{4}-\d{2}-\d{2}',
                                lines[i].strip(),
                            ):
                                if (
                                    lines[i].strip()
                                    == f':material-clock-edit-outline:{{ title="修改日期" }} {update_time}'
                                ):
                                    print(f"{file_path} 日期已是最新")
                                    break
                                else:
                                    lines[i] = (
                                        f':material-clock-edit-outline:{{ title="修改日期" }} {update_time}\n'
                                    )
                                    f.seek(0)
                                    f.writelines(lines)
                                    print(
                                        f"{file_path} 日期已修改，修改后的日期为：{update_time}"
                                    )
                                    break
                    else:
                        lines.extend(
                            [
                                f'\n\n---\n\n:material-clock-edit-outline:{{ title="修改日期" }} {update_time}\n:material-clock-plus-outline:{{ title="创建日期" }} {create_time}\n'
                            ]
                        )
                        f.seek(0)
                        f.writelines(lines)
                        print(f"{file_path} 无日期，已添加")
                print("-----------------------------------------------------------")


if __name__ == "__main__":
    docs_dir = os.path.join(os.getcwd(), "docs")
    exclude_paths = [
        os.path.join(docs_dir, "update", "index.md"),
        os.path.join(docs_dir, "tags.md"),
        os.path.join(docs_dir, "嵌入测试.md"),
        os.path.join(docs_dir, "example_directory"),
        os.path.join(docs_dir, "Update"),
    ]
    repo_owner = "Easy-QFNU"
    repo_name = "Easy-QFNU"

    github_token = os.environ.get("GITHUB_TOKEN")

    update_markdown_files(docs_dir, exclude_paths, repo_owner, repo_name, github_token)
