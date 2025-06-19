import OpenAI from 'openai';

const openai = new OpenAI({
  apiKey: process.env.REACT_APP_OPENAI_KEY,
  dangerouslyAllowBrowser: true // Only for frontend implementation
});

export async function getAIFinancialInsights(portfolioData) {
  const prompt = `Analyze this portfolio: ${JSON.stringify(portfolioData)}. 
  Provide 3 concise insights and 1 recommended action in markdown format.`;
  
  const completion = await openai.chat.completions.create({
    messages: [{ role: "user", content: prompt }],
    model: "gpt-3.5-turbo",
  });

  return completion.choices[0].message.content;
}
