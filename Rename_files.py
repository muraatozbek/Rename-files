import os
path1 = os.chdir("/path/images/folder/")
#First we should give path of images
i = 0

for file1 in os.listdir(path1):
    
    new_file_name1 = "new{}.jpg".format(i)
#new{}.jpg means it gives names new1.jpg,new2.jpg,...
    os.rename(file1, new_file_name1)
#rename the previous name to newname
    i = i+1