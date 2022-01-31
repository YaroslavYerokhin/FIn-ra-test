**Установка docker:**

 $ sudo apt-get update
 
 $ sudo apt-get install
 
 $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg
 
 $ sudo apt-get install docker-ce docker-ce-cli containerd.io
 
**Установка selenoid**

 $ sudo wget https://github.com/aerokube/cm/releases/download/1.8.1/cm_linux_amd64
 
 $ chmod +x cm
 
 $ ./cm selenoid start --vnc
 
**Установка selenoid UI**

 $ ./cm selenoid-ui start
 
 В браузере перейти на http://localhost:8080/#/
 
**Запуск тестов**

 Python3 check_new_goal.py  or  pytest check_new_goal.py
