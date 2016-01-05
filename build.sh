#!/bin/bash

export ANDROIDSDK=/opt/android-sdk-linux
export ANDROIDNDK=/opt/android-ndk-r10e

export PATH="~/.local/bin/:$PATH"

#pip install --user cython==0.23.2
#pip install --user --upgrade git+https://github.com/kivy/python-for-android.git

#cd $WORKSPACE
#git clone https://github.com/brussee/SkeletonApp.git
#cd SkeletonApp

script -c "p4a --force_build --require_perfect_match --allow_download --debug apk" # uses .p4a config file
