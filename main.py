from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route("/")

def homepage():
    return "<h1>Welcome to home page<h1>"

@app.route("/add",methods=['POST'])
def addition():
    if request.method=='POST':
        result=int(request.json['num1']) + int(request.json['num2'])
        return jsonify("the summation is {}".format(resulthttps://white-artist-rgomi.ineuron.app/))

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)