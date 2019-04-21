import os
import random
import string

origVideo = raw_input("Name of original video (with extension): ")
fps = raw_input("Input frames per second as integer: ")

#Generates random output name and processes video to 480p mp4
randomName = str(''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)]))
downResStr = 'ffmpeg -i rawVideos/' + origVideo + ' -s hd480 -c:v libx264 -r '+ fps +' -crf 23 -c:a aac -strict -2 finalVideos/' + randomName + '.mp4'
os.system(downResStr)

#extracts all frames to a new folder in the frames folder
framesFolderName = randomName + '_frames'
os.system('mkdir frames/' + framesFolderName)
extractAllFrames = 'ffmpeg -i finalVideos/' +randomName+ '.mp4 frames/' + framesFolderName +'/thumb%04d.jpg -hide_banner'
os.system(extractAllFrames)

print('Frames saved in ' + randomName + '_frames')