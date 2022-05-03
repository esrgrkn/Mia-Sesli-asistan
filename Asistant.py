from calendar import month
import time
import webbrowser
import speech_recognition as sr

from gtts import gTTS
from playsound import playsound  
import random
import os
from selenium import webdriver
import cv2 
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
hello_m = ["Selam Mia","selam mia","mia","Selam mia","Mia","Mia oradamasın","Hey Mia","hey mia","miyav"]
hello=["selam","Selam","Merhaba mia","Merhaba Mia","merhaba Mia","merhaba mia","Merhaba sesli asistan","merhaba sesli asistan","Merhaba nasılsın","Merhaba Mia nasılsın","Merhaba Nasılsın"]
situation_sentences = ["nasılsın","Nasılsın","Nasılsın Sesli asistan","naber","Naber","ne haber","Ne haber","napıyorsun","ne yapıyorsun","Napıyorsun","nasıl gidiyor","Nasıl gidiyor","napıyon","Napıyon","nasıl","nabıyon","naptı","Merhaba nasılsın"]
compliment = ["mükemmelsin","çok iyisin","mükemmel","efsane","saol","teşekkürler","teşekkür ederim","çok","iyi","çok iyi"]
returnn = ["iyiyim sen","çok iyiyim","İyiyim teşekkür ederim","iyiyim teşekkür ederim","bende iyiyim"]
returnn_ = ["biraz keyifsizim","kötüyüm","iç güvesinden hallice",]
hour = ["sesli Asistan saat kaç","saat kaç","kaç","Saat kaç","kaç saat","zaman"]
how_month = ["Bugün ayın kaçı","ayın","kaçı","günler","bu gün ayın"]
maps = ["neredeyim","Burası neresi","burası neresi","neresi burası","nerda","nerde","neresi"]
volume_level = ["sesi kontrol etmek istiyorum","sesi ayarla","sesi ayarlamak istiyorum","el ile sesi kontrol etmek istiyorum"]
searchh = ["arama yap","Arama yap","arama yaparmısın","Arama yaparmısın"]
playyoutube = ["Yutubu aç","Youtube aç","yutubu aç","youtube aç","YouTube'u aç"]
tempature = ["Bugün hava kaç derece","Bugün hava nasıl","derece","hava","kaç","hava kaç","sıcaklık kaç","sıcaklık","hava durumu"]
dolars = ["Bu gün dolar ne kadar","dolar ne kadar","Dolar ne kadar","dolar kuru"]
euros = ["Bu gün euro ne kadar","euro ne kadar","Euro ne kadar","euro kuru","Euro kurunu aç"]
closed = ["Tamam kapan","tamam kapan","Tamam Kendini kapat","uyu","kendini kapat","tamam","Tamam"],
was_born = ["Nerede doğdun","doğum yerin neresi","nerede yaratıldın"]
rhyme = ["tekerleme","bana tekerleme okur musun","bana bir tekerleme oku","bana tekerleme okurmusun"]
news = ["Haberleri aç","Haberleri açarmısın","haberleri aç","haberleri açarmısın","bu gün neler oldu","Bu gün neler oldu","gündemde neler var","haberlerrfgdf"]


descriptive = sr.Recognizer()

def record ():
    
    with sr.Microphone() as source: 
        
        audio = descriptive.listen(source) 
        
        voice = ''
        try: 
            voice = descriptive.recognize_google(audio, language='tr')
        except sr.UnknownValueError:
            speak("Ne söylediğini tam anlamadım")
        except sr.RequestError:
            speak("Sistem çalışmıyor")
            exit()
            
        return(voice)


def response(voice):
    if voice in hello_m:
        list_m = ["benden mi bahsettin","seni dinliyorum","evet benim"]
        speak(random.choice(list_m))
    if voice in hello:
        speak("dinliyorum")
    if voice in situation_sentences:
        list_s=['Sorduğun için teşekkür ederim umarım sende iyisindir','Gayet iyiyim teşekkür ederim seni sormalı','İyiyim teşekkür ederim ya sen ?','fena değilim sorduğun için teşekkür ederim umarın sende iyisindir']
        speak(random.choice(list_s))
    if voice in compliment:
        speak("Çok mütevazisin")
    if voice in returnn:
        list_r=['Bu beni mutlu etti',"Bu beni sevindirdi","harika!","Bunu duymak çok güzel"]
        speak(random.choice(list_r))
    if voice in returnn_:
        list_rr=['Buna üzüldüm',"Bu beni üzdü","Çok üzücü","Bunu duymak kötü"]
        speak(random.choice(list_rr))
    if voice in hour:
        from datetime import datetime
        speak(datetime.now().strftime('%H:%M:%S'))
    if voice in how_month:
        import datetime
        speak(datetime.date.today().strftime("%Y:%B:%A"))
    if voice in maps:
        driver=webdriver.Chrome()
        list=['Konumunu açıyorum','Konum açılıyor','Haritadann konumunuz açılıyor','Hemen size yardımcı oluyorum ']
        speak(random.choice(list))
        time.sleep(2)
        driver.get("https://www.google.com/maps/place/%C3%87anakkale,+%C3%87anakkale+Merkez%2F%C3%87anakkale/@40.1305531,26.3920735,13z/data=!3m1!4b1!4m5!3m4!1s0x14b1a9d8214a2f3f:0x8cebeb3703e22f7f!8m2!3d40.14672!4d26.408587")
        input("")  
    if voice in volume_level :
        
        speak("Sistem açılıyor")
        cameras = cv2.VideoCapture(0)#Bilgisayar üzerindeki kameraları algılar kameranız tek ise (0) eğer kameranız 1 den fazla ise (1) olmalı
        
        mpHands = mp.solutions.hands 
        hands = mpHands.Hands()
        mpDraw = mp.solutions.drawing_utils
        
        
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        
        volMin,volMax = volume.GetVolumeRange()[:2]
        
        while True:
            success,img = cameras.read()#Gelen frame leri yakalamak için
            imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#Yakalanan resim buraya gönderiliyor 
            results = hands.process(imgRGB)
        
            lmList = []
            if results.multi_hand_landmarks:
                for handlandmark in results.multi_hand_landmarks:
                    for id,lm in enumerate(handlandmark.landmark):
                        h,w,_ = img.shape
                        cx,cy = int(lm.x*w),int(lm.y*h)
                        lmList.append([id,cx,cy])
                    mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)
            
            if lmList != []:
                x1,y1 = lmList[4][1],lmList[4][2]
                x2,y2 = lmList[8][1],lmList[8][2]
        
                cv2.circle(img,(x1,y1),4,(255,0,0),cv2.FILLED)
                cv2.circle(img,(x2,y2),4,(255,0,0),cv2.FILLED) 
                cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)
        
                length = hypot(x2-x1,y2-y1)
        
                vol = np.interp(length,[5,220],[volMin,volMax])
                print(vol,length)
                volume.SetMasterVolumeLevel(vol, None)
        
                # Hand range 15 - 220
                # Volume range -63.5 - 0.0
                
            cv2.imshow('Image',img)
            if cv2.waitKey(1) & 0xff == ord('ç'):#Çıkış için "ç" tuşu kullanılabilir
                break

    if voice in searchh:
        speak("Senin için ne aramamı istersin")
        search = record() 
        print(search)
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak(search + 'Arama için bulduklarım şöyle')
    if voice in playyoutube:
        speak("Youtube açılıyor")
        
        driver=webdriver.Chrome()
        driver.get("https://www.youtube.com/")
        time.sleep(3)
        input("")
    if voice in tempature:
        speak("bu günün hava durumu açılıyor")
        driver=webdriver.Chrome()
        driver.get("https://www.google.com/search?q=bug%C3%BCn+hava+ka%C3%A7+derece&oq=bu+g%C3%BCn+hava+ka%C3%A7&aqs=chrome.1.69i57j0i10l9.4539j1j4&sourceid=chrome&ie=UTF-8")
        input("")
    if voice in closed:
        list_c = ['Görüşürüz o halde','Kendine iyi bak','Tekrar görüşmek dileğiyle']
        speak(random.choice(list_c))
        exit()
    if voice in dolars:
        listd = ["Senin için dolar kuruna bakıyorum","Dolar kuru açılıyor","Doların durumu şöyle"]
        speak(random.choice(listd))
        url = "https://www.google.com/search?q=dolar+kuru&oq=dolar+kuru&aqs=chrome..69i57j0i131i433i512j0i512j0i131i433i512l4j0i512l3.1451j1j9&sourceid=chrome&ie=UTF-8"
        webbrowser.get().open(url)
    if voice in euros:
        listd = ["Senin için euro kuruna bakıyorum","euro kuru açılıyor","euro durumu şöyle"]
        speak(random.choice(listd))
        url = "https://www.google.com/search?q=euro+kuru&oq=euro+kuru&aqs=chrome..69i57j0i131i433i512j0i512j0i131i433i512j0i512l6.2036j1j9&sourceid=chrome&ie=UTF-8"
        webbrowser.get().open(url)
    if voice in was_born:
        speak("Türkiyede bir Türk Yazılım geliştirici tarafından geliştirildim ve geliştirilmye devam ediyorum")
    if voice in rhyme:
        list_rh = ["Az gittim uz gittim.Dere tepe düz gittim.Çayır çimen geçerek,Lale sümbül biçerek,Soğuk sular içerek,Altı ayla bir güzde,Bir arpa boyu yol gittim.",
        "Adem madene gitmiş.Adem madende badem yemiş.Madem ki Adem madende badem yemiş,Niye bize getirmemiş.","İğne miğne ucu düğme Fil filince kuş dilince Horoz öttü,tavuk tepti Bülbül kızı selam etti Selamına dua etti Al çık bal çık Sana dedin sen çık"]
        speak(random.choice(list_rh))
        list_tired = ["Tekerleme okumak da yorucu iş","Oh çok yoruldum","Nefesim bitiyordu azda kalsın"]
        speak(random.choice(list_tired))
    if voice in news:
        listd = [" senin için haberlere bakıyorum","haberleri açıyorum","Haberler açılıyor"]
        speak(random.choice(listd))
        url = "https://www.google.com/search?q=son+dakika+haberleri&sxsrf=ALiCzsbwTyi067139Ujb-iQ2nD21mmTjjA%3A1651214700723&ei=bIlrYvTjK_2Vxc8PxdCckAE&oq=son+dakika&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQsAMQJzIHCCMQsAMQJzIHCCMQsAMQJ0oECEEYAEoECEYYAFAAWABgjwpoAXABeACAAQCIAQCSAQCYAQDIAQPAAQE&sclient=gws-wiz"
        webbrowser.get().open(url)
        input("")

         


try:
    def speak(string):
        tts = gTTS(string , lang='tr')
        randomd= random.randint(1,1000)
        file = 'audio-' + str(randomd) + '.mp3'
        tts.save(file)
        playsound(file)
        os.remove(file)
except:
    print("Üzgünüm birşeyler ters gitti")


time.sleep(1)
while 1 :
    voice = record()
    print(voice)
    response(voice)
    
    




   