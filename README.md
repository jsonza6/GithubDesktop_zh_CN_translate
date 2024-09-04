# Github_desktop_zh_CN_translate
Github desktop for windows 的汉化/中文翻译
# GitHub Desktop 汉化 中文为使用机械翻译，非人工校准！！！


## 项目简介

这是一个用于汉化 [GitHub Desktop](https://desktop.github.com/) 的脚本工具。该工具可以自动备份 GitHub Desktop 的关键文件，并将汉化的文件替换到指定目录中，从而实现界面的汉化。你还可以轻松地还原到原始版本。

## 功能特点

- **自动备份**：启动时自动备份 `main.js` 和 `renderer.js` 文件。
- **汉化**：自动替换为翻译后的文件，实现界面汉化。
- **还原**：可以还原到原始英文界面。
- **简单易用**：提供清晰的操作选项，支持汉化、还原和退出。

## 安装和使用

### 前提条件

- 已安装 GitHub Desktop，并确保路径正确
- （默认路径为 `C:\Users\{YourUsername}\AppData\Local\GitHubDesktop\app-3.4.3\resources\app`）。
- app-3.4.3 为2024年7月最新版
- 已翻译的 `main.js` 和 `renderer.js` 文件存放在 `translated/` 目录中。

### 安装步骤

1. **运行脚本**：
    - 双击运行 `github_desktop_translate.exe` 脚本，选择相应操作即可。

### 使用说明

1. **汉化 GitHub Desktop**：
    - 选择菜单中的 `1`，脚本将自动备份原始文件，替换为翻译后的文件，并重启 GitHub Desktop。
  
2. **还原 GitHub Desktop**：
    - 选择菜单中的 `2`，脚本将还原备份的原始文件，并重启 GitHub Desktop。
  
3. **退出程序**：
    - 选择菜单中的 `3` 退出程序。

## 文件结构

### 结构说明
- **`original/`**: 存放备份的 GitHub Desktop 原始文件 (`main.js` 和 `renderer.js`)。脚本启动时会自动将这些文件备份到这个目录。
  
- **`translated/`**: 存放翻译后的文件 (`main.js` 和 `renderer.js`)。这些文件是汉化后的版本，当用户选择汉化选项时，脚本会将这些文件复制到 GitHub Desktop 的安装目录。

- **`github_desktop_translate.exe`**: 这是主程序文件，用于执行备份、汉化、还原和重启 GitHub Desktop 的操作。

- **`README.md`**: 项目说明文件，提供项目简介、安装和使用说明、贡献指南等。

- **`LICENSE`**: 许可证文件（如果有），用于说明项目的许可条款。你可以根据项目需求选择适当的许可证，例如 MIT License。

- 此readme为人工智能生成的模板
