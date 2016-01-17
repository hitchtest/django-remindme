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
#    docker run -w="/home/hitch/django-remindme/django-remindme-tests/" -a stdin -a stdout -i -t remindme sh -c 'hitch test . --settings ci.settings'

FROM ubuntu:14.04

RUN apt-get update && apt-get install -q -y \
    python python-dev python-setuptools python-virtualenv python3 python3-dev automake libtool \
    --no-install-recommends && sudo locale-gen en_US.UTF-8 && sudo dpkg-reconfigure locales

RUN pip install hitch
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

