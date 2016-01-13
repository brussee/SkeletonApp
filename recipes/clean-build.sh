#!/bin/bash

export RECIPE=libtorrent

export ANDROIDSDK=/opt/android-sdk-linux
export ANDROIDNDK=/opt/android-ndk-r10e

export PATH="~/.local/bin/:$PATH"


#bugfix missing dir
#mkdir -p /home/paul/.local/lib/python2.7/site-packages/pythonforandroid/bootstraps/empty/build

#bugfix private recipe sources
#cp /home/paul/repos/SkeletonApp/recipes/boost/project-config.jam /home/paul/.local/lib/python2.7/site-packages/pythonforandroid/recipes/boost/
#cp /home/paul/repos/SkeletonApp/recipes/boost/user-config.jam /home/paul/.local/lib/python2.7/site-packages/pythonforandroid/recipes/boost/

#bugfix download from sourceforge
#pip install --user --upgrade git+https://github.com/brussee/python-for-android.git@fix-573


echo Delete the build files of a recipe
p4a clean_recipe_build $RECIPE --local_recipes .

script -c "p4a create --force-build --require-perfect-match --debug --android_api 16 --arch armeabi --bootstrap empty --local_recipes . --dist_name recipe --requirements $RECIPE"
