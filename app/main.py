__version__ = '1.0'
import sys
sys.stdout.write("import App")
sys.stdout.flush()
from kivy.app import App
sys.stdout.write("import ScreenManager, Screen")
sys.stdout.flush()
from kivy.uix.screenmanager import ScreenManager, Screen
sys.stdout.write("import BoxLayout")
sys.stdout.flush()
from kivy.uix.boxlayout import BoxLayout
sys.stdout.write("import Widget")
sys.stdout.flush()
from kivy.uix.widget import Widget
sys.stdout.write("import Window")
sys.stdout.flush()
from kivy.core.window import Window
sys.stdout.write("import Builder")
sys.stdout.flush()
from kivy.lang import Builder
sys.stdout.write("import Clock")
sys.stdout.flush()
from kivy.clock import Clock
sys.stdout.write("import AnchorLayout")
sys.stdout.flush()
from kivy.uix.anchorlayout import AnchorLayout
sys.stdout.write("import ObjectProperty, ListProperty")
sys.stdout.flush()
from kivy.properties import ObjectProperty, ListProperty

sys.stdout.write("import android")
sys.stdout.flush()
import android
sys.stdout.write("import os")
sys.stdout.flush()
import os
sys.stdout.write("import io")
sys.stdout.flush()
import io
sys.stdout.write("import threading")
sys.stdout.flush()
import threading

sys.stdout.write("import AndroidCamera")
sys.stdout.flush()
from androidcamera import AndroidCamera
sys.stdout.write("import HomeScreen")
sys.stdout.flush()
from homescreen import HomeScreen
sys.stdout.write("import FileWidget")
sys.stdout.flush()
from filewidget import FileWidget

sys.stdout.write("import globalvars")
sys.stdout.flush()
import globalvars

sys.stdout.write("import autoclass, cast, detach")
sys.stdout.flush()
from jnius import autoclass, cast, detach
sys.stdout.write("jnius import JavaClass")
sys.stdout.flush()
from jnius import JavaClass
sys.stdout.write("import PythonJavaClass")
sys.stdout.flush()
from jnius import PythonJavaClass
sys.stdout.write("import run_on_ui_thread")
sys.stdout.flush()
from android.runnable import run_on_ui_thread

sys.stdout.write("Context")
sys.stdout.flush()
Context = autoclass('android.content.Context')
sys.stdout.write("PythonActivity")
sys.stdout.flush()
PythonActivity = autoclass('org.kivy.android.PythonActivity')
sys.stdout.write("Intent")
sys.stdout.flush()
Intent = autoclass('android.content.Intent')
sys.stdout.write("Uri")
sys.stdout.flush()
Uri = autoclass('android.net.Uri')
sys.stdout.write("NfcAdapter")
sys.stdout.flush()
NfcAdapter = autoclass('android.nfc.NfcAdapter')
sys.stdout.write("File")
sys.stdout.flush()
File = autoclass('java.io.File')
sys.stdout.write("CreateNfcBeamUrisCallback")
sys.stdout.flush()
CreateNfcBeamUrisCallback = autoclass('org.test.CreateNfcBeamUrisCallback')
sys.stdout.write("MediaStore")
sys.stdout.flush()
MediaStore = autoclass('android.provider.MediaStore')
sys.stdout.write("MediaRecorder")
sys.stdout.flush()
MediaRecorder = autoclass('android.media.MediaRecorder')
sys.stdout.write("Camera")
sys.stdout.flush()
Camera = autoclass('android.hardware.Camera')
sys.stdout.write("CamCorderProfile")
sys.stdout.flush()
CamCorderProfile = autoclass('android.media.CamcorderProfile')
sys.stdout.write("TextUtils")
sys.stdout.flush()
TextUtils = autoclass('android.text.TextUtils')
sys.stdout.write("MediaColumns")
sys.stdout.flush()
MediaColumns = autoclass('android.provider.MediaStore$MediaColumns')

sys.stdout.write("main.kv")
sys.stdout.flush()
Builder.load_file('main.kv')
