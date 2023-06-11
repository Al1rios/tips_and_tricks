
from pytube import YouTube

yt_video = YouTube("https://www.youtube.com/watch?v=3ckZYGYvcVo")

v_file = yt_video.streams.filter(file_extension="mp4").get_by_resolution("360p")

v_file.download(".")

