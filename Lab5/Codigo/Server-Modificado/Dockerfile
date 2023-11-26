FROM ubuntu:20.10

# Use old-releases.ubuntu.com instead of archive.ubuntu.com or security.ubuntu.com
RUN sed -i -re 's/([a-z]{2}\.)?archive.ubuntu.com|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y \
    openssh-client \
    openssh-server \
    tshark

# Create "test" user
RUN useradd -m -s /bin/bash test
# Create password for test user, password: test
RUN echo "test:test" | chpasswd

RUN echo "HostKey /etc/ssh/ssh_host_ecdsa_key" >> /etc/ssh/sshd_config
RUN echo "KexAlgorithms diffie-hellman-group-exchange-sha256" >> /etc/ssh/sshd_config
RUN echo "MACs hmac-sha2-512" >> /etc/ssh/sshd_config
RUN echo "Ciphers aes256-ctr" >> /etc/ssh/sshd_config

# Expose port 22 for SSH connection
EXPOSE 22

ENTRYPOINT service ssh restart && bash
