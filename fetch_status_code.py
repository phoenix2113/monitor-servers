import datetime
import urllib.request
import urllib.error
import time
from Update_result import update_result
from send_email import send_email
import smtplib
import csv

updatedList=list()
def server_response(x,duration):
    frequency = x[2]
    if x[3]==True:        
        urls=x[1].split(';')        
        while duration>=frequency:            
            for i, url in enumerate(urls):
                try:
                    result = urllib.request.urlopen(url).getcode()
                    updatedList.append([url,result,str(datetime.datetime.now()).replace(" ","-")])
                except urllib.error.HTTPError as error:
                    result = error.code
                    # send_email() 
                except urllib.error.URLError as error:
                    # send_email()
                    result= error.reason
        
            duration = duration-frequency
            time.sleep(frequency*60)
        update_result(updatedList)
            

