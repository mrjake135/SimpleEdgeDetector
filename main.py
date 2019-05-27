from PIL import Image
from PIL import ImageFilter

#simple edge detecting photo updator
def main():
	path = "image.jpg"
	img = Image.open(path)
	width, height = img.size
	#Sobel Filter
	#Find Gradient
	img = img.filter(ImageFilter.FIND_EDGES)
	img.save("image_updated.jpg")
	img.show()
if __name__ == "__main__":
	main()