from ast import Delete
from cmath import rect
import pygame
import sys
import time
import random


#Paketlerimizi başlattık
pygame.init()


#EKRAN
ekran_genisligi=500
ekran_yuksekligi=700
ekran=pygame.display.set_mode((ekran_genisligi,ekran_yuksekligi))
pygame.display.set_caption("ARABA OYUNU")

#RENKLER
turkuaz=(175,238,238)
kırmızı=(255,0,0)
gri=(81,80,81)
siyah=(0,0,0)

#SESLER
para_sesi=pygame.mixer.Sound("para_sesi_kısa.mp3")
kaza_sesi=pygame.mixer.Sound("kaza_sesi.mp3")
iyilesme_sesi=pygame.mixer.Sound("ana_iyilesme.mp3")
kaybetme_sesi=pygame.mixer.Sound("kaybetme_sesi_kesilmiş.mp3")


#ARABA
araba=pygame.image.load("main_araba.png")
araba=pygame.transform.scale(araba,(70,70))
araba_kordinat=araba.get_rect()
arabakonum_x=208
arabakonum_y=600
araba_kordinat.topleft=(arabakonum_x,arabakonum_y)

#YOL
yol=pygame.image.load("yol.gif")
yol=pygame.transform.scale(yol,(500,700))
yol_kordinat=yol.get_rect()
yol_kordinat.topleft=(0,0)

#DÜŞMAN ARABA
düsman=pygame.image.load("düsmanArabası.png")
düsman=pygame.transform.scale(düsman,(70,70))
düsman_konum=düsman.get_rect()

#PARA
para=pygame.image.load("dollar.png")
para=pygame.transform.scale(para,(30,30))
para_konum=para.get_rect()

#CAN İÇİN KALP
kalp=pygame.image.load("heart.png")
kalp=pygame.transform.scale(kalp,(30,30))
kalp_konum=kalp.get_rect()

#FONT AYARLARI
FONT=pygame.font.SysFont("arial",40)
font2=pygame.font.SysFont('impact',60)


#SKOR
SKOR=0
#CAN
CAN=3

#FPS ayarlama
hiz=10
saat=pygame.time.Clock()
FPS=27


#gelen paraları random oluşturma
gelen_paralar=[]
for i in range(5):
    x=random.randint(65,410)   
    y=random.randint(-500,0)
    gelen_paralar.append([x,y])


#gelen düşman arabaları oluşturma
düşman_araba_listesi=[]
for i in range(3):
    x=random.randint(65,390)   
    y=random.randint(-500,0)
    düşman_araba_listesi.append([x,y])

#CAN sayısını artırmak için oluşturduğumuz kalplerin listesini oluşturuyoruz
gelen_kalpler=[]
for i in range(1):
    x=random.randint(65,410)   
    y=random.randint(-500,0)
    gelen_kalpler.append([x,y])


clock=pygame.time.Clock()

calistir =True

#  ************** ANA DÖNGMÜZ ****************
while calistir:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    ekran.blit(yol,yol_kordinat)
    ekran.blit(araba,(araba_kordinat))

    skor_YAZI=FONT.render("SKOR:"+ str(SKOR),True,kırmızı,turkuaz)
    skor_YAZI_kordinat=skor_YAZI.get_rect()
    skor_YAZI_kordinat.topleft=(10,10)

    can_YAZI=FONT.render("CAN:"+ str(CAN),True,kırmızı,turkuaz)
    can_YAZI_kordinat=can_YAZI.get_rect()
    can_YAZI_kordinat.topleft=(385,10)

    oyun_bitti=font2.render("OYUN BİTTİ!!!SKOR:"+str(SKOR),True,kırmızı,siyah)
    oyun_bitti_kordinat=oyun_bitti.get_rect()
    oyun_bitti_kordinat.topleft=(ekran_genisligi/2,ekran_yuksekligi/2)
  
    pygame.draw.line(ekran,gri,(0,65),(500,65),2)
    ekran.blit(skor_YAZI,skor_YAZI_kordinat)
    ekran.blit(can_YAZI,can_YAZI_kordinat)

    #para için for döngüsü
    for i in range(len(gelen_paralar)):
       # circle=pygame.draw.circle(ekran,kırmızı,gelen_paralar[i],10)
        para_konum=gelen_paralar[i]
        
        
        ekran.blit(para,para_konum)
        gelen_paralar[i][1]+=4  #gelen paranın geliş hızı
        if gelen_paralar[i][1]>ekran_yuksekligi:
            y=random.randrange(-60,-10)
            gelen_paralar[i][1]=y
            x=random.randrange(65,410)
            gelen_paralar[i][0]=x
            

        if araba_kordinat.colliderect((gelen_paralar[i][0],gelen_paralar[i][1],30,30)):
            SKOR+=1
            para_sesi.play()
            gelen_paralar[i][0]=random.randrange(65,410)
            gelen_paralar[i][1]=random.randrange(-60,10)


    #gelen kalpler için for döngüsü
    for i in range(len(gelen_kalpler)):
       # circle=pygame.draw.circle(ekran,kırmızı,gelen_paralar[i],10)
        kalp_konum=gelen_kalpler[i]
        
        
        ekran.blit(kalp,kalp_konum)
        gelen_kalpler[i][1]+=4  #gelen kalbin geliş hızı
        if gelen_kalpler[i][1]>ekran_yuksekligi:
            y=random.randrange(-60,-10)
            gelen_kalpler[i][1]=y
            x=random.randrange(65,410)
            gelen_kalpler[i][0]=x
            

        if araba_kordinat.colliderect((gelen_kalpler[i][0],gelen_kalpler[i][1],30,30)):
            CAN+=1
            iyilesme_sesi.play()
            gelen_kalpler[i][0]=random.randrange(65,410)
            gelen_kalpler[i][1]=random.randrange(-60,10)


    #düşman arba için for döngüsü
    for i in range(len(düşman_araba_listesi)):
       
        düsman_konum=düşman_araba_listesi[i]
        
        
        ekran.blit(düsman,düsman_konum)
        düşman_araba_listesi[i][1]+=7   #gelen düşman arabanın geliş hızı
        if düşman_araba_listesi[i][1]>ekran_yuksekligi:
            y=random.randrange(-400,-10)
            düşman_araba_listesi[i][1]=y
            x=random.randrange(65,390)
            düşman_araba_listesi[i][0]=x
            

        if araba_kordinat.colliderect((düşman_araba_listesi[i][0],düşman_araba_listesi[i][1],70,70)):
            CAN-=1
            kaza_sesi.play()
            düşman_araba_listesi[i][0]=random.randrange(65,390)
            düşman_araba_listesi[i][1]=random.randrange(-400,-10)
            if(CAN==0):
                 oyun_bitti=font2.render("OYUN BİTTİ!!!",True,kırmızı,siyah)
                 oyun_bitti_kordinat=oyun_bitti.get_rect()
                 oyun_bitti_kordinat.topleft=(95,300)
                 sonuc=font2.render("SKOR:"+str(SKOR),True,kırmızı,siyah)
                 sonuc_kordinat=sonuc.get_rect()
                 sonuc_kordinat.topleft=(95,300)
                 kaybetme_sesi.play()
                 ekran.blit(oyun_bitti,oyun_bitti_kordinat)
                 ekran.blit(sonuc,(160,390))
                 pygame.display.update()
                 pygame.time.delay(4000)
                 calistir=False
                    
    tus=pygame.key.get_pressed()

    if tus[pygame.K_LEFT] and araba_kordinat.left>65:
        araba_kordinat.x-=hiz

    elif tus[pygame.K_RIGHT] and araba_kordinat.right<ekran_genisligi-62:
        araba_kordinat.x+=hiz
   
    saat.tick(FPS)
    pygame.display.update()   