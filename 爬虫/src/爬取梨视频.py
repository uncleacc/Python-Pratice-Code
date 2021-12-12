import requests
from requests import *

URL = "https://www.pearvideo.com/video_1747603"
conId = URL.split("_")[1]
VideoStatusUrl = "https://www.pearvideo.com/videoStatus.jsp?contId=1747603&mrd=0.7331532127351621"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
    # 防盗链
    "Referer": URL
}
# 返回一个字典
dict = requests.get(VideoStatusUrl, headers=headers).json()
realUrl = dict["videoInfo"]["videos"]["srcUrl"]
systemTime = dict["systemTime"]
realUrl = realUrl.replace(systemTime, f"cont-{conId}")
# 保存视频
with open("video.mp3", mode="wb") as f:
    f.write(requests.get(realUrl, headers=headers).content)