#!/usr/bin/env ruby

# To use this Vagrant file, make sure that you have checked out this repo
# (and its submodule with git clone --recursive). Then::
#
# 1) vagrant up
# 2) Wait 25 minutes
# 3) vagrant ssh -c 'hitch test .'
#
# Note that using Vagrant in a directory which already has a .hitch directory and pyv* directories will cause weird errors.

$BOOTSTRAP_SCRIPT = <<EOF
echo Running bootstrap script...
echo export DISPLAY="127.0.0.1:10.0" >> ~/.bashrc
echo cd /vagrant/django-remindme-tests >> ~/.bashrc

sudo apt-get update
sudo apt-get install -q -y \
    bzip2 ca-certificates hicolor-icon-theme libdbus-glib-1-2 libgl1-mesa-dri libgl1-mesa-glx \
    xvfb firefox xauth sudo python3 python-setuptools python3-dev python-virtualenv python-pip git \
    node-less automake libtool patch libreadline6 libreadline6-dev zlib1g-dev libxml2 libxml2-dev \
    make build-essential libssl-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libpq-dev xvfb xauth xserver-xorg \
    --no-install-recommends

sudo locale-gen en_US.UTF-8 && sudo dpkg-reconfigure locales

sudo pip install hitch

cd /vagrant/django-remindme-tests
hitch clean
rm -rf ../pyv*
hitch init
hitch test . --extra '{"xvfb":true, "pause_on_failure":false}'
EOF

Vagrant.configure("2") do |config|
  config.vm.box = "trusty64"
  config.vm.box_url = 'https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box'
  config.vm.network :private_network, ip: "192.168.250.1"
  config.vm.provision :shell, privileged: false, :inline => $BOOTSTRAP_SCRIPT # see above
  config.ssh.forward_x11 = true
  config.vm.synced_folder ".", "/vagrant"

  config.vm.provider :virtualbox do |virtualbox|
    virtualbox.customize ["modifyvm", :id, "--memory", 4196]
  end

  config.vm.define :hitch do |node|
    node.vm.box = "trusty64"
    node.vm.hostname = "hitch"
    node.vm.network :private_network, ip: "192.168.250.2"
  end
end

