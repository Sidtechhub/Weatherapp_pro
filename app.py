from flask import Flask,render_template,requests
import requests
app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/weatherapp',methods=['POST',"GET"])
def get_weatherdata():
   
    url="https://api.openweathermap.org/data/2.5/weather"

    params = {
        'q' :requests.form.get("city"),
        'appid' :requests.form.get("appid") ,
        'units':requests.form.get("units")}
    response=requests.get(url,params=params)
    data=response.json()
    return f"data :{data}"

# data = requests.get(url, params=params)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5002)


















