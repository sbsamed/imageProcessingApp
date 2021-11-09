# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 19:45:59 2021

@author: Samed
"""

import cv2 
import  numpy as np
from matplotlib import pyplot as plt

#koordinatları kullanıcıdan alıyoruz
print("Koordinatları giriniz:")
r1=(int) (input("R1:"))
s1= (int) (input("S1:"))
r2= (int) (input("R2:"))
s2= (int) (input("S2:"))

#kullanıcının girmiş olduğu koordinatlara göre 3 adet doğrumuz oluşuyor
#burada, oluşan 3 adet doğrunun denklemleri bulundu  S=T(r)
def dogrudenklemi(x1,y1,x2,y2,r):
    
    m=(y2-y1)/(x2-x1) #doğruların eğimi bulundu 
    s=  (m*(r-x1)) + y1 # s burada doğru denklemimizin çıktısıdır  yani pixelimizin yeni değeri 
    return s


image = cv2.imread("lena.png") #resmimiz okundu
#kurt resmi üzerinde çalışılacaksa burası yorum satırından alınmalıdır
#image = cv2.imread("kurt.jpg") #resmimiz okundu


image_gri = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #hazır fonksiyon ile  gri tona dönüştürdük
image_output = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
image_array=np.array(image_gri) #görüntünün pixel değerlerine kolay erişmek için matrise çevirdik

#görüntüye ait matrisdeki satır ve sütun uzunlukları alındı
r=len(image_array[:,0]) 
c=len(image_array[0,:])


# aşağıdaki kod bloklarına genel olarak bakacak olursak,
# eğer  pixel değerimiz r1<pixel<r2  ise
# bu pixel değerine (r1,s1) ve (r2,s2) noktaları arasında kalan doğru denklemı uygulanır ve
# bu denklemden elde dilen çıktı output resmimizin ilgili indisine atanır


# #eğer bu 3 doğrudan eğimi belirsiz olan varsa bu kod blogu uygulanır
# yani iki noktası bilinen doğru denklemini düşünelim 
# eğer burada R2 ve R1 birbirine eşit ise eğim belirsizdir ve aşağıdaki işlem uygulanır
if(r2==r1):
    for x in range(r):
        for y in range(c):
            if(image_array[x,y]<=r1):
                image_output[x,y]=dogrudenklemi(0,0,r1,s1,image_array[x,y])
            elif(image_array[x,y]>r1):
                image_output[x,y]=dogrudenklemi(r2,s2,255,255,image_array[x,y])
                

#eğimi belirsiz olan hiçbir doğrumuz yoksa aşağıdaki işlemler uygulanır          
else:
    for x in range(r):
        for y in range(c):
            if(image_array[x,y]<=r1):
                image_output[x,y]=dogrudenklemi(0,0,r1,s1,image_array[x,y])
            elif(image_array[x,y]<=r2):
                image_output[x,y]=dogrudenklemi(r1,s1,r2,s2,image_array[x,y])
            elif(image_array[x,y]<=255):
                image_output[x,y]=dogrudenklemi(r2,s2,255,255,image_array[x,y])   


#gri tondaki input görüntümüz için histogram
plt.hist(image_gri.ravel(),256,[0,256]); plt.show()
#output görüntümüz için histogram
plt.hist(image_output.ravel(),256,[0,256]); plt.show()

#yeni oluşan görüntülerin ayrı pencerelerde açılması ,
#kodun tekrar run edilmesi için bu açılan pencerelerin kapanması gerekmektedir

cv2.imshow("GriTon",image_gri)
cv2.imshow("DogruDenklemiUygulandi_Output",image_output)
cv2.waitKey(0)
cv2.destroyAllWindows()















