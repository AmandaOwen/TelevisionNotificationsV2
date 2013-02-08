import urllib
import os
import cgi
import datetime
import targetchannels
import formstrings
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
    def get(self):	
		user = users.get_current_user()
		if user:				
			#So now they're logged in we can show the channel list: 
			#which needs to be created as a form so the correct channels can be selected
	
			#This sets a list of channels that are freeview or sky, 
			#so people can select appropriate channels easily. 
			#This is done with a button that selects all checkboxes witha certain class
			#And the class is when the channels are iterated through below. 
			freeview = formstrings.GetFreeview()
			skyentertainment = formstrings.GetSky()			
			formcontent = formstrings.SelectChannelButtons() 
			
			#This is the list of channels
			#As there are 40, I've divided them up into 4 columns
			#I'll write a monitoring script that checks the radio
			#times website for channel changes (but later!). 
			formcontent += "<fieldset>"
			index = 0
			channels = targetchannels.channels
			for channel in channels:
				details = channel.split("|")
				index = index + 1
				if index==1 or index==11 or index==21 or index==31: 
					formcontent += (" \n\t\t\t\t<div class='span3'> ")
				formcontent += ("\n\t\t\t\t\t<label for='" + details[0] + "'> \n\t\t\t\t\t\t<input type='checkbox' name='channels' id='" + details[0] + "' value='" + details[1])
				if details[1] in freeview:
					formcontent += ("' class='normal freeview")	
				elif details[1] in skyentertainment:
					formcontent += ("' class='normal sky")					
				else:
					formcontent += ("' class='normal")	
				formcontent += ("' /> \n\t\t\t\t\t\t")
				formcontent += ( details[1] + "\n\t\t\t\t\t</label>")				
				if index==10 or index==20 or index==30 or index==40: 
					formcontent += (" \n\t\t\t\t</div> ")
			formcontent += "</fieldset>"
			
			#This is to add a field for a TV series to be typed
			formcontent += "<fieldset>"
			formcontent += "</fieldset>"
			
			
			
			formcontent += "\n<div class='form-actions'>\n\t<button type='submit' class='btn btn-primary'>Check for new series</button>\n</div>"
				
			#Add all this to the template
			template_values = {
				'title': "Pick the channels you would like to check",
				'lead': "Pick the channels you would like to check", 
				'formaction': "/series/", 
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