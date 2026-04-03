from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')

def run_marketing_ai(data):
    prompt = f"Product: {data.get('product')}, Audience: {data.get('audience')}. Suggest posts, campaigns, and schedule."
    result = generator(prompt, max_length=50)
    return {"result": result[0]['generated_text']}
