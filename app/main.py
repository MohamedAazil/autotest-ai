from fastapi import FastAPI, Request, Depends
from .auth import resolve_installation_context
from .services.github_service import GithubService
from .services.repository_scanner import RepositoryScannerService
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server is running", "status": 200} 

@app.post("/webhook")
async def webhook(context = Depends(resolve_installation_context)):
    try:
        print("Webhook received")

        token = context["token"].get("token", None)
        
        if token is None:
            raise ValueError("Token not found") 
            

        payload = context["payload"]

        repo_full_name = payload["repository"]["full_name"]

        github = GithubService(token=token)
        
        scanner = RepositoryScannerService(github_service=github)
        
        scanner.scan(repo_full_name=repo_full_name)

        repo_contents = github.get_repo_contents(
            repo_full_name=repo_full_name
        )

        print("repo_contents", repo_contents)
        print("paths", scanner.paths)

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