import os
import shutil
import glob
from plyer import notification
# Extensions for different types of files
# documents = ['.pdf','.docx','.doc','.txt']
# media = ['.jpeg','.jpg','.svg','.png','.PNG','.mp4','.mp3']
media=['.zip','.7z','.tgz']
# setupFiles = ['.exe','.msi']
# compressedFiles = ['.zip']
# files = ['.apk']

# Path locations of respective folders
# DocumentsLocation = 'C:/Users/Aleti Sunil/Downloads/documents'
mediaLocation = 'C:/Users/navee/Downloads/applications'
# setupFilesLocation = 'C:/Users/Aleti Sunil/Downloads/setupFiles'
# compressedFilesLocation = 'C:/Users/Aleti Sunil/Downloads/compressedFiles'
# FilesLocation = 'C:/Users/Aleti Sunil/Downloads/Files'

# Get all files in the directory
filename = glob.glob("C:/Users/navee/Downloads/*")
def notify(title, message):
    notification.notify(
        title = title,
        message = message,
        timeout = 3
    )


# Iterate over each file
for file in filename:
    # Get the file extension
    fileExtension = os.path.splitext(file)[1]

    # Check the file extension and move the file to the respective folder
    # if fileExtension in documents:
    #     shutil.move(file, DocumentsLocation)
    # elif fileExtension in media:
    #     shutil.move(file, mediaLocation)
    # elif fileExtension in setupFiles:
    #     shutil.move(file, setupFilesLocation)
    # elif fileExtension in compressedFiles:
    #     shutil.move(file, compressedFilesLocation)
    # elif fileExtension in files:
    #     shutil.move(file, FilesLocation)
    if fileExtension in media:
       shutil.move(file, mediaLocation)
print("Files have been sorted")
notify("File Sorting Success", "Sorting of files in /home/navee has been completed")