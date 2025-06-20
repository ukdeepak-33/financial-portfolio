from flask import Flask, render_template, jsonify, request
import yfinance as yf
from ai_recommend import generate_recommendations

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/api/portfolio", methods=["POST"])
def portfolio_data():
    tickers = request.json.get("tickers", [])
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1mo")["Close"]
        data[ticker] = hist.tolist()
    return jsonify(data)

@app.route("/api/recommend", methods=["POST"])
def recommend():
    tickers = request.json.get("tickers", [])
    recs = generate_recommendations(tickers)
    return jsonify(recs)

if __name__ == "__main__":
    app.run(debug=True)
