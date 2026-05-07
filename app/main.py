from fastapi import FastAPI, Request, Depends
from .auth import resolve_installation_context
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server is running", "status": 200} 

@app.post("/webhook")
async def webhook(req: Request, installation_id = Depends(resolve_installation_context)):
    payload = await req.json()
    print("Webhook received")
    print(payload)
    
    return {
        "status": 200, 
        "message": "Webhook received"
    }