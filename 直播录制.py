# coding: utf-8

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdklive.v1.region.live_region import LiveRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdklive.v1 import *
import os
import subprocess
###from https://console.huaweicloud.com/apiexplorer/#/openapi/Live/debug?api=ListLiveStreamsOnline
if __name__ == "__main__":
    ak = "****"
    sk = "********"

    credentials = BasicCredentials(ak, sk)
    client = LiveClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(LiveRegion.value_of("cn-north-4")) \
        .build()
    try:
        request = ListLiveStreamsOnlineRequest()
        request.publish_domain = "live-push.live.com"
        request.limit = 10
        response = client.list_live_streams_online(request)
        streams = response.streams
        stream_list = []
        for i in streams:
            stream_list.append(i.stream)
            stream = i.stream
            start_time = i.start_time[0:10]
            print(stream,start_time)
            process = subprocess.Popen(['ffmpeg', '-i', 'rtmp://live-play.live.com/live/'+stream, '-s', '270X480', '-c:v', 'libx264', '-b:v', '0.25M', '-preset', 'medium', '-c:a', 'aac', start_time+'-'+stream+'.mp4'], creationflags=subprocess.CREATE_NEW_CONSOLE)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
