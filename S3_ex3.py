import os


def ex3():

    # Streaming part
    os.sytem("ffmpeg -re -i messi1.mp4 -an -c:v copy -f \
            mpegts udp://@224.2.2.2:2222")

    # Command line to store it as well
    os.system("ffmpeg -i udp://@224.2.2.2:2222 -map 0:0 -c copy \
            messi_stream.mp4")


if __name__ == "__main__":

    ex3()
