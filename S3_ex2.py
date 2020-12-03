import os


def ex2():

    # Mosaico
    os.system('ffmpeg \
            -i 480p_VP8.webm \
            -i 480p_VP9.webm \
            -i 480p_h265.mp4 \
            -i 480p_AV1.mkv \
            -filter_complex " \
            [0:v] setpts=PTS-STARTPTS, scale=qvga [a0]; \
            [1:v] setpts=PTS-STARTPTS, scale=qvga [a1]; \
            [2:v] setpts=PTS-STARTPTS, scale=qvga [a2]; \
            [3:v] setpts=PTS-STARTPTS, scale=qvga [a3]; \
            [a0][a1][a2][a3]xstack=inputs=4:layout=0_0|0_h0|w0_0|w0_h0[out] \
            " \
            -map "[out]" \
            -c:v libx264 -t 30 -f matroska all4.mkv')  # 4in1.mp4


if __name__ == "__main__":

    ex2()
