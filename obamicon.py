from PIL import Image
#Open the image. Image is in same folder as this file.
im=Image.open("jolisa.jpg")
#Display the image
im.show()
turquoise=(40,200,120)
purple= (100,40,200)
yellow= (160,160,0)
brown=(230,50,230)



#get the rgb date from the image
image_data= im.getdata()
#put rgb data into list
image_data_list=list(image_data)

#this will be my new picture
new_image=[]

#for every pixel in image_data_list:
#  determine which of the four colors it will be
#  add that color to my new_image list

for pixel in image_data_list:
    # pixel is in format (R,G,B,)-a 4 tuple of numbers
    intensity= pixel [0] + pixel[1]+ pixel[2]
    #determine which of the four colors to do
    if intensity >=700 and < 840:
        #new_val= (255-pixel[0], 255-pixel[1], 255-pixel[2])
        new_image.append(yellow)
    if intensity >=382 and < 700:
        #new_val= (255-pixel[0], 255-pixel[1], 255-pixel[2])
        new_image.append(brown)
    if intensity >=840:
        #new_val= (255-pixel[0], 255-pixel[1], 255-pixel[2])
        new_image.append(purple)
    if intensity >=180 and < 382:
        #new_val= (255-pixel[0], 255-pixel[1], 255-pixel[2])
        new_image.append(turquoise)    
#create new image
#Image.new(mode,size)
my_image= Image.new(im.mode,im.size)
#put my new list of rgb values into the image
my_image.putdata(new_image)
#show image
my_image.show()
#save image

#my_image.save("jolisa.jpg","JPG")
