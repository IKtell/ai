# FACE RECOGNITION

使用`python match.py test1.jpg`来与`shit/`目录下的图片进行匹配，并输出匹配度最高的学号。



# 安装步骤
1. http://anaconda.com/download/ 下载anaconda2
2. 放到 目录下，命令：bash Anaconda2-5.1.0-Linux-x86_64.sh
3. echo 'export PATH="~/anaconda2/bin:$PATH"' >> ~/.bashrc

source ~/.bashrc

4. conda create --name python3 python=3.4
source activate python34

5. 改为清华源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes

cp ~/.condarc{,.bak}

cat ~/.condarc.bak  

vim ~/.condarc
修改为如下
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
show_channel_urls: true
如上

6. conda install -c menpo dlib=19

7. conda install scikit-image

