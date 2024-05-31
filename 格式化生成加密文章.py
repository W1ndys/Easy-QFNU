# import os
from datetime import datetime
import pyperclip


def create_markdown_file():
    # 接受用户输入文件名和标题
    # filename = input("请输入文件名（不含后缀）：") + ".md"
    title = input("请输入标题：")

    # 获取当前日期
    current_date = datetime.now().strftime("%Y-%m-%d")

    # 生成Markdown内容
    markdown_content = f"""---
comments: true
level: SelectCourse
encryption_summary: 加密标题
encryption_info_message: 加密提示信息
---

# {title}

"""

    # ---

    # :material-clock-edit-outline:{{ title="修改日期" }} {current_date}
    # :material-clock-plus-outline:{{ title="创建日期" }} {current_date}

    # # 写入Markdown文件
    # with open(filename, "w", encoding="utf-8") as f:
    #     f.write(markdown_content)

    # print(f"Markdown文件 {filename} 创建成功！")

    # 复制内容到剪贴板
    pyperclip.copy(markdown_content)
    print("Markdown内容已复制到剪贴板。请按下Enter键退出。")

    input()


if __name__ == "__main__":
    create_markdown_file()
