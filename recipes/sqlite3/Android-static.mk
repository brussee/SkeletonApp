LOCAL_PATH := $(call my-dir)/..

include $(CLEAR_VARS)

LOCAL_MODULE    := sqlite3
LOCAL_SRC_FILES := sqlite3.c
LOCAL_CFLAGS    := -DSQLITE_ENABLE_FTS4

include $(BUILD_STATIC_LIBRARY)
