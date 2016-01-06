#!/bin/bash

export ADB=/opt/android-sdk-linux/platform-tools/adb

cd dist

#find the first apk
export APK=$(find -type f -name "*.apk" | head -n1)

echo Uninstall app
$ADB uninstall org.tribler.android

echo Deploy $APK
$ADB install $APK

echo Launch app
$ADB shell monkey -p org.tribler.android -c android.intent.category.LAUNCHER 1
#$ADB shell am start -n org.tribler.android/org.kivy.android.PythonActivity

echo Make screenshot
$ADB shell screencap -p | sed 's/\r$//' > screen.png
