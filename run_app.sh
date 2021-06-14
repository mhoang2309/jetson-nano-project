#!/bin/bash
python3 trt_yolo_mjpeg.py --usb 0 --copy_frame -m yolov4-custom_final -c 5 &
node ./web_server/app &