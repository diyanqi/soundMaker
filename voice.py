import os
from xpinyin import Pinyin





def  main():
	f=open("list.txt","w+")
	f.truncate()
	now=os.getcwd()
	print(os.getcwd())
	word=input()
	one_p = Pinyin()
	py = one_p.get_pinyin(word)
	path=("file '"+py.replace("-",".wav'\nfile '")+".wav'").replace("，","td").replace("。","td")\
		.replace("！","td").replace("？","td")
	print(path,file=f)
	f.close()
	os.chdir("C:\\Program Files (x86)\\UTAU\\voice\\DT")
	os.system("ffmpeg -f lavfi -t 0.5 -i anullsrc td.wav -y")
	os.system("ffmpeg -f concat -i "+now+"\\list.txt"+" -c copy "+now+"\\"+word+".fuben.wav")
	os.chdir(now)
	os.system("ffmpeg -i "+word+".fuben.wav -filter:a \"atempo=2.0\" -vn "+word+".wav")
	os.remove(word+".fuben.wav")

if __name__ == '__main__':
	main()