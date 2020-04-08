from pygame import mixer
from datetime import datetime
from time import time

def alarmloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as l:
        l.write(f"{msg} {datetime.now()}\n")

if __name__=='__main__':
    #alarmloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watertime = 40*60
    exetime = 30*60
    eyetime = 45*60

    while True:
        if time()-init_water > watertime:
            print("Water time. Enter 'drank' to stop the alarm.")
            alarmloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at ")

        if time()-init_eyes > eyetime:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            alarmloop('eyes.mp3', 'doneeyes')
            init_water = time()
            log_now("Eyes relaxed at ")

        if time()-init_exercise > exetime:
            print("Physical Activity time. Enter 'doneexe' to stop the alarm.")
            alarmloop('physical.mp3', 'doneexe')
            init_water = time()
            log_now("Physical activity completed at ")