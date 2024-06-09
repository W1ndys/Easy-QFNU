import os

# 要添加的元数据
metadata_key = "template:"
metadata_value = "Cyber-css.html"
metadata = f"{metadata_key} {metadata_value}"


# 获取当前目录及其所有子目录中的 Markdown 文件
def get_markdown_files(root_dir):
    markdown_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files


# 检查文件是否包含元数据块
def has_metadata_block(lines):
    metadata_block_start = False
    for line in lines:
        if line.strip() == "---":
            if metadata_block_start:
                return True
            else:
                metadata_block_start = True
    return False


# 检查文件是否包含指定元数据
def contains_metadata(lines, metadata_key):
    for line in lines:
        if line.strip().startswith(metadata_key):
            return True
    return False


# 在 YAML 前置元数据块中添加元数据
def add_metadata(lines, metadata_key, metadata):
    in_metadata_block = False
    for i, line in enumerate(lines):
        if line.strip() == "---":
            if in_metadata_block:
                # 结束元数据块的位置
                if not contains_metadata(lines[:i], metadata_key):
                    lines.insert(i, metadata + "\n")
                return lines
            else:
                # 开始元数据块的位置
                in_metadata_block = True
    return lines


# 如果没有元数据块，则添加完整的元数据块
def add_full_metadata_block(lines, metadata):
    new_lines = ["---\n", "comments: true\n", metadata + "\n", "---\n\n"]
    return new_lines + lines


# 读取文件内容
def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.readlines()


# 写入文件内容
def write_file(filepath, lines):
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(lines)


# 主函数
def main():
    root_dir = "."  # 当前目录
    markdown_files = get_markdown_files(root_dir)

    for filepath in markdown_files:
        lines = read_file(filepath)
        if has_metadata_block(lines):
            if not contains_metadata(lines, metadata_key):
                lines = add_metadata(lines, metadata_key, metadata)
                write_file(filepath, lines)
                print(f"已添加元数据到文件: {filepath}")
            else:
                print(f"文件已包含元数据: {filepath}")
        else:
            lines = add_full_metadata_block(lines, metadata)
            write_file(filepath, lines)
            print(f"已添加完整的元数据块到文件: {filepath}")


if __name__ == "__main__":
    main()
