#!/bin/bash

# 获取当前目录的路径
current_dir=$(pwd)
# 构建site目录的路径
site_dir="$current_dir/site"
# 构建目标目录的路径
target_dir="$current_dir/../xkzb-Gitee"

# 检查目标目录是否存在，不存在则创建
if [ ! -d "$target_dir" ]; then
    mkdir "$target_dir"
fi

# 复制site目录下的所有文件到目标目录
cp -r "$site_dir"/* "$target_dir"

echo "文件复制成功。"

# 进入目标目录
cd "$target_dir" || exit

# 执行Git命令
git add .
read -p "请输入提交信息：" commit_message
git commit -m "$commit_message"
git push

echo "文件上传到Git仓库成功。"
