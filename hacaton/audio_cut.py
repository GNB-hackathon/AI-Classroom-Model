from pydub import AudioSegment

def audio_cut_by_name(path, audio_name) :
    sound = AudioSegment.from_file(path + '\\' + audio_name)

    d_time = 1000; #1초가 1000이 여서
    d_minute = 60 * d_time # 1분 설정

    #여기서 부터는 10분단위로 오디오 짜르기
    total_len = len(sound)
    present_len = 0
    sound_list = []
    plus_number = d_minute * 10

    while present_len < total_len:
        if present_len + plus_number > total_len:
            plus_number = present_len + plus_number - total_len
        sound_list.append(sound[present_len: present_len + plus_number])
        present_len = present_len + plus_number + 1

    #파이썬 추출한 파일들을 저장하기
    store_path = path + '\\' + 'cut_file' # 이때 이자식은 파일들을 특정한 파일에 저장하는거인데, 나중에 서버에서 결정해야함
    for i, s in enumerate(sound_list, start=0):
        file_name = store_path + '\\' +'test' + str(i) + ".mp3"
        s.export(file_name, format="mp3")

#path
path = r'C:\Users\user\PycharmProjects\hacaton'
audio_name = 'audio_sample.mp3'

audio_cut_by_name(path, audio_name)
