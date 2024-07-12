import os
files = os.listdir()
print(files)

def CreateFolder(folderName):
    try:
        os.mkdir(folderName)
    except FileExistsError:
        print("Folder already exists")

CreateFolder('Images')
CreateFolder('Documents')
CreateFolder('Media')
CreateFolder('Softwares')
CreateFolder('Others')

ImgExt = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg']
DocExt = ['.txt', '.doc', '.docx', '.pdf', '.xls', '.xlsx', '.ppt', '.pptx']
MedExt = ['.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv', '.webm','.mp3', '.wav', '.aac', '.flac']
SoftExt = ['.exe', '.msi']

def MoveFiles():
    for file in files:
        if os.path.splitext(file)[1] in ImgExt and os.path.isfile(file):
            os.replace(file, f"Images/{file}")
        
        elif os.path.splitext(file)[1] in DocExt and os.path.isfile(file):
            os.replace(file, f"Documents/{file}")

        elif os.path.splitext(file)[1] in MedExt and os.path.isfile(file):
            os.replace(file, f"Media/{file}")

        elif os.path.splitext(file)[1] in SoftExt and os.path.isfile(file):
            os.replace(file, f"Softwares/{file}")

        else:
            if os.path.isfile(file):
                os.replace(file, f"Others/{file}")

            else:
                pass

MoveFiles()