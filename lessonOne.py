import webapp2

form="""
<form method = "post" action= "/testform">
        	<input name="q">
        	<input type="submit">
        </form>
"""
class TestHandler(webapp2.RequestHandler):
    def get(self):
    	q = self.request.get("q")
        self.response.write(q)

        #self.response.headers['Content-Type'] = 'plain/text'
        #self.response.write(self.request)
class MainHandler(webapp2.RequestHandler):
    def post(self):
        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/testform', TestHandler)
], debug=True)