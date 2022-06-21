import librosa
import scipy.signal as signal
import numpy as np

audio_sample, sampling_rate = librosa.load("akmu.wav", sr = None)

S = np.abs(librosa.stft(audio_sample, n_fft=1024, hop_length=512, win_length = 1024, window=signal.hann))
pitches, magnitudes = librosa.piptrack(S=S, sr=sampling_rate)

shape = np.shape(pitches)
nb_samples = shape[0]
nb_windows = shape[1]

# FFT 결과를 plot
import matplotlib.pyplot as plt
import librosa.display

#멜 스펙토그램
D = librosa.feature.melspectrogram(S=S, sr=sampling_rate)
D_dB = librosa.power_to_db(D, ref=np.max)

plt.figure(figsize=(12, 4))
librosa.display.specshow(D_dB)
plt.ylabel('mel')
plt.xlabel('time')
plt.title('Mel-frequency spectrogram')
plt.colorbar()
plt.tight_layout()
plt.show()