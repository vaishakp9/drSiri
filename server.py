from flask import Flask,render_template ,current_app,jsonify,url_for,redirect,request
import subprocess,requests,json,webbrowser,csv,sys,random
import codecs
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
token = ""
name = ""


app=Flask(__name__,static_url_path="")
app.debug=True

@app.route('/',methods=['POST','GET'])
def index():
	return ("MANJA")
@app.route('/resto',methods=['POST'])
def resto():
	request.headers
	uid = request.headers.get('uid')
	if (uid=='1'):
		name = "Perk.com,"
		level = "Michelin 1,"
		message = "Enjoyed Perk.com and its awesome service"
		csv1 = name+level+message
		return (csv1)
	if (uid=='2'):
		name = "Caffe Pascucci,"
		level = "Michelin 2,"
		message = "The gourmet delicacies were a big draw ! Great job."
		csv1 = name+level+message
		return (csv1)
	if (uid=='3'):
		name = "Mainland China,"
		level = "Michelin 3,"
		message = "The food was delectable. Try it out, guys !"
		csv1 = name+level+message
		return (csv1)
	else:
		return ("-1")
@app.route('/wait',methods=['POST'])
def weights():
	request.headers
	object_id = request.headers.get('object_id')
	url1 = "https://graph.facebook.com/v2.2/100010977690590_"+object_id+"/likes?access_token=CAACEdEose0cBAExv0ZCwQw8dJ3i6vbXR2aN266f0ORvXK8GOuy9lapisrqblD4V3hjZBZBX2q3uPxzvV7FZBlGUjMd2Gp1eFZA5XRqgCf3tYbsWeFQZAmJPUxKznkH82cZC8P3XymsNVC2Bj4Q83ffr5ORkT5OcGHf61gyJX7ZB2mowHNwssjM5uSR0sYRixbj9BoCB27UtOKQZDZD"
	r1 = requests.get(url1)
	json_data = r1.json()
	json_data = json_data["data"]
	number = len(json_data)
	#print(txt)
	print (str(number))
	return (str(number))
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
	exe=[33,26,41,39,46,25,38]
	acti=[[33,20,25,25,35,25,30],[0,6,16,14,11,0,8]]
	if("exercise" in text or "workout" in text):
		if("last week" in text):
			return "You exercised for "+str(sum(exe)/7)+" minutes last week"
		if("yesterday" in text):
			return "You exercised for "+str(exe[-2])+" minutes yesterday"
		if("today" in text):
			return "You exercised for "+str(exe[-1])+" minutes today"		
	elif("run" in text):
		if("last week" in text):
			return "You ran for "+str(sum(acti[0])/7)+" minutes, "+str(0.2*sum(acti[0])/7)[0:4]+" km last week"
		if("yesterday" in text):
			return "You ran for "+str(acti[0][-2])+" minutes, "+str(0.2*acti[0][-2])[0:4] +" km yesterday"
		if("today" in text):
			return "You ran for "+str(acti[0][-1])+" minutes, "+str(0.2*acti[0][-1])[0:4]+" km today"		
	elif("cycle" in text or "workout" in text):
		if("last week" in text):
			return "You cycled for "+str(sum(acti[1])/7)+" minutes, "+str(0.4*sum(acti[1])/7)[0:4]+" km last week"
		if("yesterday" in text):
			return "You cycled for "+str(acti[1][-2])+" minutes, "+str(0.4*acti[1][-2])[0:4] +" km yesterday"
		if("today" in text):
			return "You cycled for "+str(acti[1][-1])+" minutes, "+str(0.4*acti[1][-1])[0:4]+" km today"		
	
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
		url2 = "http://0.0.0.0:5000/"+json_data[0]
		print(url2)
		r2 = requests.get(url2)
		return r2.text
	elif(max==0) :
		print("this case")
		url2 = "http://0.0.0.0:5000/"+str(text)
		r2 = requests.get(url2)
		return r2.text
	else:
		json_data = json_data['entities'][0]
		json_data = json_data.keys()
		json_data2 = json_data3['entities'][1]
		json_data2 = json_data2.keys()
		url2 = "http://0.0.0.0:5000/ffx "+json_data[0]+" "+json_data2[0]
		print (url2)
		r2 = requests.get(url2)
		return r2.text
if __name__ =='__main__' :
	app.run(host="0.0.0.0",port=1993)

