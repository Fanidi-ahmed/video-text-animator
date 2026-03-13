import cv2
import numpy as np

class VideoGenerator:
    def __init__(self, output_filename, width=640, height=480, fps=30):
        self.output_filename = output_filename
        self.width = width
        self.height = height
        self.fps = fps
        self.video_writer = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))

    def add_frame(self, frame):
        # Assuming frame is a numpy array
        self.video_writer.write(frame)

    def generate_animation(self, text, duration):
        # A simple animation logic that generates a video frame with the text
        for i in range(int(self.fps * duration)):
            frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
            text_position = (50, 50 + i % self.height)
            cv2.putText(frame, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            self.add_frame(frame)

    def release(self):
        self.video_writer.release()

# Example usage:
# generator = VideoGenerator('output.avi')
# generator.generate_animation('Hello, World!', 5)
# generator.release()