import requests
from datetime import *

url = "https://image.baidu.com/search/index"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
}

for pn in range(1,91):
    params = {
        "tn": "resultjson_com",
        "logid": "8964265920770431646",
        "ipn": "rj",
        "ct": "201326592",
        "is": "",
        "fp": "result",
        "fr": "",
        "word": "二次元",
        "queryWord": "二次元",
        "cl": "",
        "lm": "",
        "ie": "utf-8",
        "oe": "utf-8",
        "adpicid": "",
        "st": "",
        "z": "",
        "ic": "",
        "hd": "",
        "latest": "",
        "copyright": "",
        "s": "",
        "se": "",
        "tab": "",
        "width": "",
        "height": "",
        "face": "",
        "istype": "",
        "qc": "",
        "nc": "",
        "expermode": "",
        "nojc": "",
        "isAsync": "",
        "pn": pn,
        "rn": "30",
        "gsm": "5a",
        "1639279803962": ""
    }
    res = requests.get(url, headers=headers, params=params).json()
    list = res["data"]
    imgList = []
    for mp in list:
        print(mp)
        if("thumbURL" in mp):
            imgList.append(mp["thumbURL"])

    # 下载图片
    for i in imgList:
        name = datetime.now()
        name = str(name.year) + str(name.month) + str(name.day) + str(name.hour) + str(name.minute) + str(name.second)
        with open(f"img\\{name}.jpg", mode="wb") as f:
            f.write(requests.get(i, headers=headers).content)







