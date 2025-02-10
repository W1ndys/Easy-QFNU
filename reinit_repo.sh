# 创建新的孤立分支
git checkout --orphan latest_branch

# 添加所有文件
git add -A

# 提交更改
git commit -m "feat(init): 初始化仓库"

# 删除主分支
git branch -D main

# 将当前分支重命名为主分支
git branch -m main

# 强制推送到远程仓库
git push -f origin main

# 删除所有旧的引用
git gc --aggressive --prune=all