


from pytube import YouTube

# Where to save
SAVE_PATH = "E:/"  # to_do

# Links of the videos to be downloaded
links = ["https://youtu.be/3SyUOSebG7E"]

for link in links:
    try:
        # Object creation using YouTube
        # which was imported in the beginning
        print("start")
        yt = YouTube("https://youtu.be/LLT8mqS1IB0")
        print(dir(yt))
        d_video=yt.streams()
        print(d_video)
        # mp4_streams = yt.streams.filter(file_extension='mp4')
        
        d=d_video[-1]
        x=d.download(output_path=SAVE_PATH)
        print(x)
        print('downloaded')
    except:
        print("error downloading")

    # Get all streams and filter for mp4 files
        

    # Get the video with the highest resolutio
"""

"""