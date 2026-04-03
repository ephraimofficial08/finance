# payroll.py
from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

def run_payroll_ai(data):
    prompt = f"Salary: {data.get('salary')}, Bonuses: {data.get('bonus')}, Deductions: {data.get('deductions')}. Verify payroll and detect anomalies."
    result = generator(prompt, max_length=50)
    return {"result": result[0]['generated_text']}
