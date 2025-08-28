text = input("Nhập đoạn văn bản: ") #Write a Python program that counts the number of times characters appear in a text paragraph.
char_count = {}
for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1
for k, v in char_count.items():
    print(k, "xuất hiện", v, "lần")