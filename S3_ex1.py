import os


def ex1():

    # Ex 1 Seminar 3

    # VP8
    os.system("ffmpeg -i bbb_480.mp4 -c:v libvpx -b:v 1258k -c:a libvorbis \
            480p_V8.webm")

    # VP9
    os.system("ffmpeg -i bbb_480.mp4 -c:v libvpx-vp9 -b:v 1258k 480p_VP9.webm")

    # H265
    os.system("ffmpeg -i bbb_480.mp4 -c:v libx265 -crf 28 -c:a aac -b:a \
            1258k 480p_h265.mp4")
    # AV1
    os.system("ffmpeg -i bbb_480.mp4 -c:v libaom-av1 -b:v 1258k -strict \
            experimental 480p_AV1.mkv")


if __name__ == "__main__":

    ex1()
