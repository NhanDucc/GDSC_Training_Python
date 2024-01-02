# def read_from_file():    mở file
#     with open('text.txt', 'r') as file:
#         content = file.read()
#         print(content)
# read_from_file()

# f = open('text.txt', 'r')
# file = f.readlines()    in nội dung trong file ra dạng mảng
# # # print(f.readlines())     
# # for i in f:
# #     print(i.strip())    strip để loại bỏ các dấu Enter

# def search_by_name(text: str, file) -> str:
#     keyword: str = text.lower()
#     words = keyword.split()
#     for line in file:
#         if all(word in line.lower() for word in words):
#           return line
# print(search_by_name("Mia", file))

import os
os.remove('text.txt')
if os.path.exists('text.txt'):
    print('file exist')
else:
    print('file not exist')
