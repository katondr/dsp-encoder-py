import math
import numpy as np
import scipy.fftpack as fft
import wave
import sounddevice as sd

pi = math.pi

dtmf_1 = [697, 770, 852, 941]
dtmf_2 = [1209, 1336, 1477]

keys = {
    '1': [dtmf_1[0], dtmf_2[0]],
    '2': [dtmf_1[0], dtmf_2[1]],
    '3': [dtmf_1[0], dtmf_2[0]],
    '4': [dtmf_1[0], dtmf_2[0]],
    '5': [dtmf_1[0], dtmf_2[0]],
    '6': [dtmf_1[0], dtmf_2[0]],
    '7': [dtmf_1[0], dtmf_2[0]],
    '8': [dtmf_1[0], dtmf_2[0]],
    '9': [dtmf_1[0], dtmf_2[0]],
    '*': [dtmf_1[0], dtmf_2[0]],
    '0': [dtmf_1[0], dtmf_2[0]],
    '#': [dtmf_1[0], dtmf_2[0]],
        }

def dsp_key2tones(key, tone_len, fs):
    f = keys[str(key)]
    f_1 = f[0]
    f_2 = f[1]
    w_1 = (2 * pi * f_1)/fs
    w_2 = (2 * pi * f_2)/fs
    n = np.array(range(0, math.floor((tone_len * fs)-1)))
    tone_1 = np.sin(w_1 * n)
    tone_2 = np.sin(w_2 * n)
    tones = 0.5 * (tone_1 + tone_2)
    return tones

def dsp_encode_dtmf(keys_input, tone_len, zero_len, fs):
    num_keys = len(keys_input)
    tone_len_n = math.floor(tone_len*fs)
    zero_len_n = math.floor(zero_len*fs)
    key_pause = np.zeros(zero_len_n)
    for i in range(0, len(keys_input)):
        if i == 0:
            dtmf_signal = dsp_key2tones(keys_input[i], tone_len, fs)
            dtmf_signal = np.append(dtmf_signal, key_pause)
        else:
            dtmf_signal = np.append(dtmf_signal, dsp_key2tones(keys_input[i], tone_len, fs))
            dtmf_signal = np.append(dtmf_signal, key_pause)
    return dtmf_signal

tone_len = 3
zero_len = 0.1
fs = 44100
    
#generate the DTMF signal
key_input = '01205551234'
#dtmf_signal = dsp_encode_dtmf(keys, tone_len, zero_len, fs)
#play the DTMF signal
dtmf_signal = dsp_encode_dtmf(key_input, tone_len, zero_len, fs)
#sd.OutputStream(channels=1, callback=dtmf_signal, samplerate=fs)
print(dtmf_signal)
obj = wave.open('sound.wav','w')
obj.setnchannels(1)
obj.setsampwidth(2)
obj.setframerate(fs)
#obj.writeframesraw(dtmf_signal)
obj.close()
sd.play(dtmf_signal, fs)
#ipd.Audio(dtmf_signal, rate=fs)

"""
time = np.array(range(0, len(dtmf_signal)))
times = time*(tone_len + zero_len)
signal = fft.fft(dtmf_signal)
print(signal)
plt.plot(times[0:(len(times)//12)], signal[0:(len(signal)//12)])
plt.show()
"""
