#!/bin/bash

export RECIPE=libtorrent

export ANDROIDSDK=/opt/android-sdk-linux
export ANDROIDNDK=/opt/android-ndk-r10e

export PATH="~/.local/bin/:$PATH"


#pip install --user --upgrade git+https://github.com/kivy/python-for-android.git

#bugfix missing dir
mkdir -p ~/.local/lib/python2.7/site-packages/pythonforandroid/bootstraps/empty/build

#workaround local recipe sources
mkdir -p ~/.local/lib/python2.7/site-packages/pythonforandroid/recipes/boost
cp ~/repos/SkeletonApp/recipes/boost/user-config.jam ~/.local/lib/python2.7/site-packages/pythonforandroid/recipes/boost/user-config.jam
cp ~/repos/SkeletonApp/recipes/boost/disable-so-version.patch ~/.local/lib/python2.7/site-packages/pythonforandroid/recipes/boost/disable-so-version.patch
cp ~/repos/SkeletonApp/recipes/boost/use-android-libs.patch ~/.local/lib/python2.7/site-packages/pythonforandroid/recipes/boost/use-android-libs.patch

mkdir -p ~/.local/lib/python2.7/site-packages/pythonforandroid/recipes/libtorrent
cp ~/repos/SkeletonApp/recipes/libtorrent/disable-so-version.patch ~/.local/lib/python2.7/site-packages/pythonforandroid/recipes/libtorrent/disable-so-version.patch


echo Delete the build files of a recipe
p4a clean_recipe_build $RECIPE --local_recipes .

script -c "p4a create --force-build --require-perfect-match --debug --android_api 16 --arch armeabi --bootstrap empty --local_recipes . --dist_name recipe --requirements $RECIPE"
