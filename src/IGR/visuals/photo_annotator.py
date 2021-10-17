from typing import List
import matplotlib.pyplot as plt
import json
from pathlib import Path
import re
import cv2

__CURR_DIR__ = Path(__file__).resolve().parent

IMGS = __CURR_DIR__ / "long_test"
OUT = __CURR_DIR__ / "long_test_annotated"

def get_frames(frames_path: Path = IMGS):
    def sorter(item):
        # return str(item.name).split(".")[0]
        return int(re.sub('\D', '', item.name))

    format = '*.png'

    for filename in sorted(frames_path.glob(format), key=sorter):
        filename2 = str(filename)
        img = cv2.imread(filename2)

        yield filename.name, img

def annotate_frames(frames_path: Path = IMGS, out_path: Path = OUT):
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # org
    org = (500, 50)

    # fontScale
    fontScale = 1

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2

    frames = get_frames(frames_path)
    for name, frame in frames:
        image = cv2.putText(frame, f"Epoch: {name.replace('.png', '')}", org, font, fontScale, color, thickness, cv2.LINE_AA)
        cv2.imwrite(str(out_path / name),  image)

if __name__ == "__main__":
    annotate_frames()