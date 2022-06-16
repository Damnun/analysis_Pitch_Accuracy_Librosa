import librosa
import scipy.signal as signal
import numpy as np
import pydub
from pydub import AudioSegment

import os
# 2stems = vocals and accompaniment
# 4stems = vocals, drums, bass, and other
# 5stems = vocals, drums, bass, piano, and other
def file_init_():
    stems = str(input('stems 선택 : 2, 4, 5 >>>'))
    path = str(input(r'파일이 있는 경로를 정해주세요. >>>'))
    os.chdir(path)
    file_name = str(input('음악 파일의 이름을 적어주세요.(.mp3 또는 .wav) >>>'))
    nsfile_name = file_name.replace(' ', '_')

# file exchange
    if os.path.splitext(nsfile_name)[1] == '.mp3':
        try:
            src = os.path.splitext(nsfile_name)[0] + ".mp3"
            dst = os.path.splitext(nsfile_name)[0] + ".wav"

        # convert wav to mp3
            sound = AudioSegment.from_mp3(src)
            sound.export(dst, format="wav")
        except FileNotFoundError:
            pass
    else:
        pass
    print('기다려주세요.')
    spl = r'spleeter separate -p spleeter:' + \
        str(stems)+r'stems -o output '+nsfile_name
# 'spleeter separate -p spleeter:{option}stems -o output my_song.wav'
    os.system(spl)