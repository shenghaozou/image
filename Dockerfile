FROM ubuntu
RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y htop
RUN apt-get install -y tmux
RUN apt-get install -y fio
RUN apt-get install -y python3
RUN apt-get install -y gdb
RUN apt-get install -y python-pip
RUN apt-get install -y strace
RUN pip install faulthandler
# RUN mkdir -p /bin/package
# RUN mkdir -p /bin/package3
# RUN mkdir -p /bin/10000files
# RUN mkdir -p /bin/2g
# ADD 2g /bin/2g
# ADD 10000files /bin/10000files
ADD install.sh /tmp/
RUN bash /tmp/install.sh -b -p /root/anaconda3
ADD fio /root/ 
ADD mmap_test.c /root/
ADD mmap_range.c /root/
# ADD package /bin/package/
ADD package3 /bin/package3/
