import os
from string import digits
def rename_files():
    file_list = os.listdir(r"E:\Study\Udacity\Movie Trailer\Secret message\prank")
    saved_path = os.getcwd();
    os.chdir(r"E:\Study\Udacity\Movie Trailer\Secret message\prank")
    for cfile in file_list:
        oldfile = cfile
        newfile = cfile.translate(None,"0123456789")
        print("Old File : "+oldfile+" New File : "+newfile)
        
        os.rename(oldfile,newfile)

    os.chdir(saved_path)
rename_files()    
