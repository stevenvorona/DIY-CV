import os
import random
import string

def breakDownVideo(origVideo, fps):
	#Generates random output name and processes 480p, x fps video to downgradedVideos/foo.mp4
	randomName = str(''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)]))
	downResStr = 'ffmpeg -i rawVideos/' + origVideo + ' -s hd480 -c:v libx264 -r '+ fps +' -crf 23 -c:a aac -strict -2 downgradedVideos/' + randomName + '.mp4'
	os.system(downResStr)

	#extracts all frames to frames/foo.jpg
	framesFolderName = randomName + '_frames'
	os.system('mkdir frames/' + framesFolderName)
	extractAllFrames = 'ffmpeg -i downgradedVideos/' +randomName+ '.mp4 frames/' + framesFolderName +'/thumb%04d.jpg -hide_banner'
	os.system(extractAllFrames)

	print 'Frames saved in ' + randomName + '_frames'
	return randomName

def assembleVideo(randomName, fps):
	#finds frames and builds video into assembledVideos/foo.mp4
	framesFolderName = randomName + '_frames'
	assembleStr ='ffmpeg -framerate ' + fps + ' -i frames/' + framesFolderName + '/thumb%04d.jpg assembledVideos/' + randomName + '.mp4'
	os.system(assembleStr)
	return 'Saved output video as assembledVideos/' + randomName + '.mp4'


origVideo = raw_input("Name of original video (with extension): ")
fps = raw_input("Input frames per second as integer: ")

fileName = breakDownVideo(origVideo, fps)
print assembleVideo(fileName, fps)