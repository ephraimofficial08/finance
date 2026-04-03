from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')

def run_investment_ai(data):
    prompt = f"Savings: {data.get('savings')}, Risk profile: {data.get('risk')}. Suggest investments and risk analysis."
    result = generator(prompt, max_length=50)
    return {"result": result[0]['generated_text']}
