import os

def CreateFolder(folderName, basePath=''):
    # Construct the full path to the folder
    fullPath = os.path.join(basePath, folderName)
    
    try:
        if not os.path.exists(fullPath):
            os.makedirs(fullPath)
            print(f"{folderName} Folder Created at {fullPath}")
        else:
            print(f"{folderName} Folder already exists at {fullPath}.")
    except Exception as e:
        print(f"Error creating {folderName} Folder at {fullPath}: {e}")

# Specify the base path where the folders should be created
basePath = r'C:\Users\priti\OneDrive\Desktop\cluttered'

# List files in the base path
files = os.listdir(basePath)
print(files)

CreateFolder('Images', basePath)
CreateFolder('Documents', basePath)
CreateFolder('Media', basePath)
CreateFolder('Softwares', basePath)
CreateFolder('Others', basePath)

ImgExt = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg']
DocExt = ['.txt', '.doc', '.docx', '.pdf', '.xls', '.xlsx', '.ppt', '.pptx']
MedExt = ['.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv', '.webm','.mp3', '.wav', '.aac', '.flac']
SoftExt = ['.exe', '.msi']

def MoveFiles():
    for file in files:
        if os.path.splitext(file)[1].lower() in ImgExt and os.path.isfile(os.path.join(basePath, file)):
            os.replace(os.path.join(basePath, file), os.path.join(basePath, "Images", file))
        
        elif os.path.splitext(file)[1].lower() in DocExt and os.path.isfile(os.path.join(basePath, file)):
            os.replace(os.path.join(basePath, file), os.path.join(basePath, "Documents", file))

        elif os.path.splitext(file)[1].lower() in MedExt and os.path.isfile(os.path.join(basePath, file)):
            os.replace(os.path.join(basePath, file), os.path.join(basePath, "Media", file))

        elif os.path.splitext(file)[1].lower() in SoftExt and os.path.isfile(os.path.join(basePath, file)):
            os.replace(os.path.join(basePath, file), os.path.join(basePath, "Softwares", file))

        else:
            if os.path.isfile(os.path.join(basePath, file)):
                os.replace(os.path.join(basePath, file), os.path.join(basePath, "Others", file))

    print("Files Moved Successfully!") 

MoveFiles()