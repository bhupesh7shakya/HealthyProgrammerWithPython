#make sure to make health  file and insert Kalimba.ogg music to same folder as ur program is saved 
from pygame import mixer
from datetime import datetime
import time
startedtime=time.time()
totalwater=8
mixer.init()
mixer.music.load("Kalimba.ogg")
eyes=45*60
water=25*60
excercise=60*60
while True:
    # hour variable gives the curent time in hours
    initial=time.time()
    hour=datetime.now().hour
    timer=int(time.time()-startedtime)
    time.sleep(1)
    print("timer: ",timer," second")
    if hour >= 9 and hour <= 19:1
    
        if timer == water:
            water+=25*60
            initial=time.time()
            print(int(initial))
            print("Hellow sir Its first time to drink water")
            mixer.music.play()
            print("Playing.....")
            user_input=input("Press 1 if drink the water else press 0 and then press enter")
            while True:
                if user_input=="1":
                    drank_at=datetime.now()
                    mixer.music.stop()
                    print("Stopping")
                    logfile=open("health","a")
                    logfile.write(f"You have drank water at {drank_at} and 240ml")
                    endingtime=time.time()-initial
                    print(endingtime)
                    break
                elif user_input=="0":
                    mixer.music.stop()
                    print("It will remind you in one minutes")
                    time.sleep(2)
                    mixer.music.play()
                    user_input=input("Press 1 if drink the water else press 0 and then press enter")      
        if timer==eyes:
            eyes+=45*60
            initial=time.time()
            print(int(initial))
            # time.sleep(30)
            playingtime=time.time()-initial
            print(playingtime)
            print("Hellow sir Its first time to excercise")
            mixer.music.play()
            print("Playing.....")
            user_input=input("Press 1 if eye excercise else press 0 and then press enter")
            while True:
                if user_input=="1":
                    drank_at=datetime.now()
                    mixer.music.stop()
                    print("Stopping")
                    logfile=open("health","a")
                    logfile.write(f"You have drank water at {drank_at} l")
                    endingtime=time.time()-initial
                    print(endingtime)
                    break
                elif user_input=="0":
                    mixer.music.stop()
                    print("It will remind you in one minutes")
                    time.sleep(60)
                    mixer.music.play()
                    user_input=input("Press 1 if drink the excersie else press 0 and then press enter")
        if timer==excercise:
            excercise+=60*60
            initial=time.time()
            # time.sleep(130)
            print(int(initial))
            playingtime=time.time()-initial
            print(playingtime)
            print("Hellow sir Its first time to excercose ")  
            mixer.music.play()
            print("Playing.....")
            user_input=input("Press 1 if excercose   else press 0 and then press enter")
            while True:
                if user_input=="1":
                    excercise_at=datetime.now()
                    mixer.music.stop()
                    print("Stopping")
                    logfile=open("health","a")
                    logfile.write(f"You have excercose  {excercise_at}")
                    endingtime=time.time()-initial
                    print(endingtime)
                    break
                elif user_input=="0":
                    mixer.music.stop()
                    print("It will remind you in one minutes")
                    time.sleep(60)
                    mixer.music.play()
                    user_input=input("Press 1 if excercise else press 0 and then press enter")           
        timer=0
    else:
        timer=0
