from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_recommend import get_portfolio_insights, generate_recommendations

app = Flask(__name__)
CORS(app)  # Allows frontend to access this API

@app.route("/api/portfolio", methods=["POST"])
def portfolio_data():
    tickers = request.json.get("tickers", [])
    return jsonify(get_portfolio_insights(tickers))

@app.route("/api/recommend", methods=["POST"])
def recommend():
    tickers = request.json.get("tickers", [])
    return jsonify(generate_recommendations(tickers))

if __name__ == "__main__":
    app.run(debug=True)
