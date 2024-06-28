import cv2
import os


def extract_frames(video_path, output_folder, current_fold, current_video):
    cap = cv2.VideoCapture(video_path)
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(frame_rate * 1.2)

    current_frame = 0
    while True:
        success, frame = cap.read()
        if not success:
            break
        if current_frame % frame_interval == 0:
            frame_filename = f"frame_{current_fold}_{current_video}_{current_frame}.jpg"
            frame_path = os.path.join(output_folder, frame_filename)
            print(frame_path)
            cv2.imwrite(frame_path, frame)
        current_frame += 1

    cap.release()



root = "ITMO-HSE-MLBD-LW-3"
output_folder = "extracted1"
dirs = os.listdir(root)

for fold in dirs:
    folder_path = os.path.join(root, fold)
    files = os.listdir(folder_path)

    for video in files:

        video_path = os.path.join(folder_path, video)
        extract_frames(video_path, output_folder,fold, video[:-4])
        