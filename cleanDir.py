import os

cleanList = ['assembledVideos','downgradedVideos','frames','modifiedFrames']

for i in cleanList:
	os.system('rm -r '+ i)
	os.system('mkdir ' + i)