import yfinance as yf
import pandas as pd
import numpy as np
from pypfopt import EfficientFrontier, risk_models, expected_returns

def get_portfolio_insights(tickers):
    data = yf.download(tickers, period="1mo")["Adj Close"]
    returns = data.pct_change().dropna()
    cumulative = (1 + returns).cumprod()

    perf = returns.mean() * 252
    risk = returns.std() * np.sqrt(252)
    sharpe = (perf / risk).mean()

    insights = {
        "history": data.to_dict(),
        "returns": {t: round(perf[t] * 100, 2) for t in perf.index},
        "volatility": {t: round(risk[t] * 100, 2) for t in risk.index},
        "sharpe_ratio": round(sharpe, 2),
        "top_gainer": perf.idxmax(),
        "top_loser": perf.idxmin(),
    }
    return insights

def generate_recommendations(tickers):
    data = yf.download(tickers, period="6mo")["Adj Close"]
    mu = expected_returns.mean_historical_return(data)
    S = risk_models.sample_cov(data)
    ef = EfficientFrontier(mu, S)
    weights = ef.max_sharpe()
    return ef.clean_weights()

