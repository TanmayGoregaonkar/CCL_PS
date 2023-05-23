import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write("Hello world . PS1")
		
app = webapp2.WSGIApplication([("/",MainPage)],debug = True)

