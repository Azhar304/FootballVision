import time
import cv2
import torch
from script import model

# 
if torch.cuda.is_available():
    model.to('cuda')
    print("Running on GPU")
else:
    print("GPU not available — running on CPU")

input_video = "C:/Users/dall/Desktop/football_tracking/videos/1_720p.mkv"
output_video = "C:/Users/dall/Desktop/football_tracking/videos/OUTPUT_1_720p.mkv"

cap = cv2.VideoCapture(input_video)
fps = cap.get(cv2.CAP_PROP_FPS)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = 0

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# FPS calculation
prev_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # ---- Inference on GPU ----
    results = model(frame)[0]
    annotated_frame = results.plot()

    # ---- FPS calculation ----
    curr_time = time.time()
    instantaneous_fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    
    cv2.putText(annotated_frame, f"FPS: {instantaneous_fps:.1f}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Football Detection", annotated_frame)
    writer.write(annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
print("Finished processing, saved as", output_video)
