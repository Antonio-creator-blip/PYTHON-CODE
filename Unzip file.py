import zipfile
import os
for i in range(0,5,1):
    path_to_Zip_file = "flag" + str(6-i) + ".zip"
    directory_to_extract_to = ""
    Zip_ref = zipfile.ZipFile(path_to_Zip_file, 'r')
    Zip_ref.extractall(directory_to_extract_to)
    Zip_ref.close()
    os.remove(path_to_Zip_file)
