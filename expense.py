from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')

def run_expense_ai(data):
    prompt = f"Transactions: {data.get('transactions')}. Categorize spending and detect overspending."
    result = generator(prompt, max_length=50)
    return {"result": result[0]['generated_text']}
