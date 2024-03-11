import os
from datetime import datetime

# 获取当前日期和时间
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y年%m月%d日%H时%M分")

# 构建文件路径
file_path = os.path.join("docs", "update", "posts", f"{formatted_datetime}.md")

# 如果文件已存在，则直接打开
if os.path.exists(file_path):
    os.system(f"start {file_path}")
else:
    # 创建md文件并写入元数据
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"---\n")
        file.write(f"comments: true\n")
        file.write(f"authors: [W1ndys]\n")
        file.write(f"date: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"---\n\n")
        file.write(f"# {formatted_datetime} 更新日志\n\n")
        file.write(f"\n\n<!-- more -->")

    # 打开文件
    os.system(f"start {file_path}")  # 适用于Windows系统
