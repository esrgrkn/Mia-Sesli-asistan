# Mia-Sesli-asistan![voice](https://user-images.githubusercontent.com/92585904/166426866-bb100542-dc02-46fe-83d4-3a2ed253d73b.jpg)

<br>

[youtube]:https://www.instagram.com/gurkanesserr/?hl=tr
[twitter]:https://twitter.com/GrkanEser17
[linkedin]:https://www.linkedin.com/in/g%C3%BCrkan-eser-281819224/

## Connect with me:
[<img  width="35" src="https://unpkg.com/simple-icons@v6/icons/instagram.svg" align="center" />][youtube]
[<img  width="35" src="https://unpkg.com/simple-icons@v6/icons/twitter.svg" align="center" />][twitter]
[<img  width="35" src="https://unpkg.com/simple-icons@v6/icons/linkedin.svg" align="center" />][linkedin]

<br>

## Proje Sahibi: Gürkan ESER 
<br>

## Sesli Asistan Nedir ?
Tabletinizde, telefonunuzda, bilgisayarınızda, hoparlörünüzde veya internete bağlı herhangi bir cihazda mevcut olan kişisel asistanınız/yardımcınızdır. Son yıllarda popülaritesinin artmasıyla birlikte şimdi ki çoğu akıllı cihazda yüklü olarak geliyor.

## Peki bu sesli asistan sizin için neler yapabilir:
### •	Sizinle birebir konuşabilir, sohbet edebilir. Normal,günlük konuşmalar yapabilir.
### •	Anlık olarak saati söyleyebilir.
### •	Yılın hangi ayında ve gününde olduğunuzu size söyleyebilir
### •	İstediğiniz anda Youtube’u açabilir.
### •	O an bulunduğunuz konumu size açabilir
### •	Sizin için hava durumunu kontrol edebilir.
### •	Görüntülü ses kontrol sistemini açarak size kameradan ses seviyesini ayarlamanıza izin verir(Kamera gerekli!)
### •	“Arama yap” dediğinizde size istediğiniz aramayı yapabilir.(Web araması)
### •	Size tekerleme okuyabilir.
### •	O günün Dolar ve Euro kurunu sorgulayabilir.
### •	Sesli asistandan çıkmak için ; Kapan veya Kendini kapat diyebilirsiniz.

<br>

## Sesli Asistan Çalışma mantığı nedir ?
Sesten Metine Geçiş (Speech to Text): Kullanıcı girişini (Bu bizim durumumuzda ses dosyası olacak) metine dönüştürür.
Gürültü Azaltma Motoru: Ses dosyaları oldukça gürültülü olabilir, bu yüzden programın temiz ses çıkarması için beyaz gürültüyü filtrelemenin bir yolu olması şarttır.
Etiketleme ve Ses Tanıma: Kullanıcının talebini yerine getirmek için sistemin her sonucu belirli bir işleme etiketlemesi gerekir (Yani hava durumu sorusunu "hava durumu"). Etiketlemenin doğru olması için yapay zeka sistemi genellikle binlerce farklı veri setiyle eğitilir. Farklı soruların farklı etiketlerce nasıl sınıflandırılacağını öğrenir.

<br>

## Konuşma Tanıması (Speech Recognition) Nedir?
İlk olarak kohonen (bkz: Teuvo kohonen) adlı bir fin bilim adamı tarafından 1984'te ortaya atılmış olan ses sinyalini örnekleyip, bunların içindeki harfleri arayan ardından bunları sıraya sokup anlamlandıran yapay sinir ağı uygulamasıdır. Bazı yazılımlar seslerin sinyallerini yapay zeka modellerine eğiterek daha sonra sınıflandırma yapıyorlar.

<br>

## Asistanı kullanmadan önce Bu kütüphanelerin Çalışmaya dahil edilmesi gerekiyor.

### from calendar import month
### import time
### import webbrowser
### import speech_recognition as sr
### from gtts import gTTS
### from playsound import playsound  
### import random
### import os
### from selenium import webdriver
### import cv2 
### import mediapipe as mp
### from math import hypot
### from ctypes import cast, POINTER
### from comtypes import CLSCTX_ALL
### from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
### import numpy as np

## Bunları kurduktan sonra projeyi Asistant.py dosyası içerisinden çalıştırabilirsiniz.

