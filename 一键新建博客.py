import os
from datetime import datetime

# 获取当前日期
current_date = datetime.now().strftime("%Y-%m-%d")

# 构建文件路径
file_path = os.path.join("docs", "update", "posts", f"{current_date}.md")

# 创建md文件并写入元数据
with open(file_path, "w", encoding="utf-8") as file:
    file.write(f"---\n")
    file.write(f"date: {current_date}\n")
    file.write(f"---\n\n")
    file.write(f"# {current_date} 更新日志\n\n")
    file.write(f"<!-- more -->")

# 打开文件
os.system(f"start {file_path}")  # 适用于Windows系统
