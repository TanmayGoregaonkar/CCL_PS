import webapp2
class MainPage(webapp2.RequestHandler):
	def get (self):
		for i in range(1,11):
			self.response.write("5 X "+str(i)+"="+str(5*i)+"<br>")
			

app = webapp2.WSGIApplication([('/',MainPage)] , debug = True)
