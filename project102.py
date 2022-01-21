import cv2 
import dropbox
import time
import random


startTime = time.time()

def apple():
    r = random.randint(0,10)
    
    cvObject = cv2.VideoCapture(0)
    result = True

    while(True):
        ret , frame = cvObject.read()
        imgname = "sakai" + str(r) + ".png"
        cv2.imwrite(imgname , frame)
        result = False

    return imgname
    print("Snapshot taken!!!!!!!!!!!!!!!!!!!!!!!!!! ")
    cvObject.release()
    cv2.destroyAllWindows()

def uploadFile(imgname):
    accessToken = "sl.BAhUOUeol7WOtOAawJGMyy5eCWHyHkUSRieIG6wv1PoKs7FQDdfdnBbfL_Lb37g1YL17UolCA1bRGYN4aId4qdo_BJgJ3tLa2xQuis0aR29abF22hcFZ5fU0EFpu_EsIZy_zHhyUGyzL"
    filefrom = imgname
    fileto = "/sakaiSnaps/"+(imgname)
    dbx = dropbox.Dropbox(accessToken)

    with open(filefrom, 'rb') as f:
        dbx.files_upload(f.read(), fileto ,mode = dropbox.files.WriteMode.overwrite  )
        print("Uploaded!!!!!!!!!")

def meannnn():
    while(True):
        if( (time.time() - startTime) >= 5  ):
            name = apple()
            uploadFile(name)

meannnn()