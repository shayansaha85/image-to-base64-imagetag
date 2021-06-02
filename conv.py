import base64
import os

os.system("mkdir html")

# You have to enter the path of the folder which contains your all image files in any format (jpg/jpeg/png/webp)
# For trying it you can use the sample images folder of this directory

pathOfImageFolder = input("Enter the folde path of the images : ")
imagesname = os.listdir(pathOfImageFolder)

k=1

for x in imagesname:
    with open(f"{pathOfImageFolder}/{x}", "rb") as img:
        encode = base64.b64encode(img.read()).decode('utf-8')
    base64code = 'data:image/png;base64,{}'.format(encode)
    file = open(f"./html/{x.split('.')[0]}.html", "w")

    htmlBody = f'''<img height="500", width="500", src="{base64code}">'''

    file.write(htmlBody)
    print(f"Image #{k} done")
    k=k+1
    file.close()