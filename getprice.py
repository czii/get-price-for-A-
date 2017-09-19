import urllib.request
import re
import time
import socket

def geturl(url):
	timeout = 3
	socket.setdefaulttimeout(timeout)
	response = urllib.request.urlopen(url)
	html = response.read()
	return html

#数据获取部分		
def getprice(code):
	try :
		url = "http://hq.sinajs.cn/list=" + code
		html = geturl(url)
		price = re.search('hq_str([\s\S]{70})',html.decode("gbk"),flags=0).group()
		price = re.findall('\d+\.\d+',price)
		price = float(price[2])
	except :
		return("a")
	return(price)
	
##
def main(code):
	while 1:
		try :
			price = getprice(code)
			#print(code ,"=" ,"%.2f"%price)
			print("%.2f"%price)
		except :
			#print(code,end=" ")
			print("异常")
		return()
while 1:
	print(time.strftime('%H:%M',time.localtime(time.time())),end="  ")
	main("sz002457")    #股票代码填写区，上证为sh+代码，深圳为sz+代码
	time.sleep(60)      #获取间隔
