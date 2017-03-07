
target = "G:\\Python Folder"
source = "F:\\pictures"


import pygame, sys, random
import glob,func, os

def scan(name):
    name=name+'\\*'
    files=glob.glob(name)
    List=[]
    y=[]
    for File in files:
        if  File.lower().__contains__('.jpg'):
            List.append(File)
        elif not File.__contains__('.'):
            y.append(File)
    return List,y

def copy(sorfolder, tarfolder, file_):
    sorce = open(sorfolder + file_, 'rb')
    target = open(tarfolder + file_, 'wb')
    for line in sorce.readlines():
        target.write(line)
    sorce.close()
    target.close()
screen = pygame.display.set_mode([500,500])
    
files, dirList = scan(source)
pygame.init()
print files
print ""
print "========================================"
print ""
print dirList
while dirList:
    Dir = dirList[0]
    dirList.remove(Dir)
    print "scan "+ Dir + " ?"
    done = False
    test = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    
                    test = True
                done = True
    if test:           
        tarDir = target + Dir[len(source):len(Dir)]
        print tarDir
        if not os.path.exists(tarDir):
            os.makedirs(tarDir)
        files, dirList2 = scan(Dir)
        print Dir
        print files
        print dirList2
        dirList.extend(dirList2)
        for file_ in files:
            print file_
            done = False
            picture = pygame.image.load(file_)
            picture =  pygame.transform.scale(pygame.transform.rotate(picture, 90),
                                              [picture.get_height()/10,picture.get_width()/10])
            screen = pygame.display.set_mode([picture.get_width(), picture.get_height()])
            while not done:
                
                
                screen.blit(picture, [0,0])
            
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        sys.exit()
                    elif event.type==pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            copy(source, target, file_[len(source):len(file_)])
                            done = True
                        else:
                            done = True


pygame.quit()
