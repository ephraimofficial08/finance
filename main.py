# main.py
from fastapi import FastAPI, Request
from finance import run_finance_ai
from payroll import run_payroll_ai
from expense import run_expense_ai
from savings import run_savings_ai
from investment import run_investment_ai
from debt import run_debt_ai
from health import run_health_ai
from marketing import run_marketing_ai
from tasks import run_tasks_ai
from subscription import run_subscription_ai
from bugs import run_bugs_ai
from notifications import run_notifications_ai
from behavior import run_behavior_ai
from compliance import run_compliance_ai
from optimization import run_optimization_ai

app = FastAPI(title="SmartMoney AI Engine")

@app.post("/finance")
async def finance_endpoint(request: Request):
    data = await request.json()
    return run_finance_ai(data)

@app.post("/payroll")
async def payroll_endpoint(request: Request):
    data = await request.json()
    return run_payroll_ai(data)

@app.post("/expense")
async def expense_endpoint(request: Request):
    data = await request.json()
    return run_expense_ai(data)

@app.post("/savings")
async def savings_endpoint(request: Request):
    data = await request.json()
    return run_savings_ai(data)

@app.post("/investment")
async def investment_endpoint(request: Request):
    data = await request.json()
    return run_investment_ai(data)

@app.post("/debt")
async def debt_endpoint(request: Request):
    data = await request.json()
    return run_debt_ai(data)

@app.post("/health")
async def health_endpoint(request: Request):
    data = await request.json()
    return run_health_ai(data)

@app.post("/marketing")
async def marketing_endpoint(request: Request):
    data = await request.json()
    return run_marketing_ai(data)

@app.post("/tasks")
async def tasks_endpoint(request: Request):
    data = await request.json()
    return run_tasks_ai(data)

@app.post("/subscription")
async def subscription_endpoint(request: Request):
    data = await request.json()
    return run_subscription_ai(data)

@app.post("/bugs")
async def bugs_endpoint(request: Request):
    data = await request.json()
    return run_bugs_ai(data)

@app.post("/notifications")
async def notifications_endpoint(request: Request):
    data = await request.json()
    return run_notifications_ai(data)

@app.post("/behavior")
async def behavior_endpoint(request: Request):
    data = await request.json()
    return run_behavior_ai(data)

@app.post("/compliance")
async def compliance_endpoint(request: Request):
    data = await request.json()
    return run_compliance_ai(data)

@app.post("/optimization")
async def optimization_endpoint(request: Request):
    data = await request.json()
    return run_optimization_ai(data)

# Uvicorn run (optional, Render handles this)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
