#!/bin/bash

export RECIPE=libsodium

export ANDROIDSDK=/opt/android-sdk-linux
export ANDROIDNDK=/opt/android-ndk-r10e

export PATH="~/.local/bin/:$PATH"

echo Delete the build files of a recipe
p4a clean_recipe_build $RECIPE --local_recipes .

script -c "p4a create --force-build --require-perfect-match --debug --android_api 16 --arch armeabi --bootstrap empty --local_recipes . --dist_name recipe --requirements $RECIPE"
