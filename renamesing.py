import os
import string
def rename_files():
    file_list = os.listdir(r"E:\Study\Udacity\Movie Trailer\Secret message\prank");
    File_paths = os.getcwd();
    os.chdir(r"E:\Study\Udacity\Movie Trailer\Secret message\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(File_paths);
rename_files()
