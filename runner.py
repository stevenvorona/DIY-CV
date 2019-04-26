import os
import random
import string
import pprint
from PIL import Image

def breakDownVideo(origVideo, fps):
	#Generates random output name and processes 480p, x fps video to downgradedVideos/foo.mp4
	randomName = str(''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)]))
	downResStr = 'ffmpeg -i ' + origVideo + ' -s hd480 -c:v libx264 -r '+ fps +' -crf 23 -c:a aac -strict -2 downgradedVideos/' + randomName + '.mp4'
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
	assembleStr ='ffmpeg -r ' + fps + ' -i modifiedFrames/' + framesFolderName + '/thumb%04d.jpg assembledVideos/' + randomName + '.mp4'
	# ffmpeg -r 60 -f image2 -s 1920x1080 -i pic%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p test.mp4
	os.system(assembleStr)
	return randomName + '.mp4'
#/home/steven/projects/diy_motion_tracker/modifiedFrames
#def comparePixels(pixel_1data, pixel_2data):

def manipulateImagePixels(randomName):
	framesFolderName = randomName + '_frames'
	os.system('mkdir modifiedFrames/' + framesFolderName)
	for filename in os.listdir('frames/'+framesFolderName):
		file, extension = os.path.splitext(filename)
		im = Image.open('frames/'+framesFolderName+'/'+filename, 'r')
		pix = im.load()
		pix_val = list(im.getdata())
		width, height = im.size
		for i in range(0, width):
			for j in range(0, height):
				currentRGBList = list(pix_val[j*(width) + i])
				currentRGBList[2] = 255
				pix[i,j] = tuple(currentRGBList)
		im.save('modifiedFrames/'+framesFolderName+'/'+filename, "JPEG")
	return 'modifiedFrames/' + framesFolderName
'''
from PIL import Image

'''

videoData = { }

videoData['originalVideo'] = 'rawVideos/' + str(raw_input("Name of original video (with extension): "))
videoData['fps'] = raw_input("Input frames per second as integer: ")
videoData['assignedKey'] = breakDownVideo(videoData['originalVideo'], videoData['fps'])
videoData['downGradedVideo'] = 'downgradedVideos/' + videoData['assignedKey'] + '.mp4'
videoData['framesFolder'] = 'frames/' + videoData['assignedKey'] + '_frames'
videoData['modifiedFramesFolder'] = manipulateImagePixels(videoData['assignedKey'])



videoData['assembledVideo'] = 'assembledVideos/' + assembleVideo(videoData['assignedKey'], videoData['fps'])

pprint.pprint(videoData)

#output info about video


#manipulateImagePixels('7KmGQwCy1E')