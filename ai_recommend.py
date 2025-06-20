from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt.risk_models import sample_cov
from pypfopt.expected_returns import mean_historical_return
import yfinance as yf

def generate_recommendations(tickers):
    if not tickers:
        return {"error": "No tickers provided"}
    
    data = yf.download(tickers, period="6mo")["Adj Close"]
    mu = mean_historical_return(data)
    S = sample_cov(data)
    
    ef = EfficientFrontier(mu, S)
    weights = ef.max_sharpe()
    cleaned = ef.clean_weights()
    
    return dict(cleaned)
