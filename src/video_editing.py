import cv2
import numpy as np
from math import sqrt


class VideoEditing:
    """
    A class used to real time video editing

    Methods
    -------
    execute(input_path, output_path, operation)
        Execute the real time video editing
    """

    def __init__(self):
        pass

    def remove_people(self, input_path, output_path, operation=2, max_frames=-1, print_frames=False):
        """
        It removes people from video

        Keyword arguments:
        input_path -- the input video path
        output_path -- the output video path
        operation -- operation to apply on the frame
        max_frames -- maximum number of frames to process
        print_frames -- flag to print the current frame
        """       
        
        index = 1
        
        # Open the video
        video_capture = cv2.VideoCapture(input_path)

        # Read the first frame
        success, current_frame = video_capture.read()
    
        # For each frame
        while success:
    
            print(f"Processing Frame {index}")
            
            if operation == 0:
                pass

            elif operation == 1:
                pass
            
            # Save the current frame as an image
            if print_frames:
                cv2.imwrite(f"output/frame-{index}"+suffix+".jpg", output_frame)
                            
            index += 1

            if max_frames > 0 and index > max_frames:
                break
            
            # Read the next frame
            success, current_frame = video_capture.read()
        
