import { useState, useEffect } from 'react';
import { getAIFinancialInsights } from '../lib/openai';
import ReactMarkdown from 'react-markdown';

export default function AIInsights({ holdings }) {
  const [insights, setInsights] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchInsights = async () => {
      if (holdings.length === 0) return;
      setLoading(true);
      try {
        const response = await getAIFinancialInsights(holdings);
        setInsights(response);
      } catch (error) {
        console.error("AI Error:", error);
        setInsights("Could not generate insights at this time");
      }
      setLoading(false);
    };
    
    fetchInsights();
  }, [holdings]);

  return (
    <div className="ai-insights">
      <h3>AI Portfolio Analysis</h3>
      {loading ? (
        <p>Analyzing your portfolio...</p>
      ) : (
        <ReactMarkdown>{insights}</ReactMarkdown>
      )}
    </div>
  );
}
