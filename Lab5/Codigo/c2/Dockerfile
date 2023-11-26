FROM ubuntu:16.10

# Use old-releases.ubuntu.com instead of archive.ubuntu.com or security.ubuntu.com
RUN sed -i -re 's/([a-z]{2}\.)?archive.ubuntu.com|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

RUN apt update
RUN apt install -y openssh-client
