import os
import shutil

# Đường dẫn tới thư mục chứa 10 folder con
parent_folder_path = 'tempClassMay1'

# Đường dẫn tới thư mục chứa 10 vid
video_folder_path = 'Video_Alphabet'

# Lấy danh sách tất cả các folder con trong thư mục cha
subfolders = [f.path for f in os.scandir(parent_folder_path) if f.is_dir()]

# Lấy danh sách tất cả các vid trong thư mục vid
videos = [f for f in os.listdir(video_folder_path) if os.path.isfile(os.path.join(video_folder_path, f))]

# Đảm bảo số lượng folder con và video là như nhau
if len(subfolders) != len(videos):
    print("Số lượng folder con và video không khớp!")
    exit()

# Di chuyển các video vào từng folder con theo thứ tự
for i in range(len(subfolders)):
    video_path = os.path.join(video_folder_path, videos[i])
    destination_path = os.path.join(subfolders[i], videos[i])
    shutil.move(video_path, destination_path)

print("Hoàn thành việc di chuyển video vào các thư mục con!")
