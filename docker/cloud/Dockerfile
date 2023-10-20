FROM ubuntu:latest

LABEL org.opencontainers.image.authors="Peter.Silva@ssc-spc.gc.ca"

ENV TZ="Etc/UTC" \
    DEBIAN_FRONTEND="noninteractive" \
    BUILD_PACKAGES="build-essential" 

RUN apt-get update &&\ 
    apt-get install -y python3-amqp python3-appdirs python3-dateparser python3-humanfriendly \
        python3-humanize python3-jsonpickle python3-netifaces python3-paramiko python3-pip \
        python3-psutil python3-watchdog python3-magic

# need version >= 1.5.1 to get MQTT v5 support, not in repos of 20.04 ... so get from pip.
RUN pip3 install paho-mqtt redis python-redis-lock

WORKDIR /src

COPY . /src

RUN python3 setup.py install

WORKDIR /root

CMD sr3 foreground --config $SR3_CONFIG --logStdout --no $SR3_INSTANCE