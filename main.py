from ultralytics import YOLO 

model = YOLO('yolov8m.pt')

results = model('demo.mp4', show = True, save = True)
