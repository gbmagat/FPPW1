#!/bin/bash
yolo detect train data=data/site-construction-safety/data.yaml model=yolov8n.pt epochs=10 imgsz=640