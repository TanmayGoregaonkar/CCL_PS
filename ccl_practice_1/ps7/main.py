import webapp2
import urllib
import json

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
		zipcode=self.request.get('zipcode')
		
		if len(zipcode)!=6 or not zipcode.isdigit():
			self.response.write('<html><body>')
			self.response.write('<h1>Error</h1>')
			self.response.write('<a href="/">Go back form</a>')
		
			
		
		url="https://api.postalpincode.in/pincode/" + str(zipcode)
		response=urllib.urlopen(url).read()
		response=json.loads(response)
		
		if response[0]['Status']=='Error':
			self.response.write('<html><body>')
			self.response.write('<h1>Error</h1>')
			self.response.write('<a href="/">Go back form</a>')
			self.response.write('</html></body>')
		
		else:
			self.response.write("Nearest Post Offices"+"<br>")
			self.response.write("Zipcode: "+str(zipcode)+"<br>")
			
			for post_office in response[0]["PostOffice"]:
				self.response.write("Pincode: "+str(post_office["Pincode"])+"<br>")
				self.response.write("Name: "+str(post_office["Name"])+"<br>")
				self.response.write("Region: "+str(post_office["Region"])+"<br>")
				self.response.write("Division: "+str(post_office["Division"])+"<br>")
				self.response.write("State: "+str(post_office["State"])+"<br>")
				self.response.write("Country: "+str(post_office["Country"])+"<br>")
				self.response.write("BranchType: "+str(post_office["BranchType"])+"<br>")
				self.response.write("~~~~~~~~~~~~~~~~~<br>")
				self.response.write("<br>")
			
	
		

app = webapp2.WSGIApplication([("/",MainPage),("/result",Result)],debug=True)
