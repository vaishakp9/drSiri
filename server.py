#!python2
from flask import Flask,render_template ,current_app,jsonify,url_for,redirect,request
import aiml
import subprocess,requests,json,webbrowser,csv,sys,random
import codecs
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
token = ""
name = ""


app=Flask(__name__,static_url_path="")
app.debug=True
def respond_ai(ind):
    k = aiml.Kernel()
    k.learn("firsttry.aiml")
    k.learn("emotions.aiml")
    k.setBotPredicate("name", "Chatty")
    response = k.respond(ind)
    return response
@app.route('/',methods=['POST','GET'])
def index():
	return ("MANJA")
@app.route('/keyword_extract', methods=['POST'])
def keyword_extract():
	request.headers
	text = request.headers.get("text")
	text = str(text)
	url = "https://api.repustate.com/v3/dc88b08e3079785fd126e94a3633fbe817e8d07b/entities.json"
	#payload = {"text": "I've got AIDS"}
	r = requests.post(url, data={'text':text})
	json_data = r.json()
	json_data = json.dumps(json_data)
	return str(json_data)
@app.route('/post_analyze',methods=['POST'])
def post_analyze():
	request.headers
	text = request.headers.get("text")
	text = str(text)
	#print(text)
	url = "https://api.repustate.com/v3/dc88b08e3079785fd126e94a3633fbe817e8d07b/entities.json"
	#payload = {"text": "I've got AIDS"}
	r = requests.post(url, data={'text':text})
	json_data = r.json()
	#print (str(json_data['entities'][0])+" "+str(json_data['entities'][1]))
	max = len(json_data['entities'])
	json_data3 = json_data 
	if (max == 1) :
		json_data = json_data['entities'][0]
		json_data = json_data.keys()
		r=respond_ai(json_data[0])
		#url2 = "http://0.0.0.0:5000/"+json_data[0]
		#print(url2)
		#r2 = requests.get(url2)
		#return r2.text
		return r
	elif(max==0) :
		print("this case")
		#url2 = "http://0.0.0.0:5000/"+str(text)
		#r2 = requests.get(url2)
		#return r2.text
		return respond_ai(str(text))
	else:
		json_data = json_data['entities'][0]
		json_data = json_data.keys()
		json_data2 = json_data3['entities'][1]
		json_data2 = json_data2.keys()
		#url2 = "http://0.0.0.0:5000/ffx "+json_data[0]+" "+json_data2[0]
		#print (url2)
		#r2 = requests.get(url2)
		return respond_ai("ffx"+json_data[0]+" "+json_data2[0])
if __name__ =='__main__' :
	app.run(host="0.0.0.0",port=1993)

