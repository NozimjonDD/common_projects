import os

import requests
from django.http import HttpResponseForbidden
from django.shortcuts import render

from video_player.models import LessonVideo

'''
HTML template for video player
'''


def secure_video_view(request, just_slug):
    slug = request.headers.get('Referer').split('/')[-3]
    model = request.headers.get('Referer').split('/')[-2]
    name = 'test'
    if model == 'video':
        video = LessonVideo.objects.get(slug=slug)
        name = video.video.name

    #  Method-1 with local file path
    # if not request.user.is_authenticated:
    #     return HttpResponseForbidden("You are not allowed to access this video.")
    # path = os.path.join(f"media/" f"{name}")
    # return FileResponse(open(path, 'rb'), content_type='video/mp4')


    #  Method-2 with file link(https://.........)
    # url = "https://api.gossipgirl.uz/media/business/specialist/video_intro/5659273-hd_1080_1920_30fps.mp4"
    local_filename = 'new_23.mp4'

    #  If header needed
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        # 'Referer': 'https://www.terabox.com',
        # 'Accept': 'application/json, text/plain, */*',
        # 'Cookie': 'your_cookie_here'  # TeraBox cookies-ni qo‘lda olish kerak
    }

    # response = requests.get(url, stream=True)
    # response.raise_for_status()  # Raise an exception for HTTP errors

    # with open(local_filename, 'wb') as f:
    #     for chunk in response.iter_content(chunk_size=8192):
    #         f.write(chunk)
    #
    # print(f"File downloaded successfully to {local_filename}")
    #
    # return FileResponse(open(local_filename, 'rb'), content_type='video/mp4')

    #  Method-3 Stream with file link(https://.........) without save file local storage
    from django.http import StreamingHttpResponse
    #  url = domain.com/media/path/file.pm4
    url = "https://vod3.cf.dmcdn.net/sec2(iXb5uzujxtrxAeFHfOhj9OWheMs2JhRlnXE-V1G9NmCAA1c6iizTl_SfMxvgfXrqVETBHHCW9QXsQLBJDeoHBt6Z7OHHVDqdcc2jyqL9kdQKpw347qTSvuCU9ARDheTz-P0xI6snlg-irSF02rsAHywQsZTELZiaoujj_D2uIzZryM7_4j16P96g9vmdX8F1jMXnxLFVD_a7-TdMI_Daow)/download/230/116/582611032_mp4_h264_aac_hq.mp4"
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an exception for HTTP errors
    def stream_video():
        for chunk in response.iter_content(chunk_size=8192):
            yield chunk

    return StreamingHttpResponse(stream_video(), content_type='video/mp4')
