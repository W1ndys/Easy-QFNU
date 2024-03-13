import os
from datetime import datetime

"""
主程序：创建并打开一个Markdown文件以记录当前时间的更新日志。
"""

# 获取当前日期和时间，并格式化为年月日时分的字符串
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y年%m月%d日%H时%M分")

# 构建文件路径，位于docs/update/posts目录下，文件名格式为"年月日时分.md"
file_path = os.path.join("docs", "update", "posts", f"{formatted_datetime}.md")

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
        file.write(f"date: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"---\n\n")
        # 写入更新日志的标题
        file.write(f"# {formatted_datetime} 更新日志\n\n")
        # 添加分隔符，用于内容扩展
        file.write(f"\n\n<!-- more -->")

    # 打开新创建的文件
    os.system(f"start {file_path}")  # 适用于Windows系统
