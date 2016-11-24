import requests
import regex

def parseemails( baseUrl, urlStr, allurls, allmails, reqLevel ):
	reqLevel = reqLevel + 1
	print('[{}] Url: {} '.format(reqLevel, urlStr))
	httpPage = requests.get(urlStr)
	#print('Founded emails:')
	mails = list(set(regex.findall(r'[\w\.-]+@[\w\.-]+', httpPage.text)))
	#print(mails)
	if (len(mails) > 0):
		for mail in mails:
			allmails.append(mail)
	
	rawUrls = list(set(regex.findall(r'<a href="?\'?([^"\'>]*)"', httpPage.text)))
	urls = []
	
	for url in rawUrls:
		if (url.startswith('/') or url.startswith(baseUrl) ) and ((url in allurls) == False):
			urls.append(url)
			allurls.append(url)
			#print(url)
	
	if (reqLevel < 2):
		for url in urls:
			if (url.startswith('/')):
				parseemails(baseUrl, baseUrl + url, allurls, allmails, reqLevel)
			if (url.startswith(baseUrl)):
				parseemails(baseUrl, url, allurls, allmails, reqLevel)
	
	return

allEmails = []
allUrls = []
reqLevel = 0

parseemails('https://lurkmore.to', 'https://lurkmore.to', allUrls, allEmails, reqLevel)

print('Founded emails:\n')
allEmails = list(set(allEmails))
for mail in allEmails:
	print(mail)