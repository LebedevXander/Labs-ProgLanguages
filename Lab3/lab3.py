import requests
import datetime

payload={
	'country': 'US',
	'state':'TX',
	'city': 'Houston',
	'format': 'json',
	'limited_events': 'true',
	'topic': 'softwaredev',
	'time': '0,1w',
	'radius': '100',
	'page': '0',
	'key': '8656649492580703957535c63504b'
}

r = requests.get("https://api.meetup.com/2/open_events", params=payload)
print("Status code: ", r.status_code)
response = r.json()

html_text = '<!DOCTYPE html><body>'
for meet in response['results']:
	print('***************************************')
	meet_name = meet['name']
	print(meet_name)
	html_text += '<h3>' + meet_name + '</h3>'
	
	print()
	rawtime = int(meet['time']/1000)
	meet_time = datetime.datetime.fromtimestamp(rawtime).strftime('%Y-%m-%d %H:%M:%S')
	print(meet_time)
	html_text += '<p>' + meet_time + '</p>'
	
	if 'description' in meet:
		print()
		meet_desc = meet['description']
		print(meet_desc)
		html_text += meet_desc
	
	meet_venue = meet['venue']
	if meet_venue != 'undefined':
		print()
		meet_address = meet_venue['city'] + ', ' + meet_venue['address_1'] + ', ' + meet_venue['name']
		print(meet_address)
		html_text += '<p>' + meet_address + '</p>'
	print('***************************************')
html_text += '</body>'

text_file = open("pygen.html", "w")
text_file.write(html_text)
text_file.close()