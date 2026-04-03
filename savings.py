from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')

def run_savings_ai(data):
    prompt = f"Income: {data.get('income')}, Expenses: {data.get('expenses')}, Goals: {data.get('goals')}. Suggest savings allocation and progress."
    result = generator(prompt, max_length=50)
    return {"result": result[0]['generated_text']}
