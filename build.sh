#!/bin/bash

export ANDROIDSDK=/opt/android-sdk-linux
export ANDROIDNDK=/opt/android-ndk-r10e

export PATH="~/.local/bin/:$PATH"

echo Get the latest P4A
pip install --user --upgrade git+https://github.com/kivy/python-for-android.git

echo Start build APK
script -c "p4a --force-build --require-perfect-match --debug apk" # uses .p4a config file

echo Move apk and log to dist dir
mkdir -p dist
mv --backup=t --target-directory=dist *.apk
mv --backup=t --target-directory=dist typescript
