from PIL import Image

im = Image.open('frames/8XTfqrE4CB_frames/thumb0001.jpg', 'r')

pix_val = list(im.getdata())
width, height = im.size
#print pix_val

pixelsCoordinates = { }
#x,y,[r,g,b]

for i in range(0, width):
	for j in range(0, height):
		currentCoord = str(j) + ',' + str(i)

		pixelsCoordinates[currentCoord] = pix_val[j*(width) + i]
		#print str(i) + ' ' + str(j) + ' ' + str(pix_val[j*(width) + i])

colorString = []


for i in range(0, width):
	for j in range(0, height):
		currentCoord = str(j) + ',' + str(i)
		colorString.append([int(str(pixelsCoordinates[currentCoord][0]).zfill(3))])
		colorString.append([int(str(pixelsCoordinates[currentCoord][1]).zfill(3))])
		colorString.append([int(str(pixelsCoordinates[currentCoord][2]).zfill(3))])
		#print str(i) + ' ' + str(j) + ' ' + str(pix_val[j*(width) + i])

print colorString
gay = bytes(colorString)
im = Image.frombytes("RGB", (852,480), gay)
im.save("test.jpeg", "JPEG")
'''
for i in range( 128**2 ):
    colorString += chr(255) + chr(0) + chr(0)

'''

print pixelsCoordinates['0,20']
print width
print height