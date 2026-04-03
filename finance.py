# finance.py
from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

def run_finance_ai(data):
    """
    Input: JSON with income, expenses
    Output: Suggested savings and advice
    """
    prompt = f"Income: {data.get('income')}, Expenses: {data.get('expenses')}. Give savings advice."
    result = generator(prompt, max_length=50)
    return {"result": result[0]['generated_text']}
