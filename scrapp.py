print "Author:pratikone"
print "********************************"
print "XKCD Scrapp-py"
from BeautifulSoup import BeautifulSoup
import urllib2
str="http://www.xkcd.com"
page=urllib2.urlopen(str)
soup=BeautifulSoup(page)
import os

if not os.path.exists(os.getcwd()+"/xkcd"):
	os.mkdir(os.getcwd()+"/xkcd")
os.chdir(os.getcwd()+"/xkcd")

prev=""
for  i in range(10):
	page=urllib2.urlopen(str+prev)
	soup=BeautifulSoup(page)
        print prev
	img=soup('img')[1]
        print img['alt']
        pic_src=img['src']
        
        #saving into a folder
        #opening page to read image into a file
        opene1=urllib2.build_opener()
	page1=opene1.open(pic_src)
	my_picture=page1.read()
	
	#print my_picture
	fname=soup.h3.renderContents()
	fname=fname[45:]  #[-5:] fails for non 3-digit numbers (bug removed)
	filename=os.getcwd()+fname.encode('ascii')
	filename=filename[0:len(filename)-1]+".png"
	print filename
	fout=open(filename,"wb")
	fout.write(my_picture)
	fout.close()
        #prev image
	prev=soup.findAll(accesskey="p")[0]['href']
	print i
	

print "Done"
