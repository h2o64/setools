FROM ubuntu:18.04

# install build dependencies
RUN apt-get update && \
    apt-get install -y sudo git \
                       gcc bison flex swig mock libbz2-dev \
                       libsepol1 libsepol1-dev gcc sepol-utils \
                       libselinux1 libselinux1-dev python-selinux selinux-utils python-dev \
                       python-enum34 python-pyqt5 python-setools python-pip python-mock python-tox \
                       networkx \
                       # Install SELinux userspace utilities dependencies
                       libaudit-dev libcap-ng-dev libustr-dev libpcre3-dev

# install runtime dependencies
RUN apt-get install -y python-networkx && \
    pip2 install tox && \
    pip2 install mock

# create an user 'docker'
RUN adduser --disabled-password --gecos '' docker && \
    adduser docker sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# switch to 'docker' user
USER docker
WORKDIR /home/docker

# define variables
ENV setools_repo https://github.com/h2o64/setools
ENV setools_rev HEAD

# clone repositories
RUN git clone ${setools_repo} setools && \
    cd ./setools/ && \
    git reset --hard ${setools_rev} && \
    # Download current SELinux userspace tools and libraries
    wget https://github.com/SELinuxProject/selinux/archive/20180524.tar.gz && \
    tar -xzf 20180524.tar.gz && mv selinux-20180524 selinux-src && \
    patch -p1 -d selinux-src < patches/libsepol-2.4-mls-semantic-level-expand.patch && \
    # Drop sepolicy to break setools4 dependence (sepolicy isn't used hereanyway)
    sed -i -e 's/sepolicy//' selinux-src/policycoreutils/Makefile && \
    # Compile and install SELinux toolchain
    sudo make CFLAGS="-O2 -pipe -fPIC -Wall" -C selinux-src install && \
		# Setup
    python setup.py build && \
    sudo python setup.py develop

# Try to reduce size of container.
RUN sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
