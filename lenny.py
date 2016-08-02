import faces
from random import randint

def pickRandom(list):
    return list[randint(0,len(list))]


def pickPart(parts,index):
    #makes sure it doesn't try to pick index 1 if the part only has one version
    return parts[min(index,len(parts)-1)]

def CreateFace():
    ear = pickRandom(ears)
    mouth = pickRandom(mouths)
    eye = pickRandom(eyes)
    return ear[0] + eye[0] + mouth[0] + eye[len(eye)-1]+ear[len(ear)-1]

if __name__ == "__main__":


    print(str(CreateFace().encode('ascii')))