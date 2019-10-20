from video_editing import VideoEditing


def main():
    """
    Entrypoint for the code of project 04 Group 08 MO446/2sem2019
    """
    
    # Create the Video Editing object
    ve = VideoEditing()

    # Remove people from video
    ve.remove_people("input/i-0.mp4", "output/o-0", operation=1, max_frames=-1, print_frames=False)


main()
