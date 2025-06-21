import React, { useState } from "react";
import { Line } from "react-chartjs-2";
import "chart.js/auto";

const API_URL = "https://portfolio-api.onrender.com/api";

export default function Dashboard() {
  const [tickers, setTickers] = useState("");
  const [data, setData] = useState(null);
  const [recommendations, setRecommendations] = useState({});

  const loadPortfolio = async () => {
    const symbols = tickers.split(",").map(s => s.trim());
    const res = await fetch(`${API_URL}/portfolio`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ tickers: symbols }),
    });
    const json = await res.json();
    setData(json);

    const recRes = await fetch(`${API_URL}/recommend`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ tickers: symbols }),
    });
    setRecommendations(await recRes.json());
  };

  return (
    <div>
      <input
        value={tickers}
        onChange={(e) => setTickers(e.target.value)}
        placeholder="e.g., AAPL,GOOG,TSLA"
      />
      <button onClick={loadPortfolio}>Analyze</button>

      {data && (
        <>
          <Line
            data={{
              labels: Object.keys(data.history[Object.keys(data.history)[0]]),
              datasets: Object.entries(data.history).map(([symbol, values]) => ({
                label: symbol,
                data: Object.values(values),
                borderColor: "#" + Math.floor(Math.random() * 16777215).toString(16),
              })),
            }}
          />

          <div>
            <h3>Sharpe Ratio: {data.sharpe_ratio}</h3>
            <p>Top Gainer: {data.top_gainer}</p>
            <p>Top Loser: {data.top_loser}</p>
          </div>

          <div>
            <h3>AI Recommendations</h3>
            {Object.entries(recommendations).map(([k, v]) => (
              <p key={k}>{k}: {(v * 100).toFixed(2)}%</p>
            ))}
          </div>
        </>
      )}
    </div>
  );
}
