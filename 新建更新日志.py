import os
from datetime import datetime

"""
主程序：创建并打开一个Markdown文件以记录每天的更新日志。
"""

# 获取当前日期，并格式化为年月日的字符串
current_date = datetime.now().strftime("%Y年%m月%d日")
current_date_iso = datetime.now().strftime("%Y-%m-%d")

# 构建文件路径，位于docs/update/posts目录下，文件名格式为"年月日.md"
file_path = os.path.join("docs", "update", "posts", f"{current_date}.md")

# 检查文件是否已存在；若存在，则直接打开文件
if os.path.exists(file_path):
    os.system(f"start {file_path}")
else:
    # 如果文件不存在，则创建并写入基础元数据和更新日志标题
    with open(file_path, "w", encoding="utf-8") as file:
        # 写入Markdown文件的元数据部分
        file.write(f"---\n")
        file.write(f"comments: true\n")
        file.write(f"authors: [W1ndys]\n")
        file.write(f"date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"---\n\n")
        # 写入更新日志的标题
        file.write(f"# {current_date_iso}\n\n")
        # 添加分隔符，用于内容扩展
        file.write(f"\n\n<!-- more -->\n\n\n\n")
        # 添加"修改日期"和"创建日期"的内容
        # file.write(
        #     f':material-clock-edit-outline:{{ title="修改日期" }} {current_date_iso}\n'
        # )
        # file.write(
        #     f':material-clock-plus-outline:{{ title="创建日期" }} {current_date_iso}'
        # )

    # 打开新创建的文件
    os.system(f"start {file_path}")  # 适用于Windows系统
