from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    fields = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
              'floors', 'waterfront', 'view', 'condition',
              'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated']
    try:
        values = [float(request.form[field]) for field in fields]
        prediction = model.predict([values])[0]
        return render_template("result.html", price=f"${prediction:,.2f}")
    except:
        return render_template("result.html", price="Invalid input.")

if __name__ == "__main__":
    app.run(debug=True)
