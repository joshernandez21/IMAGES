import os
import re
import shutil

# Get the list of all files and directories
path = "/media/sf_Media/Movies"
dir_list = os.listdir(path)
# for file in dir_list:
#     if file.endswith('.mp4'):
#         print("The original filename is : " + str(file))


#         folder_name = re.sub(r'([0-9]{4}).*$', r'\1', file)
#         dir_path = path + "/" + folder_name
#         os.mkdir(dir_path)
#         src_path = path + "/" + file
#         dst_path = path + "/" + folder_name + "/" + file
#         shutil.move(src_path, dst_path)
#         print("Extracted String : " + folder_name)


for file in dir_list:
    try:
        if file.endswith('.srt'):
            print("The original filename is : " + str(file))
            folder_name = re.sub(r'([0-9]{4}).*$', r'\1', file)
            dir_path = path + "/" + folder_name
            src_path = path + "/" + file
            dst_path = path + "/" + folder_name + "/" + file
            shutil.move(src_path, dst_path)
            print("Extracted String : " + folder_name)
    except:
        print("Unable to move file")






