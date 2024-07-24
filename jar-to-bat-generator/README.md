# JAR包对应的BAT文件生成器

这个 Python 脚本会自动遍历指定目录及其子目录，检查是否存在 JAR 文件，并生成相应的 BAT 文件，以 `java -jar` 命令启动这些 JAR 文件。

## 环境要求

- Python 3.x

## 使用方法

1. **克隆仓库或下载脚本：**

    ```sh
    git clone https://github.com/yourusername/jar-to-bat-generator.git
    cd jar-to-bat-generator
    ```

2. **运行脚本：**

    导航到包含脚本的目录并运行：

    ```sh
    python gen_jar_bat.py <path_to_directory>
    ```

    例如：

    ```sh
    python gen_jar_bat.py C:\hacker
    ```

    这将遍历 `C:\hacker` 目录及其子目录，为每个找到的 `.jar` 文件生成对应的 `.bat` 文件。

3. **检查结果：**

    脚本将遍历指定的根文件夹及其子目录，为每个找到的 `.jar` 文件生成对应的 `.bat` 文件。生成的 `.bat` 文件将位于与相应 `.jar` 文件相同的目录中。


