# spectral centroid : 소리의 무게 중심
# 주파수 표현시 주파수의 가중 평균을 계산. sklearn을 통해 0~1사이로 추출
import numpy as np
import matplotlib.pyplot as plt
import librosa.feature
import librosa.display
import sklearn

y, sr = librosa.load("Algorithm/akmu.wav")
spectral_centroids = librosa.feature.spectral_centroid(y, sr=sr)[0]

frames = range(len(spectral_centroids))
t = librosa.frames_to_time(frames)


def normalize(x, axis=0):
    return sklearn.preprocessing.minmax_scale(x, axis=axis)


plt.figure(figsize=(16,6))
librosa.display.waveshow(y, sr=sr, alpha=0.5, color='b')
plt.plot(t, normalize(spectral_centroids), color='r')
plt.show()
