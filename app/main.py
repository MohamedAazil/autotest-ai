from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server is running", "status": 200} 

@app.post("/webhook")
async def webhook(req: Request):
    payload = await req.json()
    print("Webhook received")
    print(payload)
    
    return {
        "status": 200, 
        "message": "Webhook received"
    }