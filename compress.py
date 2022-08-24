
import numpy as np
import heapq
from PIL import Image as Pimage

def frequency_table(data):
    freq_table = np.array(np.unique(data, return_counts=True))
    freq_table = np.transpose(freq_table)
    return dict(freq_table)
def codebook_generator(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
    low = heapq.heappop(heap)
    high = heapq.heappop(heap)
    for value in low[1:]:
        value[1] = '0' + value[1]
        for value in high[1:]:
        value[1] = '1' +value[1]
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
    return dict(sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))
    def huffman_encoding(data, codebook):
        code = ''
        for i in data:
            code = code + codebook[i]
        return code
 
def huffman_decoding(encoded_data, codebook):
    data = encoded_data
    codebook = {value:key for key, value in codebook.items()}
    decoded_data = []
    c = 0
    l = 1
    while len(data) != 0:
        if data[c:l] in codebook:
            decoded_data.append(codebook[data[c:l]])
            data = data[l:]
            l = 1
        else:
            l = l + 1
    return decoded_data


  {

    # sample data & convertion to numpy array
sample = [114, 20, 114, 114, 110, 12, 117, 85, 114, 118, 114, 114, 114, 6,
    70, 71, 93, 102, 72, 114, 114, 53, 117, 74, 117, 114, 114, 14, 102, 14, 117, 114]
data = np.array(sample)
# create frequency table
frequency = frequency_table(data)
# generating codebook
codebook = codebook_generator(frequency)
# encoding data
encoded_data = huffman_encoding(data, codebook)  
# decoding data
decoded_data = huffman_decoding(encoded_data, codebook)
# verify function
print('Frequency Table')
print(frequency)
print('')
print('Codebook')
print(codebook)
print('')
print('Encoded Data')
print(encoded_data)
print('')
print('Is data converted back corectly?')
print(decoded_data == sample)
 
  },
 
def diff_encoding(data):
    encoded = []
    encoded.append(data[0])
    while len(data) != 1:
        if data[1] - encoded[0] > 0:
            encoded.append(257)
            encoded.append(data[1] - encoded[0])
        else:
            encoded.append(258)
            encoded.append(encoded[0] - data[1])
        data = data[1:]
    return encoded
def diff_decoding(code):
    decoded = []
    data = code
    while len(data) != 0:
        if data[0] == 257:
            decoded.append(code[0] + data[1])
            data = data[2:]
        elif data[0] == 258:
            decoded.append(code[0] - data[1])
            data = data[2:]
        else:
            decoded.append(data[0])
            data = data[1:]
    return data
 
 
def rl_encoding(data):
    rl_encoded = []
    while len(data) != 2:
        c = 0
        l = 1
        r = 1
        while data[c] == data[l]:
            l = l + 1
            r = r + 1
        if r > 3:
            rl_encoded.append(256)
            rl_encoded.append(data[c])
            rl_encoded.append(r)
        elif r <= 3:
            for i in data[c:l]:
                rl_encoded.append(i)
        data = data[l:]
    for i in data:
        rl_encoded.append(i)
    return rl_encoded

def rl_decoding(data):
    decoded = []
    while len(data) != 0:
        if data[0] == 256:
            for i in range(0, data[2]):
                decoded.append(data[1])
        else:
            decoded.append(data[0])
        data = data[1:]
    return decoded
sample = [114, 20, 114, 114, 110, 12, 117, 85, 114, 118, 114, 114, 114, 6, 70, 71, 93, 102, 72, 114, 114, 53, 117, 74, 117, 114, 114, 14, 102, 14, 117, 114]
data = np.array(sample)
# differential encoding
data_211 = diff_encoding(data)
# huffman encoding
frequency_table_211 = frequency_table(data_211)
codebook_21 = codebook_generator(frequency_table_211)
data_212 = huffman_encoding(data_211, codebook_21)

# differential encoding
data_231 = diff_encoding(data)
# run-length encoding
data_232 = rl_encoding(data_231)
# huffman encoding
frequency_23 = frequency_table(data_232)
codebook_23 = codebook_generator(frequency_23)
data_233 = huffman_encoding(data_232, codebook_23)
print(len(data_233))
print(len(encoded_data))

# Part 3: Image Coding"
# image
img = 'sample.png'
#img = 'Lhotse_Mountain_8-Bit_Grayscale.jpg'
# reading image / convert to numpy array
im = np.asarray(Pimage.open(img))
im = im.flatten()
# differential encoding
data_31 = diff_encoding(im)
# run-length encoding
data_32 = rl_encoding(data_31)
# huffman encoding
frequency_3 = frequency_table(data_32)
codebook_3 = codebook_generator(frequency_3)
data_3 = huffman_encoding(data_32, codebook_3)
#im.shape
len(data_3)
