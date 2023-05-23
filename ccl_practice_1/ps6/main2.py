import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		a,b = 0,1;
		self.response.write(str(a)+'<br>'+str(b)+'<br>')
		for i in range(6) :
			curr = a+b
			self.response.write(str(curr)+'<br>')
			a = b
			b = curr

app = webapp2.WSGIApplication([('/',MainPage)],debug = True)
