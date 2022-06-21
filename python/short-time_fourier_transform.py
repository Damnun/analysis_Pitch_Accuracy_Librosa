import matplotlib.pyplot as plt
import librosa
import numpy as np

y, sr = librosa.load('Algorithm/akmu.wav')
D = np.abs(librosa.stft(y, n_fft=2048, hop_length=512))
print(D.shape)

plt.figure(figsize=(16,6))
plt.plot(D)
plt.show()