import os, shutil

from_dir="Document_Files"
to_dir="Downloads"

list_of_files = os.listdir("Document_Files")
print(list_of_files)

for i in list_of_files:
    file_name, extension = os.path.splitext(i)
    if extension == "":
        continue
    if extension in [".pdf", ".doc", ".txt"]:
        path1 = from_dir+"/"+i
        path2 = to_dir +"/"+ "Document_Files"
        path3 = to_dir + "/" + "Document_Files" + "/"+ i
        if os.path.exists(path2)== True:
            print("Moving File")
            shutil.move(path1, path2)
        else:
            print("Path Not Found")
            print("Creating New Folder")
            os.makedirs(path2)
            print("Moving File")
            shutil.move(path1, path3)            