# NVidia



## Nvidia driver 설치

```
sudo apt-add-repository ppa:graphics-drivers/ppa
sudo apt remove nvidia*
sudo apt autoremove
sudo ubuntu-drivers autoinstall
```

참고자료: <https://askubuntu.com/questions/1077493/unable-to-install-nvidia-drivers-on-ubuntu-18-04/1077501>



## CUDA 설치

- 이곳을 참고하여 다운받을 cuda 버전 결정: <https://www.tensorflow.org/install/source>

- 다운로드: <https://developer.nvidia.com/cuda-toolkit-archive>

- CUDA 설치

```
sudo rm -rf /usr/local/cuda*

# 설치파일 실행
sudo ./cuda_xxxx_linux

Do you accept the previously read EULA?
accept/decline/quit:              accept

Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 410.48?
(y)es/(n)o/(q)uit: n

Install the CUDA 10.0 Toolkit?
(y)es/(n)o/(q)uit: y

Enter Toolkit Location
 [ default is /usr/local/cuda-10.0 ]: 

Do you want to install a symbolic link at /usr/local/cuda?
(y)es/(n)o/(q)uit: y

Install the CUDA 10.0 Samples?
(y)es/(n)o/(q)uit: n

```

- CUDA 버전확인

```
nvcc --version

# 만약 cuda를 설치했는데 nvcc가 없다고 하면 ~/.bashrc에 다음 두 줄 추가
export PATH="/usr/local/cuda-10.1/bin${PATH:+:${PATH}}"
export LD_LIBRARY_PATH="/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"
```



## CuDNN 설치

- 다운로드: <https://developer.nvidia.com/rdp/cudnn-archive>

- 압축 해제 후 복사해서 설치

```
sudo cp -r extracted_dir/cuda/include /usr/local/cuda
sudo cp -r extracted_dir/cuda/lib64 /usr/local/cuda
```

