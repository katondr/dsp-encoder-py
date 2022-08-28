import wave, struct, math, random
sampleRate = 44100 # hertz
duration = 2 # seconds
frequency = 440.0 # hertz
obj = wave.open('sound.wav','wb')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)
for i in range(99999):
    value = random.randint(-32767, 32767)
    data = struct.pack('<h', value)
    obj.writeframesraw(data)
obj.close()
