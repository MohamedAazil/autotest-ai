from fastapi import FastAPI, Request, Depends
from .auth import resolve_installation_context
from .services.github_service import GithubService
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server is running", "status": 200} 

@app.post("/webhook")
async def webhook(context = Depends(resolve_installation_context)):
    try:
        print("Webhook received")

        token = context["token"]

        payload = context["payload"]

        repo_full_name = payload["repository"]["full_name"]

        github = GithubService(token=token)

        repo_contents = github.get_repo_contents(
            repo_full_name=repo_full_name
        )

        print(repo_contents)

        return {
            "status": 200,
            "message": "Webhook received"
        }
            
    except Exception as e: 
        return {
            "status": 500,
            "message": "Request Failed",
            "error": str(e) 
        }