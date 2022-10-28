import streamlit as st
from yt_dlp import YoutubeDL
from pathlib import Path

st.title("youtubeをダウンロードするアプリ")
st.markdown("""---""")
st.header("ダウンロード")

DL_URL = st.text_input("URLを入力")
# with st.expander('解像度の設定'):
#     res = st.selectbox(
#         '解像度を選択',
#         (2160, 1440, 1080, 720, 480, 360, 240, 144),
#         index=2)
    

# with YoutubeDL(ydl_opts) as ydl:
#     ydl.download([''])
#status: "downloading", "error", "finished"

def my_hook(d):
    if d['status'] == 'downloading':
        progress.progress(d['downloaded_bytes']/d['total_bytes'])
    print('status', d['status'])
    print('filename', d['filename'])
    print('total_bytes', d['total_bytes'])
    print('downloaded_bytes', d['downloaded_bytes'])
    # if d['status'] == 'finished':
    #     st.progress(1.0)


ydl_opts = {
    'format': "bv*[vcodec~='^((he|a)vc|h26[45])'][height=1080]+bestaudio[ext=m4a]",
    'outtmpl': 'download/%(title)s.%(ext)s',
    'merge-output-format':"mp4",
    'progress_hooks': [my_hook],

}



if st.button("実行"):
    progress = st.progress(0)
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([DL_URL])


st.markdown("""---""")
st.header("履歴")


for file in Path('download').iterdir():
    if not file.name.startswith('.'):
        st.subheader(file.name)
        with open(file, "rb") as file:
            btn2 = st.download_button(
                    label="ダウンロード",
                    data=file,
                    file_name=file.name,
                )



# with col1:
#     st.text("A cat")

# with col2:
#     with open("download/米津玄師 Kenshi Yonezu - KICKBACK.mp4", "rb") as file:
#         btn = st.download_button(
#                 label="Download image",
#                 data=file,
#                 file_name="flower.mp4",
#             )

