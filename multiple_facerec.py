import os
import cv2 as cv
import face_recognition as fr
import shutil

def resize_image(image, max_size=1024):
    h, w = image.shape[:2]
    if max(h, w) > max_size:
        scale = max_size / max(h, w)
        new_size = (int(w * scale), int(h * scale))
        return cv.resize(image, new_size)
    return image



foldername = input("What is your folder name?: ")
newfolder = input("What is the new folder's name?: ")

currdir = os.getcwd()

folderPath = os.path.join(currdir,foldername)

filesList = os.listdir(folderPath)

knownPath = os.path.join(folderPath,filesList[0])
known = cv.imread(knownPath)
known = resize_image(known)
print("The picture shown right now is taken as known.")
cv.imshow("IMAGE THAT IS KNOWN",known)
cv.waitKey(100)
knownRGB = cv.cvtColor(known,cv.COLOR_BGR2RGB)
knownFace = fr.face_encodings(knownRGB)[0]

os.makedirs(newfolder,exist_ok=True)

for file in filesList:

    unknownPath = os.path.join(folderPath,file)
    unknown = cv.imread(unknownPath)
    unknown = resize_image(unknown)
    unknownRGB = cv.cvtColor(unknown,cv.COLOR_BGR2RGB)


    facelocations = fr.face_locations(unknownRGB)
    faceencodings = fr.face_encodings(unknownRGB,facelocations)


    if len(facelocations) > 0:

        for encodings in faceencodings:
                
                
            res = fr.compare_faces([knownFace],encodings)[0]
                
            if res == True:
                print(f"{unknownPath} file is moved.")
                shutil.move(unknownPath,newfolder)

                break

    else:

        print("Do you want to move this image?")
        cv.imshow('UNKNOWN IMAGE',unknown)
        cv.waitKey(0)
        ask = input('y/n?: ').lower()

        if ask == 'y':
            print(f"{unknownPath} File is moved.")
            shutil.move(unknownPath,newfolder)

            
        else:
            print("As you did not type 'y', the picture will stay.")

        
            

