from flask import Flask,jsonify
import aiml
app=Flask(__name__)
app.debug=True

def respond_ai(ind):
    k = aiml.Kernel()
    k.learn("firsttry.aiml")
    k.setBotPredicate("name", "Chatty")
    response = k.respond(ind)
    return response
@app.route('/<ind>')
def index(ind):
    r=respond_ai(ind)
    return r


	

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)