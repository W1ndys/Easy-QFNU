#!/bin/bash

# 删除旧的 .git 目录
echo "删除旧的 .git 目录..."
rm -rf .git

# 初始化新的 git 仓库
echo "初始化新的 git 仓库..."
git init

# 创建并切换到 main 分支
echo "切换到 main 分支..."
git checkout -b main

# 添加所有文件
echo "添加所有文件到暂存区..."
git add .

# 创建初始提交
echo "创建初始提交..."
git commit -m "feat(init): 重新初始化仓库"

# 添加远程仓库
echo "添加远程仓库..."
git remote add origin "git@github.com:W1ndys/Easy-QFNU.git"

# 强制推送到远程仓库
echo "强制推送到远程仓库..."
git push -f origin main

echo "完成！仓库已重新初始化并推送到 GitHub。"