import moviepy.editor as mp
import sys
import os

def show_clip(path):
    path = os.path.abspath(path)
    clip = mp.VideoFileClip(path).subclip()
    clip.preview()


if __name__ == '__main__':
    show_clip(sys.argv[1])
