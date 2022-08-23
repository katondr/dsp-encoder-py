dtmf_1 = [697, 770, 852, 941]
dtmf_2 = [1209, 1336, 1477]

keys = {
    '1': [dtmf_1[0], dtmf_2[0],
    '2': [dtmf_1[0], dtmf_2[1],
    '3': [dtmf_1[0], dtmf_2[0],
    '4': [dtmf_1[0], dtmf_2[0],
    '5': [dtmf_1[0], dtmf_2[0],
    '6': [dtmf_1[0], dtmf_2[0],
    '7': [dtmf_1[0], dtmf_2[0],
    '8': [dtmf_1[0], dtmf_2[0],
    '9': [dtmf_1[0], dtmf_2[0],
    '*': [dtmf_1[0], dtmf_2[0],
    '0': [dtmf_1[0], dtmf_2[0],
    '#': [dtmf_1[0], dtmf_2[0],
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
