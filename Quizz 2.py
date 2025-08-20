# EX1:
text = "Hello World"
length = len(text)
print(f"Chuỗi: {text}")
print(f"Độ dài: {length}")
print()

# EX2:
text = "google.com"
count = {}
for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print(f"Chuỗi: {text}")
print(f"Đếm ký tự: {count}")
print()

# EX3:
text = "w3resource"
if len(text) < 2:
    result = ""
else:
    result = text[:2] + text[-2:]

print(f"Chuỗi: {text}")
print(f"Kết quả: {result}")

# EX4:
text = "restart"
first_char = text[0]
result = first_char + text[1:].replace(first_char,'$')
print(f"Chuỗi gốc: {text}")
print(f"Kết quả: {result}")
print()

# EX5:
str1 = "abc"
str2 = "xyz"

first_two_1 = str1[:2]
rest_1 = str1[2:]
first_two_2 = str2[:2]
rest_2 = str2[2:]
new_str1 = first_two_2 + rest_1
new_str2 = first_two_1 + rest_2
result = new_str1 + " " + new_str2

print(f"Chuỗi 1: {str1}")
print(f"Chuỗi 2: {str2}")
print(f"Kết quả: {result}")

# EX6:
text1 = "abc"
text2 = "string"

def add_ing_or_ly(text):
    if len(text) < 3:
        return text
    elif text.endswith("ing"):
        return text + "ly"
    else:
        return text + "ing"

result1 = add_ing_or_ly(text1)
result2 = add_ing_or_ly(text2)

print(f"'{text1}' -> '{result1}'")
print(f"'{text2}' -> '{result2}'")
print()

# EX7:
text = "The lyrics is not that poor!"

not_pos = text.find("not")
poor_pos = text.find("poor")

if not_pos != -1 and poor_pos != -1 and not_pos < poor_pos:
    result = text[:not_pos] + "good" + text[poor_pos + 4:]
else:
    result = text

print(f"Gốc: '{text}'")
print(f"Kết quả: '{result}'")
print()

# EX8
words = ["Python", "Programming", "Exercises", "Code"]

longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word

print(f"Danh sách từ: {words}")
print(f"Từ dài nhất: {longest}")
print(f"Độ dài: {len(longest)}")
print()

# EX9:
text = "Python"
n = 1  # Xóa ký tự ở vị trí 1 (ký tự 'y')

if 0 <= n < len(text):
    result = text[:n] + text[n+1:]
else:
    result = text

print(f"Chuỗi gốc: '{text}'")
print(f"Xóa vị trí {n}: '{result}'")

# EX10:
text = "abcdef"
if len(text) > 1:
    result = text[-1] + text[1:-1] + text[0]
else:
    result = text

print("Bài 10:")
print(f"Gốc: '{text}'")
print(f"Kết quả: '{result}'")
print()

# EX11:
text = "abcdefg"
result = ""
for i in range(len(text)):
    if i % 2 == 0:
        result += text[i]

print("Bài 11:")
print(f"Gốc: '{text}'")
print(f"Kết quả: '{result}'")
print()

# EX12:
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Bài 12:")
print(f"Câu: '{sentence}'")
print(f"Đếm từ: {word_count}")
print()

# EX13:
print("Bài 13:")
user_input = "Hello World"  # Ví dụ
print(f"Input: {user_input}")
print(f"Chữ hoa: {user_input.upper()}")
print(f"Chữ thường: {user_input.lower()}")
print()

# EX14
text = "red, white, black, red, green, black"
words = text.split(", ")
unique_words = list(set(words))  # Loại bỏ trùng lặp
unique_words.sort()  # Sắp xếp theo alphabet

print("Bài 14:")
print(f"Input: {text}")
print(f"Kết quả: {', '.join(unique_words)}")

# EX15
result1 = add_tags('i', 'Python')
result2 = add_tags('b', 'Python Tutorial')

print("Bài 15:")
print(f"add_tags('i', 'Python') -> '{result1}'")
print(f"add_tags('b', 'Python Tutorial') -> '{result2}'")
print()

# EX17
def insert_end(text):
    if len(text) < 2:
        return ""
    last_two = text[-2:]
    return last_two * 4

print(insert_end('Python'))
print(insert_end('Exercises'))
print()

# EX18
def first_three(text):
    if len(text) < 3:
        return text
    return text[:3]

print(first_three('ipy'))
print(first_three('python'))
print(first_three('ab'))
print()

# EX19
def get_before_char(text, char):
    pos = text.rfind(char)
    if pos == -1:
        return text
    return text[pos+1:]

url1 = "https://www.w3resource.com/python-exercises"
url2 = "https://www.w3resource.com/python"

print(get_before_char(url1, '/'))
print(get_before_char(url2, '/'))

# EX20
def reverse_if_multiple_4(text):
    if len(text) % 4 == 0:
        return text[::-1]
    return text

print(reverse_if_multiple_4("abcd"))
print(reverse_if_multiple_4("python"))
print(reverse_if_multiple_4("abcdefgh"))
print()

# EX21
def uppercase_if_condition(text):
    if len(text) < 4:
        first_four = text
    else:
        first_four = text[:4]

    count_upper = 0
    for char in first_four:
        if char.isupper():
            count_upper += 1
    if count_upper >= 2:
        return text.upper()
    return text

print(uppercase_if_condition("PyThon"))
print(uppercase_if_condition("python"))
print(uppercase_if_condition("PYTHON"))
print(uppercase_if_condition("PyTH"))
print()

# EX22
def sort_string(text):
    return ''.join(sorted(text))

print(sort_string("python"))
print(sort_string("hello"))
print(sort_string("Programming"))
print()

# EX23
def remove_newline(text):
    return text.replace('\n', '')

text_with_newline = "Hello\nWorld\nPython"
print("Trước khi xóa:")
print(text_with_newline)
print("Sau khi xóa:")
print(remove_newline(text_with_newline))

# EX64
def max_consecutive_zeros(binary_str):
    max_length = 0
    current_length = 0

    for char in binary_str:
        if char == '0':
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0

    return max_length


print("Bài 64:")
print(max_consecutive_zeros("11000111"))
print(max_consecutive_zeros("1100001110000"))
print()

# EX65
def common_characters(str1, str2):
    common = []
    for char in str1:
        if char in str2 and char not in common:
            common.append(char)

    if len(common) == 0:
        return "No common characters"

    common.sort()
    return ''.join(common)


print("Bài 65:")
print(common_characters("python", "java"))
print(common_characters("hello", "world"))
print(common_characters("abc", "xyz"))
print()

# EX66
def are_anagrams(str1, str2):
    str1_sorted = ''.join(sorted(str1.lower()))
    str2_sorted = ''.join(sorted(str2.lower()))
    return str1_sorted == str2_sorted

print("Bài 66:")
print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "bello"))
print(are_anagrams("python", "typhon"))
print()

#EX67
def remove_consecutive_duplicates(text):
    if len(text) == 0:
        return text

    result = text[0]
    for i in range(1, len(text)):
        if text[i] != text[i - 1]:
            result += text[i]

    return result


print("Bài 67:")
print(remove_consecutive_duplicates("aabbcc"))
print(remove_consecutive_duplicates("aabbbcccd"))
print(remove_consecutive_duplicates("hello"))
print()

# EX68
def separate_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    once = ""
    multiple = ""

    for char in text:
        if char_count[char] == 1 and char not in once:
            once += char
        elif char_count[char] > 1 and char not in multiple:
            multiple += char

    return once, multiple


print("Bài 68:")
text = "hello"
once, multiple = separate_characters(text)
print(f"Xuất hiện 1 lần: '{once}'")
print(f"Xuất hiện nhiều lần: '{multiple}'")

text2 = "programming"
once2, multiple2 = separate_characters(text2)
print(f"Xuất hiện 1 lần: '{once2}'")
print(f"Xuất hiện nhiều lần: '{multiple2}'")

# EX69
def longest_common_substring(str1, str2):
    longest = ""

    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            substring = str1[i:j]
            if substring in str2 and len(substring) > len(longest):
                longest = substring

    return longest

print("Bài 69:")
print(longest_common_substring("GeeksforGeeks", "GeeksQuiz"))
print(longest_common_substring("abcdxyz", "xyzabcd"))
print(longest_common_substring("python", "java"))
print()

# EX 70
def uncommon_characters(str1, str2):
    result = ""
    # Ký tự trong str1 nhưng không trong str2
    for char in str1:
        if char not in str2 and char not in result:
            result += char
    # Ký tự trong str2 nhưng không trong str1
    for char in str2:
        if char not in str1 and char not in result:
            result += char
    return result

print("Bài 70:")
print(uncommon_characters("aab", "bcde"))
print(uncommon_characters("python", "java"))
print(uncommon_characters("hello", "world"))
print()

# EX71
def move_spaces_to_front(text):
    spaces = ""
    non_spaces = ""

    for char in text:
        if char == ' ':
            spaces += char
        else:
            non_spaces += char

    return spaces + non_spaces

print("Bài 71:")
print(f"'{move_spaces_to_front('hello world python')}'")
print(f"'{move_spaces_to_front('a b c d e')}'")
print(f"'{move_spaces_to_front('python programming')}'")

# EX75
# 75. Tìm cửa sổ nhỏ nhất chứa tất cả ký tự riêng biệt
def smallest_window_all_chars(text):
    unique_chars = set(text)
    min_length = len(text)
    result = text

    for i in range(len(text)):
        for j in range(i + len(unique_chars), len(text) + 1):
            window = text[i:j]
            if set(window) == unique_chars and len(window) < min_length:
                min_length = len(window)
                result = window
    return result

print("Bài 75:")
print(smallest_window_all_chars("aabbcc"))
print(smallest_window_all_chars("abcdef"))
print()

# EX76

def count_substrings_k_distinct(text, k):
    count = 0

    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j]
            if len(set(substring)) == k:
                count += 1

    return count


print("Bài 76:")
print(f"abc có 2 ký tự riêng biệt: {count_substrings_k_distinct('abc', 2)}")
print(f"aabc có 2 ký tự riêng biệt: {count_substrings_k_distinct('aabc', 2)}")
print()

# EX 77
def count_non_empty_substrings(text):
    n = len(text)
    return n * (n + 1) // 2

print("Bài 77:")
print(f"abc có {count_non_empty_substrings('abc')} chuỗi con")
print(f"hello có {count_non_empty_substrings('hello')} chuỗi con")
print()

# EX 78
def count_non_empty_substrings(text):
    n = len(text)
    return n * (n + 1) // 2


print("Bài 77:")
print(f"abc có {count_non_empty_substrings('abc')} chuỗi con")
print(f"hello có {count_non_empty_substrings('hello')} chuỗi con")
print()


# 78. Đếm ký tự ở cùng vị trí trong bảng chữ cái
def count_same_position_as_alphabet(text):
    count = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(text)):
        if i < 26 and text[i].lower() == alphabet[i]:
            count += 1

    return count

print("Bài 78:")
print(f"abcdef: {count_same_position_as_alphabet('abcdef')}")
print(f"AbCdEf: {count_same_position_as_alphabet('AbCdEf')}")
print(f"python: {count_same_position_as_alphabet('python')}")
print()

# EX84
def swap_case(text):
    result = ""
    for char in text:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char

    return result


print("Bài 84:")
print(swap_case("PYTHON eXERCISES"))
print(swap_case("jAVA"))
print(swap_case("nUMpY"))

# EX87
def find_common_values(str1, str2):
    common = ""
    for char in str1:
        if char in str2 and char not in common:
            common += char
    return common

print("Bài 87:")
print("Original strings:")
str1 = "Python3"
str2 = "Python2.7"
print(str1)
print(str2)
print("Intersection of two said String:")
result = find_common_values(str1, str2)
print(result)
print()

# EX 90
def remove_duplicate_words(text):
    words = text.split()
    unique_words = []

    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    return ' '.join(unique_words)


print("Bài 90:")
print("Original String:")
original = "Python Exercises Practice Solution Exercises"
print(original)
print("After removing duplicate words from the said string:")
result = remove_duplicate_words(original)
print(result)
print()

# EX 91
def convert_list_to_string(lst):
    result = ""
    for i, item in enumerate(lst):
        if i > 0:
            result += ","
        result += str(item)
    return result

print("Bài 91:")
print("Original list:")
original_list = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
print(original_list)
print("Convert the heterogeneous list of scalars into a string:")
result = convert_list_to_string(original_list)
print(result)

# EX93
def extract_numbers(text):
    numbers = []
    current = ""

    for char in text:
        if char.isdigit():
            current += char
        else:
            if current:
                numbers.append(int(current))
                current = ""
    if current:
        numbers.append(int(current))
    return numbers

text = "red 12 black 45 green"
print(extract_numbers(text))

# EX 95
def rgb_to_hex(r, g, b):
    return f"{r:02X}{g:02X}{b:02X}"

print(rgb_to_hex(255, 165, 1))
print(rgb_to_hex(255, 255, 255))
print(rgb_to_hex(0, 0, 0))
print(rgb_to_hex(0, 0, 128))
print(rgb_to_hex(192, 192, 192))

# EX 98
def decapitalize(text):
    if len(text) == 0:
        return text
    return text[0].lower() + text[1:]

print(decapitalize("Java Script"))
print(decapitalize("Python"))

# EX 101
def add_strings_as_numbers(str1, str2):
    if str1.isdigit() and str2.isdigit():
        return int(str1) + int(str2)
    else:
        return "Error in input!"

print(add_strings_as_numbers("25", "17"))
print(add_strings_as_numbers("abc", "17"))
print(add_strings_as_numbers("25", "xyz"))

# EX 102
def remove_punctuation(text):
    result = ""
    for char in text:
        if char.isalnum() or char == ' ':
            result += char
    return result

text = "String! With. Punctuation?"
print("Original text:")
print(text)
print("After removing Punctuations from the said string:")
print(remove_punctuation(text))