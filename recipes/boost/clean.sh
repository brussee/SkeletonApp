#!/bin/bash

cd ~

BOOST_VERSION=60
export BOOST_ROOT=/home/brussee/boost_1_${BOOST_VERSION}_0
export LIBTORRENT_ROOT=/home/brussee/libtorrent-1_0_8

export ARCH=arm
export CROSSHOST=$ARCH-linux-androideabi
export CROSSHOME=/home/brussee/custom-$ARCH-toolchain

export PYTHON_ROOT=


rm -rf $BOOST_ROOT
rm -rf $LIBTORRENT_ROOT
rm -rf $CROSSHOME
rm /home/brussee/user-config.jam


if [ ! -f libtorrent-1_0_8.tar.gz ]; then

    wget http://github.com/arvidn/libtorrent/archive/libtorrent-1_0_8.tar.gz
fi

tar xf libtorrent-1_0_8.tar.gz
mv libtorrent-libtorrent-1_0_8 libtorrent-1_0_8

if [ ! -f boost_1_${BOOST_VERSION}_0.tar.bz2 ]; then

    wget http://sourceforge.net/projects/boost/files/boost/1.${BOOST_VERSION}.0/boost_1_${BOOST_VERSION}_0.tar.bz2
fi

tar xf boost_1_${BOOST_VERSION}_0.tar.bz2
