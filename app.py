from flask import Flask, render_template, request, redirect
from model import predict_disease

app = Flask(__name__)

# LOGIN PAGE
@app.route('/')
def login_page():
    return render_template("login.html")

# LOGIN CHECK
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Demo login
    if username == "user" and password == "1234":
        return redirect("/home")
    else:
        return "Invalid Login"

# SYMPTOM PAGE
@app.route('/home')
def home():
    return render_template("index.html")

# PREDICTION
@app.route('/predict', methods=['POST'])
def predict():
    symptoms = request.form['symptoms']
    disease, level = predict_disease(symptoms)
    return render_template(
        "result.html",
        symptoms=symptoms,
        disease=disease,
        level=level
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)