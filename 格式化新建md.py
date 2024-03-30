import os
from datetime import datetime


def create_markdown_file():
    # 接受用户输入文件名和标题
    filename = input("请输入文件名（不含后缀）：") + ".md"
    title = input("请输入标题：")

    # 获取当前日期
    current_date = datetime.now().strftime("%Y-%m-%d")

    # 生成Markdown内容
    markdown_content = f"""---
comments: true
---

# {title}

---

:material-clock-edit-outline:{{ title="修改日期" }} {current_date}
:material-clock-plus-outline:{{ title="创建日期" }} {current_date}
"""

    # 写入Markdown文件
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"Markdown文件 {filename} 创建成功！")

    # 打开Markdown文件
    os.system(f"start {filename}")


if __name__ == "__main__":
    create_markdown_file()
