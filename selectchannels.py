import urllib
import os
import cgi
import datetime
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
    def get(self):	
		user = users.get_current_user()
		if user:				
			#So now they're logged in we can show the channel list: 
			
			
			
			#Add all this to the template
			template_values = {
				'title': "Pick the channels you would like to check",
				'lead': "Pick the channels you would like to check"
			}
			path = os.path.join(os.path.dirname(__file__), 'template.html')
			self.response.out.write(template.render(path, template_values))
		else: 
			self.redirect(users.create_login_url(self.request.uri))
			
application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)
def main():
    run_wsgi_app(application)
if __name__ == "__main__":
    main()