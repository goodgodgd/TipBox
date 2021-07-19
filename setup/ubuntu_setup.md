# How to Setup Ubuntu 20.04



sudo apt update
sudo apt upgrade -y
sudo ubuntu-drivers install

- reboot



### naver whale

https://whale.naver.com/ko/download/linux/



### language

update language pack
sudo apt install fcitx-hangul
sudo fc-cache -f -v

- reboot



### python

https://github.com/pyenv/pyenv-installer

sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

sudo apt install -y llvm

curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

pyenv install 3.x

sudo snap install pycharm-community --classic



### CUDA

version: https://www.tensorflow.org/install/source

https://developer.nvidia.com/cuda-toolkit-archive

https://developer.nvidia.com/rdp/cudnn-archive



### Typora

https://support.typora.io/Typora-on-Linux/



### Development

sudo apt install build-essential git cmake



