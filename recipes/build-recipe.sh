#!/bin/bash

export RECIPE=leveldb

export ANDROIDSDK=/opt/android-sdk-linux
export ANDROIDNDK=/opt/android-ndk-r10e

export PATH="~/.local/bin/:$PATH"


#pip install --user --upgrade git+https://github.com/kivy/python-for-android.git

#bugfix missing dir
mkdir -p ~/.local/lib/python2.7/site-packages/pythonforandroid/bootstraps/empty/build

#workaround local recipes patches
cp -R ~/repos/SkeletonApp/recipes/$RECIPE/ ~/.local/lib/python2.7/site-packages/pythonforandroid/recipes/


echo Delete the build files of a recipe
p4a clean_recipe_build $RECIPE --local_recipes .

script -c "p4a create --force-build --require-perfect-match --debug --android_api 16 --arch armeabi --bootstrap empty --dist_name recipe --requirements $RECIPE"
