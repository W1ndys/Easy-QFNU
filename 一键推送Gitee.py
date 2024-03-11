import subprocess
import os


def git_push():
    # 进入site目录
    os.chdir("site")

    # 执行git add
    subprocess.run(["git", "add", ".", "-f"])  # 强制添加

    # 提示用户输入commit信息
    commit_message = input("请输入commit信息: ")

    # 执行git commit
    subprocess.run(["git", "commit", "-m", commit_message])

    # 执行git push
    subprocess.run(["git", "push"])


if __name__ == "__main__":
    git_push()
