# pip install & pip download

---

### 说明

将 pip的执行命令 封装成 python 执行的形式，便于pip包的下载 与离线安装。


- 1 下载对应版本到pip包到本地目录
    - win版本
    - any版本

- 2 安装离线包
   - 根据本地的路径 安装对应的包
   
- 3 可根据其他命令执行自定义的执行
    ```
    # pip 命令说明
    # https://pip.pypa.io/en/stable/user_guide/
    # pip uninstall SomePackage     卸载包
    # pip search SomePackage        卸载包
    # pip uninstall SomePackage     卸载包
    # pip show                      显示安装包信息
    # pip show -f SomePackage       查看指定包的详细信息
    # pip list                      列出已安装的包
    # pip list -o                   查看可升级的包
    ```