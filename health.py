from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')

def run_health_ai(data):
    prompt = f"Salary: {data.get('salary')}, Expenses: {data.get('expenses')}, Savings: {data.get('savings')}, Investments: {data.get('investments')}, Debts: {data.get('debts')}. Compute financial health score."
    result = generator(prompt, max_length=50)
    return {"result": result[0]['generated_text']}
