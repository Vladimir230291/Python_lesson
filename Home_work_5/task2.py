# Реализуйте RLE алгоритм:
# реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.\

def rle_encode(data):
    encoding = ""
    prev_char = ""
    count = 1
    if not data:
        return ""
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


with open("Decode_Text.txt", "r") as f:
    decode = f.read()
print(decode)

encode = rle_encode(decode)

with open("Encode.txt", "w") as fh:
    fh.write(encode)
    print(encode)

