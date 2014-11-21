from Myro import *
#This is the editing and Performance code, a lot of GIFS are loaded and combined in this code along with several special effects applied to the GIFS
#Initial constants used throughout the code
hx2=354
hx1=21
hy2=240
hy1=0

dx2=304
dx1=100
dy2=238
dy1=13

def blueScreen(pBlue, pic):                #Used for the first part to put harry and draco on the quidditch pitch
    pBlue=loadPicture(pBlue)
    pic=loadPicture(pic)
    h=getHeight(pBlue)
    w=getWidth(pBlue)

    newPic=makePicture(w, h-50)
    show(newPic)
    for j in range(h):
        for i in range(w):
            pxB=getPixel(pBlue, i, j)
            pxP=getPixel(pic, i, j)
            pxN=getPixel(newPic, i, j)
            if getRed(pxB)!=0 and getGreen(pxB)!=0:
                if getBlue(pxB)>getRed(pxB) and getBlue(pxB)>getGreen(pxB) and getBlue(pxB)>130 and getGreen(pxB)>130 and getRed(pxB)>130:
                    setRGB(pxN, getRGB(pxP))
                else: setRGB(pxN, getRGB(pxB))
    show(newPic)
    savePicture(newPic, "HarryDracoStart2.jpg")


def greenScreen(pGreen, pic):                #Edited into blueScreen code for the first part of the movie
    if getHeight(pGreen)<getHeight(pic):
        h=getHeight(pGreen)
    else: h=getHeight(pic)
    if getWidth(pGreen)<getWidth(pic):
        w=getWidth(pGreen)
    else: w=getWidth(pic)
    newPic=makePicture(w, h)
    show(newPic)
    for j in range(h):
        for i in range(w):
            pxG=getPixel(pGreen, i, j)
            pxP=getPixel(pic, i, j)
            pxN=getPixel(newPic, i, j)
            if getRed(pxG)!=0 and getBlue(pxG)!=0:
                if getGreen(pxG)/getRed(pxG)>1.2 and getGreen(pxG)/getBlue(pxG)>1.1:
                    setRGB(pxN, getRGB(pxP))
                else: setRGB(pxN, getRGB(pxG))
    show(newPic)



def overlayPic(face, Pic, Dx, Dy):          #Base overlay function to put harry or draco's faces onto the robots
    a=loadPicture(face)
    pic=loadPicture(Pic)
    Dx=int(Dx)
    Dy=int(Dy)
    numx=(dx2-dx1)//2
    numy=(dy2-dy1)//2
    for I, i in zip(range(Dx-numx, Dx+numx), range(dx1, dx2)):
        for J, j in zip(range(Dy-numy, Dy+numy), range(dy1, dy2)):
            pix=getPixel(a, i, j)
            PIX=getPixel(pic, I, J)
            if getRed(pix)>5 and getGreen(pix)>5 and getBlue(pix)>5:
                setRGB(PIX, getRGB(pix))
    show(pic)
    savePicture(pic, "HarryDracoBlueFace2.jpg")


def overlayDGIF(pics):                      #Overlaying Draco's face when they first see the snitch
    a=loadPicture("dracoM.jpg")
    b=loadPicture("DracoScared.png")
    pics=loadPictures("DracoHarry.gif")
    Dx=638#584
    Dy=502
    for x in range(20):
        if x!=16 and x!=17:
            for I, i in zip(range(Dx-150, Dx+150), range(101, 305)):
                for J, j in zip(range(Dy-112, Dy+112), range(12, 238)):
                    pix=getPixel(a, i, j)
                    PIX=getPixel(pics[x], I, J)
                    if getRed(pix)>5 and getGreen(pix)>5 and getBlue(pix)>5:
                        setRGB(PIX, getRGB(pix))
        else:
    for I, i in zip(range(Dx-102, Dx+102), range(101, 305)):
        for J, j in zip(range(Dy-112, Dy+112), range(12, 238)):
            pix=getPixel(b, i, j)
            PIX=getPixel(pics, I, J)
            if getRed(pix)!=255 and getGreen(pix)!=255 and getBlue(pix)!=255:
                setRGB(PIX, getRGB(pix))
        Dx=Dx+10
        if x==4:
            Dx=576
        if x==10:
            Dx=610
        if x==14 or x==15 or x==16 or x==17:
            Dx=638
        if x==18 or x==19:
            Dx=628
    return(pics)
    savePicture(pics, name)#"DracoHarryFace.gif")




def combineHS():                            #Combining two gifs into one after finishing filming them
    aList=loadPictures("HarrySplit.gif")
    print("loaded aList")
    bList=loadPictures("HarrySplit2.gif")
    print("loaded bList")
    for i in range(27, 60):
        print("i is on: ", i)
        aList.append(bList[i])
    print("Saving Pictures...")
    savePicture(aList, "HarrySplit3.gif")




def overlayHGIF(PList):                         #Overlaying Harry's face when they first see the snitch
    a=loadPicture("Harry.png")
    b=loadPicture("HarryScared.jpg")
    pics=loadPicture(PList)
    print("Loaded Pictures")
    Dx=862
    Dy=515
    for x in range(len(pics)):
        if x!=16 and x!=17:
          for I, i in zip(range(Dx-165, Dx+165), range(22, 353)):
             for J, j in zip(range(Dy-120, Dy+120), range(0, 240)):
                pix=getPixel(a, i, j)
                PIX=getPixel(pics[x], I, J)
                if getRed(pix)!=255 and getGreen(pix)!=255 and getBlue(pix)!=255:
                   setRGB(PIX, getRGB(pix))
        else:
            for I, i in zip(range(Dx-138, Dx+138), range(34, 310)):
                for J, j in zip(range(Dy-152, Dy+152), range(9, 313)):
                    pix=getPixel(b, i, j)
                    PIX=getPixel(pics, I, J)
                    if getRed(pix)!=255 and getGreen(pix)!=255 and getBlue(pix)!=255:
                        setRGB(PIX, getRGB(pix))

        if x<6:
           Dx=Dx-10
        elif x<13:
            Dx=Dx-6
            if x==11:
               Dx==790
        Dx=792

    print("Saving Pictures")
    #return(pics)
    savePicture(pics, "DracoHarryFace.gif")


def splitScreen():                          #Making two GIF's into a split screen
    picsTop=loadPicture("HarrySplitFace2.gif")
    print("Loaded 1")
    picsBot=loadPicture("DracoSplitFace.gif")
    print("Loaded 2")
    aList=[]
    for i in range(1):
        altox=getHeight(picsTop)#[i])
        altoy=getHeight(picsBot)#[i])
        new=makePicture(getWidth(picsTop), altox+altoy)
        for pix in getPixels(picsTop):
            a=getX(pix)
            b=getY(pix)
            c=getRGB(pix)
            d=getPixel(new, a, b)
            setRGB(d, c)
        for pix in getPixels(picsBot):
            a=getX(pix)
            b=getY(pix)
            c=getRGB(pix)
            d=getPixel(new, a, b+getHeight(picsTop))
            setRGB(d, c)
        aList.append(new)
    print("Saving Pictures...")
    savePicture(aList, "SplitTest.gif")


def splitScreen2():                  #Cropping each picture in the split screen into smaller versions of themselves so that the function takes lesser time. Then putting them into a split screen
    picsTop=loadPictures("HarrySplitFace2.gif")
    print("Loaded 1")
    picsBot=loadPictures("DracoSplitFace.gif")
    print("Loaded 2")
    aList=[]
    h=getHeight(picsTop[0])
    w=getWidth(picsTop[0])
    for x in range(len(picsTop)):
        new=makePicture(w*5//6, 5*h//3)
        print("Picture ", x+1, "Starting Top")
        for i in range(w*5//6):
            for j, j2 in zip(range(h//4,h*5//6), range(h*5//6-h//4)):
                pix=getPixel(picsTop[x], i, j)
                setRGB(getPixel(new, i, j2), getRGB(pix))
        print("Picture ", x+1, "Starting Bottom")
        for I in range(w*5//6):
            for J, J2 in zip(range(h//4,h*5//6), range(h*5//6-h//4)):
                PIX=getPixel(picsBot[x], I, J)
                setRGB(getPixel(new, I, J2+j2), getRGB(PIX))
        aList.append(new)
    print("Saving Pictures...")
    savePicture(aList, "SplitTest2.gif")


def combineFall():                  #Combining two GIFS into one to make the fall longer. Taking alternate pictures of each GIF and making it into one GIF
    pics1=loadPictures("zoomOut2.gif")
    print("loaded 1")
    pics2=loadPictures("DracoFalling.gif")
    print("loaded 2")
    aList=[]
    for i in range(len(pics1)):
        aList.append(pics1[i])
        aList.append(pics2[i])
    print("saving pictures")
    savePicture(aList, "DracoFallFinal.gif")


def overlayFall():              #Overlaying Draco's face onto each picture during his fall
    pics=loadPictures("DracoFalling.gif")
    a=loadPicture("DracoScared.png")
    print("Loaded Pictures")
    Dx=910
    Dy=266
    Dx=[902,926,919,846,724,798,715,794,618,599,721,672,600,700,843]
    Dy=[258,250,240,346,334,284,289,391,527,537,541,658,523,442,424]
    for x in range(len(pics)):
        for I, i in zip(range(Dx[x]-97, Dx[x]+97), range(37, 231)):
            for J, j in zip(range(Dy[x]-123, Dy[x]+123), range(0, 246)):
                pix=getPixel(a, i, j)
                PIX=getPixel(pics[x], I, J)
                if getRed(pix)!=255 and getGreen(pix)!=255 and getBlue(pix)!=255:
                    setRGB(PIX, getRGB(pix))
    savePicture(pics, "DracoFaceFall.gif")


def iPhoneGIF():            #Loading iPhone pictures on the hard disk and making them into one continuous GIF
    aList=[]
    for i in range(55):
        name="IMG_{}[1].jpg"        #Notice the clever use of string formatting to load a lot of similarly named pictures using just one function
        aList.append(loadPicture(name.format(5118+i)))
    print("Loaded Pictures")
    savePicture(aList, "Chase.gif")


def putSnitch(PList):       #Overlaying the snitch onto the last few picture in a GIF scene...when Harry and Draco first see the snitch
    pics=loadPictures(PList)
    a=loadPicture("snitch.png")
    print("Loaded Pictures")
    Dx=685
    Dy=210
    for x in range(14, 20):

        for I, i in zip(range(Dx-200, Dx+200), range(0, 400)):
            for J, j in zip(range(Dy-94, Dy+94), range(0, 188)):
                pix=getPixel(a, i, j)
                PIX=getPixel(pics[x], I, J)
                if getRGB(pix)!=(255,255,255):
                    setRGB(PIX, getRGB(pix))
    for num in range(12, 20):
        show(pics[num])
        wait(2)
    savePicture(pics, "DracoHarryFace.gif")


def SnitchMove():       #Making the Snitch move, leaving everthing else in the scene to remain stationary
    pics=loadPictures("DracoHarry.gif")
    a=loadPicture("snitch.png")
    aList=[]
    aPic=overlayDGIF(pics[19])
    aPic=overlayHGIF(aPic)
    for i in range(20):
        aList.append(copyPicture(aPic))
    Dx=685
    Dy=210
    for x in range(len(aList)):
        for I, i in zip(range(Dx-200, Dx+200), range(0, 400)):
            for J, j in zip(range(Dy-94, Dy+94), range(0, 188)):
                pix=getPixel(a, i, j)
                PIX=getPixel(aList[x], I, J)
                if getRGB(pix)!=(255,255,255):
                    setRGB(PIX, getRGB(pix))
        Dx=Dx-Dx//20
    savePicture(aList, "SnitchMoving.gif")

def chaseOverlay():         #Overlaying Harry's and Draco's Face along with the picture Snitch onto each picture in the Chase Scene
    a=loadPicture("Harry.png")
    b=loadPicture("dracoFlipped.jpg")
    c=loadPicture("snitch.png")
    pics=loadPictures("Chase.gif")
    print("Loaded Pictures")
    Dx=[660,600,590,576,576,569,564,560,551,544,534,526,522,515,512,504,500,502,496,488,488,482,476,469,469,468,463,456,453,448,443,440,434,417,414,407,406,402,397,394,388,388,388,381,381,374,374,367,360,364,366,361,368,372,368]
    Dy=388
    Hx=[848,901,888,867,856,856,844,839,824,808,793,789,784,769,765,751,751,744,734,719,719,712,712,708,704,692,692,688,674,662,656,648,638,621,612,599,599,599,586,581,575,575,568,568,568,568,568,561,538,538,532,520,520,514,509]
    Hy=459
    Sx=[509,417,405,385,390,386,381,374,334,322,322,305,302,286,282,246,251,250,242,242,232,237,231,208,202,198,192,187,171,155,154,158,158,161,169,173,170,174,174,174,174,174,174,174,174,174,174,174,163,163,163,163,163,163,163]
    Sy=362
    for x in range(len(pics)):
        for I, i in zip(range(Hx[x]-165, Hx[x]+165), range(22, 353)):
            for J, j in zip(range(Hy-120, Hy+120), range(0, 240)):
                pix=getPixel(a, i, j)
                PIX=getPixel(pics[x], I, J)
                if getRed(pix)!=255 and getGreen(pix)!=255 and getBlue(pix)!=255:
                    setRGB(PIX, getRGB(pix))
        if x==0:
            Hy=538
        if x==1:
            Hy=523
        if x==17:
            Hy=509
        if x==22:
            Hy=496
        if x==32:
            Hy=486
        if x==47:
            Hy=474


        for I, i in zip(range(Dx[x]-102, Dx[x]+102), range(101, 305)):
            for J, j in zip(range(Dy-112, Dy+112), range(12, 238)):
                pix=getPixel(b, i, j)
                PIX=getPixel(pics[x], I, J)
                if getRed(pix)!=255 and getGreen(pix)!=255 and getBlue(pix)!=255:
                    setRGB(PIX, getRGB(pix))
        if x==0:
            Dy=473
        if x==1:
            Dy=458
        elif x<23:
            Dy=450
        elif x<33:
            Dy=431
        elif x<47:
            Dy=421
        else:
            Dy=410

        for I, i in zip(range(Sx[x]-200, Sx[x]+200), range(0, 400)):
            for J, j in zip(range(Sy-94, Sy+94), range(0, 188)):
                pix=getPixel(c, i, j)
                PIX=getPixel(pics[x], I, J)
                if getRGB(pix)!=(255,255,255):
                    setRGB(PIX, getRGB(pix))
        if x==0:
            Sy=358
        if x==1:
            Sy=349
        if x==3:
            Sy==342
        if x==11 or x==13 or x==16 or x==25:
            Sy=323
        if x==12 or x==24 or x==32:
            Sy=315
        if x==14:
            Sy=330
        if x==33:
            Sy=300
        if x==47:
            Sy=292
    savePicture(pics, "chaseFaces.gif")



def fade(aList):                        #Fading the end of the chase scene into darkness showing the emergence of the Dementors
    bList=[copyPicture(aList[0])]
    show(aList[0])
    j=0
    for i in range (len(aList),0,-1):
        print("Picture no.", i+1)
        for pix in getPixels(aList[j]):
            setRGB(pix, getRed(pix)-(getRed(pix)/i), getGreen(pix)-(getGreen(pix)/i), getBlue(pix)-(getBlue(pix)/i))
        p2=copyPicture(aList[j])
        bList.append(p2)
        j+=1
    print("saving pictures")
    savePicture(bList, "FADE.gif")



def crossFade(p1, p2):                 #CrossFading multiple scenes into another
    aList=[copyPicture(p1)]
    show(p1)
    RGBp2=getPixels(p2)
    for i in range(8, 0, -1):
        for pix1, pix2 in zip(getPixels(p1), getPixels(p2)):
            setRGB(pix1, getRed(pix1)-((getRed(pix1)-getRed(pix2))/i), getGreen(pix1)-((getGreen(pix1)-getGreen(pix2))/i), getBlue(pix1)-((getBlue(pix1)-getBlue(pix2))/i))
        p=copyPicture(p1)
        aList.append(p)
    savePicture(aList, "fadeAway.gif")



def seeingRed(p, a):               #Showing the blood effect at the end of Draco's fall to show him getting hurt
    for x in range(a, len(p)):
        for pix in getPixels(p[x]):
            setRed(pix, 255)
    savePicture(p, "RedDracoFall.gif")



def dementorOverlay(pics):          #Cropping and overlaying the picture of a Dementor onto the scenes
    a=loadPicture("dementor.jpg")
    pics=loadPictures(pics)
    Hx=924
    Hy=232
    for x in range(15, len(pics)):
        for I, i in zip(range(Hx-200, Hx+200), range(0, 400)):
            for J, j in zip(range(Hy-186, Hy+186), range(0, 372)):
                pix=getPixel(a, i, j)
                PIX=getPixel(pics[x], I, J)
                if getRed(pix)!=255 and getGreen(pix)!=255 and getBlue(pix)!=255:
                    setRGB(PIX, getRGB(pix))
    savePicture(pics, "HarryDementor.gif")



def overlayHarryCatch():            #Overayin a picture of the snitch and Harry's face in the last scene when he catches the snitch
    pics=loadPictures("chasing_snitch.gif")
    a=loadPicture("Harry.png")
    b=loadPicture("HarryHappy.png")
    c=loadPicture("snitch.png")
    print("Loaded Pictures")
    Dx=343
    Dy=502
    Sx=1002
    Sy=470
    for x in range(len(pics)):
        print("Picture no.", x+1)
        for I, i in zip(range(Sx-200, Sx+200), range(0, 400)):
            for J, j in zip(range(Sy-94, Sy+94), range(0, 188)):
                pix=getPixel(c, i, j)
                PIX=getPixel(pics[x], I, J)
                if getRGB(pix)!=(255,255,255):
                    setRGB(PIX, getRGB(pix))

        if x<52:
            for I, i in zip(range(Dx-165, Dx+165), range(22, 353)):
                for J, j in zip(range(Dy-120, Dy+120), range(0, 240)):
                    pix=getPixel(a, i, j)
                    PIX=getPixel(pics[x], I, J)
                    if getRed(pix)!=255 and getGreen(pix)!=255 and getBlue(pix)!=255:
                       setRGB(PIX, getRGB(pix))
        else:
            for I, i in zip(range(Dx-133, Dx+133), range(15, 280)):
                for J, j in zip(range(Dy-133, Dy+133), range(13, 278)):
                    pix=getPixel(b, i, j)
                    PIX=getPixel(pics[x], I, J)
                    if getRed(pix)!=255 and getGreen(pix)!=255 and getBlue(pix)!=255:
                        setRGB(PIX, getRGB(pix))
        Dx=Dx+10
        if x==3:
            Dx=362
        if x==4:
            Dx=378
        if x==55:
            Dx=950
        if x==56:
            Dx=964
    print("Saving Pictures...")
    savePicture(pics, "HarryCatchSnitch.gif")








