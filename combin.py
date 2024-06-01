from pydub import AudioSegment
import os

def combine_audio(path):
    #변수에 따른 값들 가져오기
    files = os.listdir(path)
    sound_list = []

    for i in files:
        sound_list.append(AudioSegment.from_file(path + '\\' + i))

    x = sound_list[0]
    for i in range(1,len(sound_list)):
        x = x + sound_list[i]
    x.export('res.mp3' , format="mp3")

#여기는 파일의 경로는
path = r'C:\Users\user\PycharmProjects\hacaton\cut_file'

combine_audio(path)


