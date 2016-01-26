#!/bin/bash

export BOOST_ROOT=/home/brussee/boost_1_60_0
export LIBTORRENT_ROOT=/home/brussee/libtorrent-1_0_8

export ANDROIDSDK=/opt/android-sdk-linux
export ANDROIDNDK=/opt/android-ndk-r10e
#export ANDROIDNDK=/home/brussee/crystax-ndk-10.3.1
export ANDROIDAPI=16

export ARCH=arm
export CROSSHOST=$ARCH-linux-androideabi
export CROSSHOME=/home/brussee/custom-$ARCH-toolchain

export SYSTEM=linux-x86_64
export TOOLCHAIN_VERSION=4.9
export TOOLCHAIN_PREFIX=$CROSSHOME/bin/$CROSSHOST

export PYTHON_ROOT=


# make custom toolchain
cd $ANDROIDNDK
./build/tools/make-standalone-toolchain.sh --arch=$ARCH --platform=android-$ANDROIDAPI --install-dir=$CROSSHOME --ndk-dir=$ANDROIDNDK --toolchain=$CROSSHOST-$TOOLCHAIN_VERSION --system=$SYSTEM

# compile Boost.Build engine with this custom toolchain
cd $BOOST_ROOT
./bootstrap.sh

cp ~/repos/SkeletonApp/recipes/boost/user-config.jam ~

# compile Boost libraries with Boost.Build
#script -c "./b2 -q toolset=gcc-$ARCH target-os=android threading=multi link=shared runtime-link=shared --with-system --with-filesystem --with-thread --with-date_time --prefix=$CROSSHOME install"


# compile libtorrent with boost libraries
cd $LIBTORRENT_ROOT

script -c "../boost_1_60_0/b2 -q toolset=gcc-$ARCH target-os=android threading=multi link=shared boost-link=shared boost=source --prefix=$CROSSHOME install"
