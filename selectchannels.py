import urllib
import os
import cgi
import datetime
import targetchannels
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
    def get(self):	
		user = users.get_current_user()
		if user:				
			#So now they're logged in we can show the channel list: 
			#which needs to be created as a form so the right channels can be selected
			formcontent = ""
			index = 0
			channels = targetchannels.channels
			for channel in channels:
				details = channel.split("|")
				index = index + 1
				if index==1 or index==11 or index==21 or index==31: 
					formcontent += (" <div class='span3'> ")
				formcontent += ("\n\t\t\t<label for='" + details[0] + "'> \n\t\t\t<input type='checkbox' name='channels' id='" + details[0] + "' value='" + details[1] + "' /> ")
				formcontent += ( details[1] + " </label>")				
				if index==10 or index==20 or index==30 or index==40: 
					formcontent += (" </div> ")
			#Now we need to set up some buttons to: 
			#Select all
			#Select freeview
				
			#Add all this to the template
			template_values = {
				'title': "Pick the channels you would like to check",
				'lead': "Pick the channels you would like to check", 
				'formaction': "something", 
				'formcontent': formcontent
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