from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')

def run_subscription_ai(data):
    prompt = f"Salary: {data.get('salary')}, Deposits: {data.get('deposits')}, Account activity: {data.get('activity')}. Suggest subscription tier and detect fraud."
    result = generator(prompt, max_length=50)
    return {"result": result[0]['generated_text']}
