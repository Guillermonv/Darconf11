from flask import Flask
from pymongo import MongoClient
from flask import request, jsonify

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.local
mycol = db["comapanies"]
app = Flask(__name__)


@app.route("/")
def home_page():
    return "Welcome Darconf"

@app.route("/company/<company>/<location>/<size>",  methods=["POST"])
def add(company,location,size):
    mydict = {"company":  company,
            "location":location,
            "size":size}

    mycol.insert_one(mydict)
    return "Field inserted"

@app.route("/company")
def getall():
    output = []
    for s in mycol.find():
        output.append({'company': s['company'], 'location' : s['location'], 'size' : s['size']})
    return jsonify({'result': output})


@app.route("/company/<company>")
def getbyproperty(name):
    s = mycol.find_one({'company': company})
    if s:
        output = {'company': s['company'], 'location': s['location'], 'size': s['size']}
    else:
        output = "No such company"
    return jsonify({'result': output})

@app.route("/company/<company>")
def delperson(name):
 mycol.delete_one({'company': company})
 return "borrado"


if __name__ == '__main__':
    app.run(debug=True)