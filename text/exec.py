"""
編寫接口函數,從終端輸入端口名稱獲取端口運行狀態中的地址值
思路：
1.根據輸入的端口名稱找到對應的段落
2.在該段落中匹配address
"""
import re

# port=input("端口：")
def get_address(port):
    f=open('exc.txt')
    while True:#每一次跳出for循環就會得到一段的內容 也就是data
        #獲取一段內容
        data = ''  # 定義空字符串
        for line in f:#每次取一行
            if line=='\n':##如果是空白就印===
            #     print("===========")
            # print(line)
                break
            data+=line
        #data為空說明到文檔結尾
        if not data:#如果這段的內容都是空 說明文檔結束
            break
        # print(data)
        obj=re.match(port,data)#用port(字符串) 去match data (匹配開始位置)
        # 如果匹配到就會返回一個match對象 沒有的話會返回none 不然data就是目標段落
        if obj:
            # print("yes")
            # pattern=r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            pattern=r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknown"
            obj=re.search(pattern,data)#用正則表達去匹配目標段落data
            return obj.group()
    return "沒有該端口"

if __name__=='__main__':
    port=input("端口：")
    print(get_address(port))

