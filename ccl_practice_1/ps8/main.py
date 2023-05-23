# -*- coding: utf-8 -*-
import webapp2
import urllib2
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
                self.response.write('<html><body>')
                self.response.write('<form action="/forecast" method="post">')
                self.response.write('Latitude: <input type="text" name="lat"><br>')
        
                self.response.write('Longitude: <input type="text" name="lon"><br>')
                self.response.write('Forecast Type: <select name="type">')
                self.response.write('<option value="temperature_2m">Hourly</option>')
                self.response.write('<option value="daily">Daily</option>')                        
                self.response.write('</select><br>')
                self.response.write('<input type="submit" value="Search">')
                self.response.write('</form></body></html>')

class ForecastHandler(webapp2.RequestHandler):
    def post(self):
            lat = self.request.get('lat')
            lon = self.request.get('lon')
            forecast_type = self.request.get('type')

            
            url = 'https://api.open-meteo.com/v1/forecast?latitude='+lat+'&longitude='+lon+'&hourly='+forecast_type
            
                  #url = 'https://api.open-meteo.com/v1/forecast?latitude='+lat+'&longitude='+lon+'&daily=temerature_2m'
                  
            #print(url)
        #try:
            response = urllib2.urlopen(url).read()
            data = json.loads(response)

            # Extract and display relevant information from the response
            
            self.response.write('<html><body>')
            #self.response.write('<h1>Weather Forecast for '+'('+lat+','+lon+')</h1>')
            self.response.write('<h1>Weather Forecast for '+'('+lat+','+lon+') - '+'Hourly'+' Forecast</h1><ul>')
            if forecast_type == 'temperature_2m':
                self.response.write('<table><tr><th>Time</th><th>\t\t</th><th>temperature</th></tr>')
                for i in range(len(data['hourly']['temperature_2m'])):
                      time_=data['hourly']['time'][i]
                      temperature_=data['hourly']['temperature_2m'][i]
                      self.response.write('<tr><td>'+time_+'</td>'+'<td>\t\t</td>'+'<td>'+str(temperature_)+'</td></tr>')
                self.response.write('</table>')
            elif forecast_type == 'daily':
                pass
            self.response.write('</ul></body></html>')

        #except Exception as e:
            #self.response.write('<html><body><h1>Error: '+e+'</h1>')
            #self.response.write('<p>Please try again with correct input.</p></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/forecast', ForecastHandler)
], debug=True)


#py google-cloud-sdk/bin/dev_appserver.py C:\Users\sahil\CCL_trial\8\app.yaml
