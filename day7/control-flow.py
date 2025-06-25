import sys
def saveToStorage(mediaType):
    if(mediaType == "image"):
        print("Execute save to cloudinary method")
    elif(mediaType == "video"):
        print("Execute save to mux method")
    else:
        print("Invalid media type")    

try:
    media_type = str(sys.argv[1])
    saveToStorage(media_type)
except:
    print("You must pass media type argument!")    