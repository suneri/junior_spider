# spider course for junior engineers
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

5. 离线安装 Chrome 插件。安装方法：下载插件后，在 chrome 浏览器地址栏输入 chrome://extensions，选择 Load Unpacked 或者 加载，来执行安装。Chrome 浏览器插件的离线下载地址：
   1. JSONView: https://github.com/gildas-lormeau/JSONView-for-Chrome
   2. POSTMAN: https://github.com/postmanlabs/postman-app-support/releases
   3. POSTMAN INTERCEPTER: https://github.com/postmanlabs/postman-chrome-interceptor/releases

## Ubuntu 18 虚拟机环境

    1. 下载安装 Virtubox 
    2. 下载 虚拟机，下载完成后解压后，双击启动虚拟机。下载链接: https://pan.baidu.com/s/1qSTZ_rGe7AcJJo7vlVTp1w
    3. 密码为 xxxy