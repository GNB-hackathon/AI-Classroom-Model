# 모듈 설치: !pip install moviepy
from moviepy.editor import VideoFileClip, AudioFileClip

def replace_audio_in_video(video_file_path, new_audio_file_path, output_file_path, volume=1.0):
    # 비디오 파일과 새 오디오 파일 불러오기
    video = VideoFileClip(video_file_path)
    new_audio = AudioFileClip(new_audio_file_path)
    # 볼륨 조정(1.0이 기존 볼륨 크기 기준)
    new_audio = new_audio.volumex(volume)
    # 비디오의 오디오 교체
    video = video.set_audio(new_audio)
    # 결과 비디오 파일 저장(코덱: mp4 기준)
    video.write_videofile(output_file_path, codec='libx264', audio_codec='aac')


original_video_file = r"C:\Users\user\PycharmProjects\hacaton\video_sample.mp4"
new_audio_file = r"C:\Users\user\PycharmProjects\hacaton\jungwoosung.mp3"  # wav 등 다른 포맷도 가능
output_video_file = "final_output_file.mp4"

replace_audio_in_video(original_video_file, new_audio_file, output_video_file)