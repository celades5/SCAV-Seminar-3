# SCAV-Seminar-3
Seminar 3 for SCAV subject at UPF

**Teacher:** Javi Fernandez

Tis readme intents to explain the third semianr in the SCAV subject for the video part.

This repository consists in:

**Pdf:** Pdf file containing screenshots of exercises with results. Plus a link in the header to the *git repository*.

**Python exercises:** Containing the code for all the different exercises needed to compute this lab. Run *ex4* containing the menu of all the lab for a full experience. Run each exercise independently if desired.

**ex1:** We are going to carry out the procedure of transforming the videos to VP8, VP9, ​​h265 and AV1 with a single video, in our case it will be 480p called *480p_res.mp4*. To do the others it would be the same procedure that we implmented for the first convertion. To transform it we will follow the indications of *https://trac.ffmpeg.org.*

For the convertion to specific types, we have followed this guides from the ffmpeg website.

-   **VP8** &rarr; *https://trac.ffmpeg.org/wiki/Encode/VP8*

-   **VP9** &rarr; *https://trac.ffmpeg.org/wiki/Encode/VP9*

-   **VPH.265** &rarr; *https://trac.ffmpeg.org/wiki/Encode/H.265*

-   **AV1** &rarr; *https://trac.ffmpeg.org/wiki/Encode/AV1*

As we can see in the **pdf file**, the video have been transformed into the outputs specified.

**ex2** To make the mosaic, we execute *ex2* python script, with the names that we have given to the new videos.
Once we have execute that we can see the a new video with the 4 codecs altogether. Although it is asked to seek for differences, I can not quite see significant differences between them, excep for a little more distortion in the VP8 compared to the others.
However, we can state the following:

-   In terms of bit rate, **VP8** and **VP9** consume considerably more than **h265** and **AV1**.

-   Regarding the encoding time, **AV1** is the one that has taken the longest, unlike the **h265** which is the fastest.

- **NOTE:** This exercise has been done twice, one with an outuput *.mkv* and another with outuput *.mp4*

**ex3:** This is the streaming part. With the first line in the we would create our live streaming from bbb.mp4 to the corresponding ip. Using *ffplay* and *VLC* app, the live video should be streamed locally. As we can see with the pictures in the *pdf file*, all has been done correctly.

-   **NOTE:** Due to low computation and processing of my pc, we were not able to see the actuall streaming, however, we can see how the packages are being sent and recieved correctly. If there would be any loss of packages, the quality of the frames on the video would decrease for a period of time.
