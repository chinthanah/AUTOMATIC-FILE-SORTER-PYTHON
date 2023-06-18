AUTOMATIC FILE SORTER


import os,shutil
path=r"C:/Users/chint/OneDrive/Desktop/PYTHON/"
file_name=os.listdir(path)
Folder_names=['csv files','jpg files','pdf files','png files']

for loop in range(0,4):
    if not os.path.exists(path+Folder_names[loop]):
        print(path+Folder_names[loop])
        os.makedirs(path+Folder_names[loop])
        
    
        for file in file_name:
    if '.csv' in file and not os.path.exists(path+'csv files/'+file):
        shutil.move(path+file,path+'csv files/'+file)
    elif '.jpg' in file and not os.path.exists(path+'jpg files/'+file):
        shutil.move(path+file,path+'jpg files/'+file)
    elif '.pdf' in file and not os.path.exists(path+'pdf files/'+file):
        shutil.move(path+file,path+'pdf files/'+file)
    elif '.png' in file and not os.path.exists(path+'png files/'+file):
        shutil.move(path+file,path+'png files/'+file)


