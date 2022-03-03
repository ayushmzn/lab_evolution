import os
import urllib.request
import cv2 as cv
path = 'G:/folder/lh3.googleusercontent.com'
os.chdir('G:/folder')
os.mkdir('hd_images')
files = os.listdir(path)
images_name = []
hd_images_link = []
for f in files:
    if f[-1: -4: -1]=='gnp':
        images_name.append(f)
for i in images_name:
    s = 'https://lh3.googleusercontent.com/' + i[ :-8]
    hd_images_link.append(s)

#for i in hd_images_link:
   # print(i)
n = 1
for i in hd_images_link:
    path = 'G:/folder/hd_images/' + str(n) + '.jpg'
    n+=1
    urllib.request.urlretrieve(i, path)
print('completed')