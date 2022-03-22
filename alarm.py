#Necessary module pygame#
from time import localtime
from pygame import mixer

H = input("set the hour you want to wake up")

M = input("set the minutes you want to wake up")

while True:
	if localtime().tm_hour ==int(H) and localtime ().tm_min==int(M):
		print("Wake up")
		mixer.init()
		mixer.msic.load("#music name + .extension#")
		mixer.music.play
		break
