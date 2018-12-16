# spider-course-4
Spider course 4 sample, Python 3.6

## 环境搭建
1. 安装 python 3.6 
2. 安装 pip
    1. Linux 
    
        参考 https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers

    2. Windows
        
        \# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        
        \# python get-pip.py
3. 配置 pip 为清华源
    1. Linux、MacOS

        \# vim ~/.config/pip/pip.conf
        
        [global]<br>
        index-url = https://pypi.tuna.tsinghua.edu.cn/simple 
    
    2. Windows

        %APPDATA%\pip\pip.ini

        [global]<br>
        index-url = https://pypi.tuna.tsinghua.edu.cn/simple 
4. 统一安装全部需要的依赖库，执行下面的命令

    \#pip install -r requirements.txt 

## Ubuntu 18 虚拟机环境

    1. 下载安装 Virtubox 
    2. 下载 虚拟机，下载完成后解压后，双击启动虚拟机。下载链接: https://pan.baidu.com/s/1Rns_T6Pr3prMtXdQJOkgug 密码: kaq8
    3. 密码为 xxxy