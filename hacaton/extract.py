# 모듈 설치: !pip install moviepy
from moviepy.editor import VideoFileClip
def extract_audio_from_video(video_file_path, audio_file_path):
    # mp4 등 비디오 파일 불러오기
    video = VideoFileClip(video_file_path)
    # 오디오를 추출하여 mp3 파일로 저장
    video.audio.write_audiofile(audio_file_path)


#이 함수는 현재 파일 경로, 바꾸고 싶은 video이름, 바꿀 audio 이름 이 3가지만 입력하면됨
def extract_audio_from_video_by_name(path,video_name,audio_name):
    video_file = path + '\\' + video_name  # 변환하고 싶은 비디오 파일의 경로
    audio_file = path + '\\' + audio_name  # 저장할 오디오 파일의 경로, 이름 지정
    extract_audio_from_video(video_file, audio_file)

# 여기서는 한번 test로 시험해보는 거
path = r'C:\Users\user\PycharmProjects\hacaton'
video_name = "video_sample.mp4"
audio_name = "audio_sample.mp3"

extract_audio_from_video_by_name(path,video_name,audio_name)

