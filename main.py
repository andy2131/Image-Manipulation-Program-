import numpy as np
from PIL import Image  

q=str(input('Enter any key to run program (press q to exit): '))

while q!='q':
    
    imgname=str(input('Enter the image filename: '))
    option=str(input('Enter one of the following options: r(Reflection), t(Threshold), s(Save File): '))
    img=Image.open(imgname)
    img.show() 
    print('Image(width, height):',img.size)
    print('Image mode: '+img.mode)
    gryimg=img.convert('L')
    array=np.array(gryimg)
    
    def reflection(array):
        percent=int(input('Enter the percentage being reflected (Percentage<=50): '))
        dir=str((input('Enter v for reflecting vertically or h for horizontally: ')))
        if dir=='v':
            rows=int(percent*(1/100)*len(array))
            reflected=np.array(array[rows*2-1:rows-1:-1])
            rest=np.array(array[rows:])
            return np.vstack((reflected,rest))
        if dir=='h':
            columns=int(percent*(1/100)*len(array[0]))
            reflected=np.array(array[::,columns*2-1:columns-1:-1]) 
            rest=np.array(array[::,columns:])
            return np.hstack((reflected,rest))
    
    def threshold(array):
        threshold=int(input('Enter a threshold value: '))
        thresholdarray=((array>threshold)*255).astype(np.uint8)
        return thresholdarray
    
    def file(modifiedarray):
        modifiedimg=Image.fromarray(modifiedarray)
        modifiedimg.show()
        save=str(input("Enter yes to save your image (press any key if you don't want to): "))
        if save=='yes':
            name=str(input('Enter filename you want image to be saved as: '))
            modifiedimg.save(name)
            return 
        else:
            return 
        
    if option=='r':
        reflectedarray=reflection(array)
        file(reflectedarray)
         
    
    if option=='t':
        thresholdarray=threshold(array)
        file(thresholdarray)
        
        
    if option=='s':
        save=str(input("You haven't made any changes to the image yet. Enter yes to save the original image (press any key if you don't want to): "))
        if save=='yes':
            name=str(input('Enter filename you want image to be saved as: '))
            img.save(name)
    
    q=str(input('Enter any key to continue program (press q to exit): '))

 


