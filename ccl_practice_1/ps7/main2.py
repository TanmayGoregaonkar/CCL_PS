import webapp2
import json
import urllib

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write('<html><body>'
		'<form action="/result" method="post" >'
		'<label>Zipcode</label><br>'
		'<input type="text" name="zipcode" placeholder="111111" pattern=[0-9]{6} required>'
		'<input type="submit" name="submit">'
		'</form>'
		'</body></html>'
		)
		
class Result(webapp2.RequestHandler):
	def post(self):
		zipcode = self.request.get('zipcode')
		if len(zipcode)!=6 or not zipcode.isdigit():
			self.response.write(
			'<h1>ERROR</h1>'
			'<a href="/">Goo back</a>'
			)
		
		url = 'https://api.postalpincode.in/pincode/'+str(zipcode)
		response = urllib.urlopen(url).read()
		response = json.loads(response)
		
		if response[0]['Status'] == 'Error':
			self.response.write(
			'<h1>ERROR</h1>'
			'<a href="/">Goo back</a>'
			)
		
		else:
			for p in response[0]['PostOffice']:
				self.response.write('Name : '+str(p['Name'])+'<br>')
		
		
app = webapp2.WSGIApplication([("/",MainPage),("/result",Result)],debug = True)
		
		
