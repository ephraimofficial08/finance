from transformers import pipeline
generator = pipeline('text-generation', model='gpt2')

def run_tasks_ai(data):
    prompt = f"Tasks: {data.get('tasks')}, Availability: {data.get('availability')}. Rank tasks by priority and suggest delegation."
    result = generator(prompt, max_length=50)
    return {"result": result[0]['generated_text']}
