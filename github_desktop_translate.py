import os
import shutil
import subprocess
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_github_desktop_path():
    user_profile = os.getenv('USERPROFILE')
    default_path = os.path.join(user_profile, r"AppData\Local\GitHubDesktop\app-3.4.3\resources\app")
    if os.path.exists(default_path):
        return default_path
    else:
        return input("无法找到指定路径，请手动输入GitHub Desktop的安装目录: ")

def backup_files(src, dst, files):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for file_name in files:
        src_file = os.path.join(src, file_name)
        dst_file = os.path.join(dst, file_name)
        if os.path.exists(src_file):
            if not os.path.exists(dst_file):
                shutil.copy(src_file, dst)
                logging.info(f"{file_name} 已备份到 {dst}")
            else:
                logging.info(f"{file_name} 已存在备份，跳过备份")
        else:
            logging.warning(f"{file_name} 不存在，无法备份")

def apply_translation(github_path, translated_path, files):
    for file_name in files:
        src_file = os.path.join(translated_path, file_name)
        dst_file = os.path.join(github_path, file_name)
        if os.path.exists(src_file):
            shutil.copy(src_file, dst_file)
            logging.info(f"{file_name} 已替换")
        else:
            logging.warning(f"{file_name} 不存在于翻译文件夹中，无法替换")

def restore_original_files(github_path, original_path, files):
    for file_name in files:
        src_file = os.path.join(original_path, file_name)
        dst_file = os.path.join(github_path, file_name)
        if os.path.exists(src_file):
            shutil.copy(src_file, dst_file)
            logging.info(f"{file_name} 已还原")
        else:
            logging.warning(f"{file_name} 备份文件不存在，无法还原")

def kill_github_desktop():
    try:
        subprocess.run(["taskkill", "/F", "/IM", "GitHubDesktop.exe"], check=True)
    except subprocess.CalledProcessError:
        logging.error("无法杀死 GitHub Desktop 进程")

def restart_github_desktop():
    user_profile = os.getenv('USERPROFILE')
    github_exe = os.path.join(user_profile, r"AppData\Local\GitHubDesktop\GitHubDesktop.exe")
    try:
        subprocess.Popen(github_exe)
    except FileNotFoundError:
        logging.error("无法找到 GitHub Desktop 可执行文件")

def main():
    github_path = get_github_desktop_path()
    original_path = "./original/"
    translated_path = "./translated/"
    files_to_process = ["renderer.js", "main.js"]

    logging.info("正在备份原始文件...")
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
            logging.info("GitHub Desktop 已经汉化并重启。")
        elif choice == "2":
            kill_github_desktop()
            restore_original_files(github_path, original_path, files_to_process)
            restart_github_desktop()
            logging.info("GitHub Desktop 已经还原并重启。")
        elif choice == "3":
            logging.info("程序退出。")
            sys.exit()
        else:
            logging.warning("无效选项，请重新输入。")

if __name__ == "__main__":
    main()