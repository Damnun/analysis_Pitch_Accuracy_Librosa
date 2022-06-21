import librosa
import scipy.signal as signal
import numpy as np


audio_sample, sampling_rate = librosa.load("akmu.wav", sr = None)

S = np.abs(librosa.stft(audio_sample, n_fft=1024, hop_length=512, win_length = 1024, window=signal.hann))
pitches, magnitudes = librosa.piptrack(S=S, sr=sampling_rate)

shape = np.shape(pitches)
nb_samples = shape[0]
nb_windows = shape[1]

for i in range(0, nb_windows):
    index = magnitudes[:, i].argmax()
    pitch = pitches[index, i]
    print(pitch)

# FFT 결과를 plot
import matplotlib.pyplot as plt
import librosa.display

D = librosa.feature.melspectrogram(S=S, sr=sampling_rate)
D_dB = librosa.power_to_db(D, ref=np.max)

#MFCC
mfcc = librosa.feature.mfcc(S=D_dB, n_mfcc=15)

delta2_mfcc = librosa.feature.delta(mfcc, order=2)

plt.figure(figsize=(12, 4))
librosa.display.specshow(delta2_mfcc)
plt.ylabel('MFCC coeffs')
plt.xlabel('Time')
plt.title('MFCC spectogram')
plt.colorbar()
plt.tight_layout()
plt.show()