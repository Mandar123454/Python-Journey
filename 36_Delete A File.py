import os
import shutil

# path = "test.txt"
# path = "empty_folder"
path = "folder"

try:
    # os.remove(path) # delete a file
    #os.rmdir(path) # rmdir means remove dirctory # delete an empty directory
    shutil.rmtree(path) # rmtree means remove tree # delete a directory contain files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")