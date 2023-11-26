FROM ubuntu:20.10

# Use old-releases.ubuntu.com instead of archive.ubuntu.com or security.ubuntu.com
RUN sed -i -re 's/([a-z]{2}\.)?archive.ubuntu.com|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y \
    git \
    autoconf \
    gcc \
    zlib1g-dev \
    libssl-dev \
    make \
    wget

RUN wget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-8.3p1.tar.gz
RUN tar zxvf openssh-8.3p1.tar.gz
WORKDIR /openssh-8.3p1
RUN sed -i 's/8.3/?/' version.h

RUN ./configure
RUN make
RUN make install
