#       Service Status Script              #
#       By Junaid Kapadia                  #
#       Contact: Junaid.Kapadia@tallac.com #
############################################
import requests
import json
import pymongo
import os
import redis
import xml.etree.ElementTree as ET
from pymongo import MongoClient
from StringIO import StringIO
from xml.etree.ElementTree import Element, SubElement, tostring
from flask import Flask
app = Flask(__name__)
REDIS_IP = os.environ.get("REDIS_IP", None)
MONGO_IP = os.environ.get("MONGO_IP", None)

@app.route("/")
def service_alive_status():
	return "I am up and running."

@app.route("/mongo")
def mongo_status():

   mongoStatus = ''
   responseTime = '1.0'
   #Establish connection with Mongo
   try:
  	 client = MongoClient(MONGO_IP, 27017, connectTimeoutMS=3000)
  	 db = client.tallac
         mongo_customers_count = db.customers.count()
         mongoStatus = 'OK'
   except:
         mongoStatus = 'Down'
   finally:
         client.close()

   xmlTemplate = """<pingdom_http_custom_check>
                <status>""" + str(mongoStatus) + """</status>
                <response_time>""" + str(responseTime) + """</response_time>
</pingdom_http_custom_check>"""

   return xmlTemplate

@app.route("/lms1")
def lms_status1():

    lmsStatus = ''
    responseTime = ''
    expectedResponse = {'name': 'SKUName', 'value': 'XXXXX-XXXX'}
    url = 'https://update1.eng.VENDOR.com:443/cwms-register'
    headers = {'Connection': 'Keep-Alive', 'X-CP-Register-Protocol-Version': '1.3', 'Content-Type': 'application/xml'}
    #payload = {'ProductId': '2062', 'LicenseKey': 'XX3E09-3D19-9C59-7F01-D65A-00F2-2098-030C-0639', 'ActionType': '0'}
    xml = """<?xml version='1.0' encoding='utf-8'?>
    <RegisterInfo>
    <param name="ProductId" value="2062"/>
    <param name="LicenseKey" value="XX3E09-3D19-9C59-7F01-D65A-00F2-2098-030C-0639"/>
    <param name="ActionType" value="0"/>
    </RegisterInfo>"""
    try:
        r = requests.post(url, data=xml, headers=headers, verify=False, timeout=.300)
        response = ET.fromstring(r.text)
        resp = response[0][5].attrib
        respTime = response.attrib
        check_resp = cmp(resp, expectedResponse)
    except Exception as e:
            print "Vendor Error, LMS is down."
            check_resp = 1
    if check_resp == 0:
       lmsStatus = "OK"
       responseTime = respTime.values()[0]
    else:
       lmsStatus = "Down"

    #except:
      # lmsStatus = 'Down'


    xmlTemplate = """<pingdom_http_custom_check>
                 <status>""" + str(lmsStatus) + """</status>
                 <response_time>""" + str(responseTime) + """</response_time>
</pingdom_http_custom_check>"""

    return xmlTemplate

@app.route("/lms2")
def lms_status2():

    lmsStatus = ''
    responseTime = ''
    expectedResponse = {'name': 'SKUName', 'value': 'XXXXXX-10000S'}
    url = 'https://update2.eng.VENDOR.com:443/cwms-register'
    headers = {'Connection': 'Keep-Alive', 'X-CP-Register-Protocol-Version': '1.3', 'Content-Type': 'application/xml'}
    #payload = {'ProductId': '2062', 'LicenseKey': 'XX3E09-3D19-9C59-7F01-D65A-00F2-2098-030C-0639', 'ActionType': '0'}
    xml = """<?xml version='1.0' encoding='utf-8'?>
    <RegisterInfo>
    <param name="ProductId" value="2062"/>
    <param name="LicenseKey" value="XX3E09-3D19-9C59-7F01-D65A-00F2-2098-030C-0639"/>
    <param name="ActionType" value="0"/>
    </RegisterInfo>"""
    try:
        r = requests.post(url, data=xml, headers=headers, verify=False, timeout=0.300)
        response = ET.fromstring(r.text)
        resp = response[0][5].attrib
        respTime = response.attrib
        check_resp = cmp(resp, expectedResponse)
    except Exception as e:
           print "Vendor Error, LMS is down."
           check_resp = 1
    if check_resp == 0:
       lmsStatus = "OK"
       responseTime = respTime.values()[0]
    else:
       lmsStatus = "Down"

    #except:
      # lmsStatus = 'Down'


    xmlTemplate = """<pingdom_http_custom_check>
                 <status>""" + str(lmsStatus) + """</status>
                 <response_time>""" + str(responseTime) + """</response_time>
</pingdom_http_custom_check>"""

    return xmlTemplate


if __name__ == "__main__":
   app.run(host='0.0.0.0')
