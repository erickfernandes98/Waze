from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/wazePost',methods=["POST"])
def wazePost():
    if request.method == 'POST':
        latitude = request.form['latitude']
        print(latitude)
        longitude = request.form['longitude']
        print(longitude)
        return jsonify(result='<iframe src="https://embed.waze.com/iframe?zoom=15&lat='+latitude+'&lon='+longitude+'&pin=1&ct=livemap" width="1100" height="600" allowfullscreen></iframe>')
    return render_template('index.html')

@app.route("/")
def index_template():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port = 8080, debug = True)