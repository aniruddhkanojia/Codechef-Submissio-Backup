import re
import urllib2
print "Type Username"
#username=raw_input()
username=raw_input()
response = urllib2.urlopen('http://www.codechef.com/users/'+str(username))
html = response.read()
regex=ur"\"(.*?status.*?)\""
m = re.findall(regex,html)
c=0
t=len(m)
for i in m:
	c+=1
	response = urllib2.urlopen('http://www.codechef.com/'+str(i))
	html= response.read()
	regex=ur"<tr class=\"kol\"(.*?)tr>"
	q = re.findall(regex,html)
	regex=ur"viewsolution\/(\d{7})"
	for j in q:
		if "accepted" in j:
			
			tmp=re.findall(regex,j)
			i=i.split(',')
			i=i[0].split('/')

			lang=re.findall(ur"width=\"70\">(.*?)<",j)
			lang=lang[0]
			response = urllib2.urlopen('http://www.codechef.com/viewplaintext/'+str(tmp[0]))
			html= response.read()
			html=html.replace("&lt;","<");	
			html=html.replace("&gt;",">");	
			html=html.replace("&quot;","\"");	
			html=html.replace("&amp;","&");	
			ext=""
			lang=lang.lower()
			if("++" in lang):
				ext=".cpp"
			elif ("java" in lang):
				ext=".java"
			elif ("pyth" in lang):
				ext=".py"
			elif ("c" in lang):
				ext=".c"
			else:
				ext=".txt"
			f=open(i[-1]+ext,'w')
			f.write(html[5:-6])
			f.close()
			print i[-1]+ext + " file created (%d/%d)\n\n" % (c,t)
			break

