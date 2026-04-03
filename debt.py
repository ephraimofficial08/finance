from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')

def run_debt_ai(data):
    prompt = f"Loans: {data.get('loans')}, Credit cards: {data.get('credit_cards')}. Suggest repayment strategy and risk score."
    result = generator(prompt, max_length=50)
    return {"result": result[0]['generated_text']}
