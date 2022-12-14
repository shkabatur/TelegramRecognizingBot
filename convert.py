import os

def convert_x_to_wav(ipath, opath):
        os.system(f"ffmpeg -i {ipath} {opath}")


