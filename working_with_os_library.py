import os

# ví dụ 1
# print("Sentence 1")
# os.abort()    để chỉ in những câu trước đó
# print("Sentence 2")

# ví dụ 2
# path = "F:/Hajiin/Hajiin dowload/ChromeSetup.exe"
# check = os.access(path, os.F_OK)    F = find: tìm xem có file không
# check_1 = os.access(path, os.R_OK)  R = read: đọc file
# check_2 = os.access(path, os.W_OK)  W = write: ghi đè lên file
# check_3 = os.access(path, os.X_OK)  A = append: thêm vào file (vào cuối file)
# print(f"check: {check}, check 1: {check_1}, check 2: {check_2}, check 3: {check_3}")

# ví dụ 3
# print("Current directory: ", os.getcwd())       xem thư mục hiện tại
# print("Current directory: ", os.listdir())      in ra toàn bộ tệp có trong thư mục hiện tại

# ví dụ 4
# if not os.path.exists("New_dir"):   
#     os.mkdir("New_dir")    tạo thư mục mới
# os.chdir("New_dir")        di chuyển từ thư mục hiện tại tới thư mục khác 
# print("Current directory: ", os.getcwd())
