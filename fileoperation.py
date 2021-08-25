#Writing in file 
with open("text.txt", "w",encoding='utf-8')as f:
    f.write("to chaliye shuru krte he bina kisi backchodi ke")
    f.close()
    f = open("text.txt", "r")
print(f.read())
##Reading file
f = open('text.txt','r',encoding='utf-8')
print(f.read())
# closing opened file
f = open("text.txt", "r",encoding='utf-8')
print(f.read())
f.close()