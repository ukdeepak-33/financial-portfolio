from flask import Flask, render_template, request, jsonify
import yfinance as yf
from ai_recommend import get_portfolio_insights, generate_recommendations

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/api/portfolio", methods=["POST"])
def portfolio_data():
    tickers = request.json.get("tickers", [])
    if not tickers:
        return jsonify({"error": "No tickers provided"}), 400

    insights = get_portfolio_insights(tickers)
    return jsonify(insights)

@app.route("/api/recommend", methods=["POST"])
def recommend():
    tickers = request.json.get("tickers", [])
    recs = generate_recommendations(tickers)
    return jsonify(recs)

if __name__ == "__main__":
    app.run(debug=True)
