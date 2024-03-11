#!/bin/bash

# ANSI颜色和风格设置
# Info信息：绿色
INFO='\033[0;32m'
# 成功信息：绿色
SUCCESS='\033[0;32m'
# 警告信息：黄色
WARNING='\033[0;33m'
# 错误信息：红色
ERROR='\033[0;31m'
# 恢复默认颜色
NC='\033[0m' # No Color

# 构建site
printf "${INFO}INFO${NC}: 构建site...\n"
mkdocs build

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
printf "${INFO}INFO${NC}: 复制文件到目标目录...\n"
cp -r "$site_dir"/* "$target_dir"
printf "${SUCCESS}INFO${NC}: 文件复制成功。\n"

# 进入目标目录
printf "${INFO}INFO${NC}: 进入目标目录...\n"
cd "$target_dir" || exit

# 执行Git命令
printf "${INFO}INFO${NC}: 执行Git命令...\n"
git add .
printf "${INFO}INFO${NC}: 请输入提交信息："
read commit_message
git commit -m "$commit_message"
git push
printf "${SUCCESS}INFO${NC}: 文件上传到Git仓库成功。\n"

# 删除最初的site文件夹
printf "${INFO}INFO${NC}: 删除最初的site文件夹...\n"
rm -rf "$site_dir"
printf "${SUCCESS}INFO${NC}: 最初的site文件夹已删除。\n"

# 提示用户按Enter键退出
printf "${INFO}INFO${NC}: 按Enter键退出...\n"
read -r
