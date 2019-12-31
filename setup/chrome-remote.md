# Chrome



## chrome 설치

참고자료: https://snowdeer.github.io/linux/2018/02/02/ubuntu-16p04-install-chrome/

### wget 설치

```
$ sudo apt-get install libxss1 libgconf2-4 libappindicator1 libindicator7
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 
$ sudo dpkg -i google-chrome-stable_current_amd64.deb
```

### apt-get 설치

```
$ wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - 
$ sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
$ sudo apt-get update
$ sudo apt-get install google-chrome-stable
```

만약 설치 이후에 `apt-get update` 명령을 이용해서 패키지 목록을 업데이트 할 때, 다음과 같은 오류 메세지가 나오면

```
W: Target Packages (main/binary-amd64/Packages) is configured multiple times in /etc/apt/sources.list.d/google-chrome.list:3 and /etc/apt/sources.list.d/google.list:1
```

아래 명령을 수행한다.

```
$ sudo rm -rf /etc/apt/sources.list.d/google.list 
```



## 원격 설정

### Chrome Remote Desktop 설치

chrome 웹 스토어에서 "Chrome Remote Desktop" 검색 후 설치

혹은 여기로 바로 가기: <https://chrome.google.com/webstore/detail/chrome-remote-desktop/inomeogfingihgjfjlpeplalcfajhgai>

원격 데스크톱 상태 확인

```
$ systemctl status chrome-remote-desktop
● chrome-remote-desktop.service - LSB: Chrome Remote Desktop service
   Loaded: loaded (/etc/init.d/chrome-remote-desktop; generated)
   Active: active (exited) since Tue 2019-12-17 16:39:47 KST; 48min ago
     Docs: man:systemd-sysv-generator(8)
  Process: 858 ExecStart=/etc/init.d/chrome-remote-desktop start (code=exited, status=0/SUCCESS)

12월 17 16:39:39 ian-rtx chrome-remote-desktop[858]: Failure count for 'session' is now 0
12월 17 16:39:39 ian-rtx chrome-remote-desktop[858]: Failure count for 'host' is now 0
...
```



### 원격 컴퓨터 세팅

여기로 들어가서 원격 이름과 PIN 설정  

https://remotedesktop.google.com/access

여기에 나온대로 설정파일 수정

https://superuser.com/questions/778028/configuring-chrome-remote-desktop-with-ubuntu-gnome-14-04/850359#850359

```
$ sudo usermod -a -G chrome-remote-desktop [username]
$ /opt/google/chrome-remote-desktop/chrome-remote-desktop --stop
$ sudo cp /opt/google/chrome-remote-desktop/chrome-remote-desktop /opt/google/chrome-remote-desktop/chrome-remote-desktop.orig
$ sudo gedit /opt/google/chrome-remote-desktop/chrome-remote-desktop
```

"chrome-remote-desktop" 파일 내용 수정

```
...
DEFAULT_SIZES = "1920x1080"
...
# echo $DISPLAY로 DISPLAY_NUMBER 확인
FIRST_X_DISPLAY_NUMBER = 1
...
  def launch_session(self, x_args):
    self._init_child_env()
    self._setup_pulseaudio()
    self._setup_gnubby()
    #self._launch_x_server(x_args)
    #self._launch_x_session()
    display = self.get_unused_display_number()
    self.child_env["DISPLAY"] = ":%d" % display
```

수정, 저장 후 닫고 재시작

```
/opt/google/chrome-remote-desktop/chrome-remote-desktop --start
```



### 접속 컴퓨터 세팅

접속 컴퓨터에서는 Chrome Remote Desktop만 설치하면 됨
