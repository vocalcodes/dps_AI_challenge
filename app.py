from flask import Flask, request, jsonify, render_template, flash
import pickle

app = Flask(__name__)
model = pickle.load(open('randomforest.pkl', 'rb'))
app.secret_key = "key"

@app.route("/")
def index():
    flash("Prediction: ")
    return render_template("index.html")


@app.route("/predict", methods=['POST', 'GET'])
def predict():
    year = int(request.form["year"])
    month = int(request.form["month"])
    target = [0, 0, year, month]
    prediction = model.predict([target])
    flash(f"Prediction: {prediction[0]}")
    return render_template("index.html")
    
@app.route("/api/predict", methods=['POST'])
def apiPredict():
    if "year" not in request.get_json(force=True) or "month" not in request.get_json(force=True):
        return {"error": "Missing input value"}, 400
    else:
        data = request.get_json(force=True)
        year = data["year"]
        month = data["month"]
        if year < 2021:
            return {"error": "Select a year after 2020"}, 400
        elif month < 1 or month > 12:
            return {"error": "Invalid month"}, 400
        else:
            target = [0, 0, year, month]
            prediction = model.predict([target])
            return jsonify({'prediction': prediction[0]})
    
if __name__ == "__main__":
    app.run(debug = True)