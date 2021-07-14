# very-serious-video-project
This is an extremely messy Python script I wrote to render a video in an unusual way.

[Video Link](https://www.youtube.com/watch?v=K1dLxK4mfVk)

## How
Although the process I used could be applied to any video, I hardcoded some values to save time and get the exact results I wanted.
It shouldn't be too hard to adjust the values, or even genericize the entire program if you're feeling bold.
First, I downsized the video to 40x30 and split the individual frames into images with ffmpeg.
These steps could easily be integrated into the script, even if via a wrapper.
Again, I was definitely making this more with the end goal in mind than for the sake of the process.
I processed each frame in Python, doing calculations like color analysis (although that's really stretching the term, considering the "algorithm" I came up with).
Using PyGame, I rendered the pixels as color-matched sprites in varying stages of the animation to create a wave effect.
Finally, as this was all going through PyGame instead of a proper video editor, the only way to output this to a video was through screen recording.
I probably could have come up with a better method, like saving all the rendered frames as images and stitching them together, but this was the quick and dirty solution.
One consequnces of this strategy was that forcing the program to process in real-time cost frames, resulting in a noticeable freeze at one point in the video.

## Why
I ask myself that question too.
