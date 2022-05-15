# 신호처리적으로 pitch를 추출하는 2가지 방법
# 1. autocorrelation을 이용하여 peak or max 값을 찾는다.
# 2. FFT를 이용하여 magnitude의 peak or max 값을 찾는다.
# 정확도를 높이기 위해 pitch doubling이나 신호의 주기성, 주파수 범위 한정, 신호의 역치값 등을 고려한다.
# librosa는 wav, flac 확장자는 지원하나 mp3는 지원하지 않음. -> pydub, ffmpeg 패키치 설치

import librosa
import scipy.signal as signal
import numpy as np
import pydub
from pydub import AudioSegment

# files
src = "musicfile/start(gaho).mp3"
dst = "musicfile/start(gaho)ver3.wav"

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

audio_sample, sampling_rate = librosa.load("musicfile/start(gaho)ver3.wav", sr = None)

S = np.abs(librosa.stft(audio_sample, n_fft=1024, hop_length=512, win_length = 1024, window=signal.hann))
pitches, magnitudes = librosa.piptrack(S=S, sr=sampling_rate)

shape = np.shape(pitches)
nb_samples = shape[0]
nb_windows = shape[1]

for i in range(0, nb_windows):
    index = magnitudes[:,i].argmax()
    pitch = pitches[index,i]
    print(pitch)

# FFT 결과를 plot
import matplotlib.pyplot as plt
import librosa.display

#normalize_function
min_level_db = -100
def _normalize(S):
    return np.clip((S-min_level_db)/(-min_level_db), 0, 1)

mag_db = librosa.amplitude_to_db(S)
mag_n = _normalize(mag_db)
plt.subplot(311)
librosa.display.specshow(mag_n, y_axis='linear', x_axis='time', sr=sampling_rate)
plt.title('start(gaho) spectrogram')

t = np.linspace(0, 24000, mag_db.shape[0])
plt.subplot(313)
plt.plot(t, mag_db[:, 100].T)
plt.title('magnitude (dB)')
plt.show()
