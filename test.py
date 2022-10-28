
from yt_dlp import YoutubeDL
import ffmpeg


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')
    print('status', d['status'])
    print('filename', d['filename'])
    print('total_bytes', d['total_bytes'])
    print('downloaded_bytes', d['downloaded_bytes'])

#video
ydl_opts = {
    'format': "bv*[vcodec~='^((he|a)vc|h26[45])'][height=1080]+bestaudio[ext=m4a]",
    'outtmpl': 'download/%(title)s.%(ext)s',
    'merge-output-format':"mp4",
    'progress_hooks': [my_hook],

}

#audio
# ydl_opts = {
#     'format': 'm4a/bestaudio/best',
#     # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
#     'postprocessors': [{  # Extract audio using ffmpeg
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'wav',
#     }]
# }



with YoutubeDL(ydl_opts) as ydl:
    #try:
    ydl.download(['https://www.youtube.com/watch?v=M2cckDmNLMI'])
    #except:
    print("ダウンロード失敗><\n他の解像度を選んでね")


 
# # 入力
# stream = ffmpeg.input("ゴーストレストラン ⧸ 初音ミク [j8MxmBc0TMo].webm")
 
# # 出力
# stream = ffmpeg.output(stream, "test.mp4")
 
# # 実行
# ffmpeg.run(stream)