# This dockerfile builds a container capable of running the hitch tests for
# Django-RemindMe. When building it runs the tests to ensure that all packages
# that need downloading and building are downloaded and built.
#
# To build this image (WARNING: this will take a while - maybe ~25 minutes):
#
#    docker build . -t remindme
#
# To rerun the tests (WARNING: uses xvfb - you won't be able to see firefox)
#
#    docker run -w="/home/hitch/django-remindme/django-remindme-tests/" -a stdin -a stdout -i -t remindme sh -c 'hitch test . --extra \'{\\"\"xvfb\\"\":true}\\' '

FROM ubuntu:14.04

RUN apt-get update && apt-get install -q -y \
    bzip2 ca-certificates hicolor-icon-theme libdbus-glib-1-2 libgl1-mesa-dri libgl1-mesa-glx \
    xvfb firefox xauth sudo python3 python-setuptools python3-dev python-virtualenv python-pip git \
    node-less automake libtool patch libreadline6 libreadline6-dev zlib1g-dev libxml2 libxml2-dev \
    make build-essential libssl-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libpq-dev xvfb xauth xserver-xorg \
    --no-install-recommends && sudo locale-gen en_US.UTF-8 && sudo dpkg-reconfigure locales

RUN sudo pip install hitch
RUN /usr/sbin/useradd hitch -m && /usr/sbin/adduser hitch sudo

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

WORKDIR /home/hitch

ADD . django-remindme

RUN chown -R hitch:hitch django-remindme

USER hitch
WORKDIR /home/hitch/django-remindme/django-remindme-tests

RUN hitch init
RUN hitch test . --extra '{"xvfb":true,"pause_on_failure":false}'

