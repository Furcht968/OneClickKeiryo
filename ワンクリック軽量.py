from PIL import Image
import os,sys
import shutil
if(len(sys.argv)==1):
	print("ファイルが存在しないよ！")
	input("ボタンを押してね！")
	sys.exit()
count=0
for i in sys.argv[1:]:
	count=count+1
	print(str(count)+"枚目は「"+i+"」")
	file=i
	if(os.path.exists(os.path.dirname(file)+"\Resize")==False):
		os.mkdir(os.path.dirname(file)+"\Resize")
	img=Image.open(file)
	print("キロバイトになるまでリサイズしています・・・")
	while(1):
		img_resize = img.resize((int(img.width/2), int(img.height/2)))
		img_resize.save(file.replace(".png","")+"_1.png",quality=95)
		if(int(str(os.path.getsize(file))[:3]) <= 1000):
			break
	print("クオリティーを下げています・・・")
	image=Image.open(file.replace(".png","")+"_1.png")
	image.save(file.replace(".png","")+"_2.png",quality=60)
	print("JPEG化しています・・・")
	image2=Image.open(file.replace(".png","")+"_2.png")
	image.load()
	background = Image.new("RGB", image2.size, (255, 255, 255))
	background.paste(image2, mask=image2.split()[3])
	name=file.replace(".png","")+"_軽量化.jpg"
	background.save(name,"JPEG")
	os.remove(file.replace(".png","")+"_1.png")
	os.remove(file.replace(".png","")+"_2.png")
	print(os.path.dirname(file)+"\Resize\\"+os.path.basename(name))
	if(os.path.exists(os.path.dirname(file)+"\Resize\\"+os.path.basename(name))==False):
		shutil.move(name,os.path.dirname(file)+"\Resize")
	else:
		os.remove(os.path.dirname(file)+"\Resize\\"+os.path.basename(name))
		shutil.move(name,os.path.dirname(file)+"\Resize")
	print(str(count)+"枚目完了！\n")
input("完了！\nボタンを押してね！\n")
