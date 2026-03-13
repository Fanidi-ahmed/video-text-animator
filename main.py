from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np

app = FastAPI()

@app.post("/animate-text/")
async def animate_text(file: UploadFile = File(...), text: str = "Sample Text"):
    # Load video file
    with open(file.filename, "wb") as buffer:
        buffer.write(await file.read())
    video = cv2.VideoCapture(file.filename)

    # Check if video opened successfully
    if not video.isOpened():
        return {"error": "Could not open video"}

    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (frame_width, frame_height))

    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Add text to frame
        cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        out.write(frame)

    video.release()
    out.release()
    return {"message": "Video generated successfully!", "video_path": "output.avi"}