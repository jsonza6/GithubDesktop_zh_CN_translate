import os
import shutil
import subprocess
import sys

# GitHub Desktop 安装的固定路径
def get_github_desktop_path():
    # 固定路径
    path = r"C:\Users\Mi\AppData\Local\GitHubDesktop\app-3.4.3\resources\app"
    if os.path.exists(path):
        return path
    else:
        return input("无法找到指定路径，请手动输入GitHub Desktop的安装目录: ")

# 备份文件
def backup_files(src, dst, files):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for file_name in files:
        src_file = os.path.join(src, file_name)
        if os.path.exists(src_file):
            shutil.copy(src_file, dst)
            print(f"{file_name} 已备份到 {dst}")
        else:
            print(f"{file_name} 不存在，无法备份")

# 替换为翻译文件
def apply_translation(github_path, translated_path, files):
    for file_name in files:
        src_file = os.path.join(translated_path, file_name)
        dst_file = os.path.join(github_path, file_name)
        if os.path.exists(src_file):
            shutil.copy(src_file, dst_file)
            print(f"{file_name} 已替换")
        else:
            print(f"{file_name} 不存在于翻译文件夹中，无法替换")

# 还原原始文件
def restore_original_files(github_path, original_path, files):
    for file_name in files:
        src_file = os.path.join(original_path, file_name)
        dst_file = os.path.join(github_path, file_name)
        if os.path.exists(src_file):
            shutil.copy(src_file, dst_file)
            print(f"{file_name} 已还原")
        else:
            print(f"{file_name} 备份文件不存在，无法还原")

# 杀死 GitHub Desktop 进程
def kill_github_desktop():
    subprocess.run(["taskkill", "/F", "/IM", "GitHubDesktop.exe"])

# 重启 GitHub Desktop
def restart_github_desktop():
    github_exe = r"C:\Users\Mi\AppData\Local\GitHubDesktop\GitHubDesktop.exe"
    subprocess.Popen(github_exe)

# 主程序
def main():
    github_path = get_github_desktop_path()
    original_path = "./original/"
    translated_path = "./translated/"
    files_to_process = ["renderer.js", "main.js"]

    # 启动时自动备份原始文件
    print("正在备份原始文件...")
    backup_files(github_path, original_path, files_to_process)

    while True:
        print("\n请选择一个操作:")
        print("1. 汉化")
        print("2. 还原")
        print("3. 退出")
        choice = input("输入选项 (1/2/3): ")

        if choice == "1":
            kill_github_desktop()
            apply_translation(github_path, translated_path, files_to_process)
            restart_github_desktop()
            print("GitHub Desktop 已经汉化并重启。")
        elif choice == "2":
            kill_github_desktop()
            restore_original_files(github_path, original_path, files_to_process)
            restart_github_desktop()
            print("GitHub Desktop 已经还原并重启。")
        elif choice == "3":
            print("程序退出。")
            sys.exit()
        else:
            print("无效选项，请重新输入。")

if __name__ == "__main__":
    main()
