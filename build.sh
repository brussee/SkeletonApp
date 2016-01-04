#!/bin/bash

export ANDROIDSDK=/opt/android-sdk-linux
export ANDROIDNDK=/opt/android-ndk-r10e

export PATH="~/.local/bin/:$PATH"

#pip install --user cython==0.21.2

#pip install --user git+https://github.com/kivy/python-for-android.git


RECIPES=~/.local/lib/python2.7/site-packages/pythonforandroid

MYRECIPES=~/repos/python-for-android/pythonforandroid/recipes

cp -r $MYRECIPES $RECIPES


#cd $WORKSPACE

#git clone https://github.com/brussee/SkeletonApp.git

#cd SkeletonApp

script -c "p4a --debug apk" # uses .p4a config file
