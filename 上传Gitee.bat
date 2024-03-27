@echo off
chcp 65001 > nul
REM 构建site
echo INFO: 构建site...
mkdocs build

REM 获取当前目录的路径
SET "current_dir=%cd%"
REM 构建site目录的路径
SET "site_dir=%current_dir%\site"
REM 构建目标目录的路径
SET "target_dir=%current_dir%\..\xkzb-Gitee"

REM 检查目标目录是否存在，不存在则创建
IF NOT EXIST "%target_dir%" (
    mkdir "%target_dir%"
)

REM 复制site目录下的所有文件到目标目录
echo INFO: 复制文件到目标目录...
xcopy /s /e /y "%site_dir%" "%target_dir%"
echo INFO: 文件复制成功。

REM 进入目标目录
echo INFO: 进入目标目录...
cd /d "%target_dir%" || exit

REM 执行Git命令
echo INFO: 执行Git命令...
git add .
echo INFO: 请输入提交信息：
set /p commit_message=
git commit -m "%commit_message%"
git push
echo INFO: 文件上传到Git仓库成功。

REM 删除最初的site文件夹
echo INFO: 删除最初的site文件夹...
rmdir /s /q "%site_dir%"
echo INFO: 最初的site文件夹已删除。

REM 打开指定页面
start https://gitee.com/W1ndys/xkzb.qfnu.w1ndys.top/pages#/
