import os
checkingPath = "C:\\Users\\DwarfKhan\\Documents\\work\\TechAcademyLocalRepos\\PythonSmallProjects\\TestFolder"
fileList = os.listdir(checkingPath)
print(fileList)
textFileList = []

for file in fileList:
    isTxt = file.find(".txt")
    if isTxt != -1:
        textFileList.append(file)

for file in textFileList:
    absPath = os.path.join(checkingPath,file)
    fileTime = os.path.getmtime(absPath)
    print("{}\n Was Modified:{}\n\n".format(file,fileTime))

