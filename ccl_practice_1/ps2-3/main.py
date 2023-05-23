import webapp2
class MainPage(webapp2.RequestHandler):
	def get(self):
		for i in range(5):
			self.response.write("Name : Tanmay Goregaonkar<br>Roll no : 33227 <br> Seat No. T190058570<br>")
			self.response.write("~~~~~~~~~~~~~~~~~~~~~~~~~<br>")		

		self.response.write("<hr>")				
		self.response.write("Using while loop")
		self.response.write("<hr>")	
		var = 5;
		while(var):
			
			self.response.write("Name : Tanmay Goregaonkar<br>Roll no : 33227 <br> Seat No. T190058570<br>")
			self.response.write("~~~~~~~~~~~~~~~~~~~~~~~~~<br>")		
			var-=1
			

app = webapp2.WSGIApplication([('/',MainPage)],debug = True)
