from moviepy.editor import *
from os import walk
import argparse,sys

parser = argparse.ArgumentParser()
#
# parser.add_argument("--path", help="path too directory with videos")
parser.add_argument("--rotate", help="rotate this video? default = true", default=True)
#
args = parser.parse_args()
#
path = input("drag a file here \n")


for (dirpath, dirnames, filenames) in walk(path):
    if(len(filenames) > 0):
        print(dirpath)
        name = dirpath.split("\\")[len(dirpath.split("\\")) - 1] + ".gif"
        print(name)
        videoClip = VideoFileClip(dirpath + "/" + filenames[0])
        if(args.rotate):
            videoClip = videoClip.rotate(90)

        videoClip.write_gif(filename=name)






