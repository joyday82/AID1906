"""
創建兩個進程
分別複製一個文件的上和下半部份到新的文件中
"""

from multiprocessing import Process
import os

filename='./face.jpeg'
size=os.path.getsize(filename)#先獲取圖片大小

#複製上半部份
def top():
    fr=open(filename,'rb')#圖片 所以用rb
    # 上面這行可放到11行當父進程 但父進程創建fr 兩個子進程使用這個fr會相互影響
    # 在父進程中創建對象的：消息隊列,管道 子進程用父進程的對象使用
    fw=open('top.jpg','wb')#取新的名字 用wb打開
    n=size//2#圖片一半的大小
    fw.write((fr.read(n)))#寫入
    fr.close()
    fw.close()

#複製下半部份
def bot():
    fr = open(filename, 'rb')
    fw = open('bot.jpg', 'wb')
    # 打開時文件在開頭 要把位置移到中間才能往後讀
    fr.seek(size//2,0)#0是開頭 以開頭為基準 0是默認值不寫也可以 向後移動
    fw.write(fr.read())#默認直接讀到結尾
    fr.close()
    fw.close()

# 把他們都變成進程
p1=Process(target=top)
p2=Process(target=bot)
p1.start()
p2.start()
p1.join()
p2.join()