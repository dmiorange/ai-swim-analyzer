import cv2

def get_video_info(video_path):
    """Return total frames, fps, and duration of video."""
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps if fps > 0 else 0
    cap.release()

    return {
        "fps": fps,
        "total_frames": total_frames,
        "duration": duration
    }

def frame_to_seconds(frame_number, fps):
    """Convert frame index to time (seconds)."""
    return frame_number / fps

def seconds_to_frame(seconds, fps):
    """Convert time (seconds) to frame index."""
    return int(seconds * fps)
