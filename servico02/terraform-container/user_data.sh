#!/bin/bash
yum install -y docker
systemctl enable docker
systemctl start docker
sudo chown $USER /var/run/docker.sock
docker run -p 80:80 -d nginx