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

moved = 0

foldername = input("What is your folder name?: ")
newfolder = input("What is the new folder's name?: ")

currdir = os.getcwd()
folder_path = os.path.join(currdir,foldername)
# folder_path = os.path.join(root,foldername)
print("FOLDER PATH: ",folder_path)


fileslist = os.listdir(folder_path)
print("FILES : ",fileslist)
print("\n")

knownpath = os.path.join(folder_path,fileslist[0])
known = cv.imread(knownpath)
known = resize_image(known)
print("The picture shown right now is taken as known.")
cv.imshow("IMAGE THAT IS KNOWN",known)
cv.waitKey(100)
knownRGB = cv.cvtColor(known,cv.COLOR_BGR2RGB)
knownfaceencoding = fr.face_encodings(knownRGB)[0]

os.makedirs(newfolder,exist_ok=True)


for file in fileslist:
    
    unknownpath = os.path.join(folder_path,file)
    unknown = cv.imread(unknownpath)
    unknown = resize_image(unknown)
    unknownRGB = cv.cvtColor(unknown,cv.COLOR_BGR2RGB)

    try:
        unknownfaceencoding = fr.face_encodings(unknownRGB)[0]

        res = fr.compare_faces([knownfaceencoding],unknownfaceencoding,tolerance=0.6)[0]
        if res:
            print(f"{unknownpath} File is moved.")
            shutil.move(unknownpath,newfolder)

            moved += 1
    
    except:
        cv.imshow('UNKNOWN IMAGE',unknown)
        cv.waitKey(100)
        ask = input("Do you want to moved this image?(y/n): ").lower()

        if ask == 'y':
            print(f"{unknownpath} File is moved.")
            os.remove(unknownpath)
            moved +=1
        else:
            print("As you did not type 'y', the picture will stay.")



if moved == 0:
    print("No files moved.")
else:
    print(f"{moved} files moved.")        
    