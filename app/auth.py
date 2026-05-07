import time 
import jwt
import os
import requests
from dotenv import load_dotenv
from fastapi import Request

load_dotenv()
GITHUB_APP_ID = os.getenv("GITHUB_APP_ID")
GITHUB_PRIVATE_KEY = os.getenv("GITHUB_PRIVATE_KEY")


def generate_jwt(): 
    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + 600,
        "iss": GITHUB_APP_ID
    }

    token = jwt.encode(
        payload = payload,
        key = GITHUB_PRIVATE_KEY, 
        algorithm = "RS256"
    )
    
    return token

def get_installation_token(installation_id): 
    jwt_token = generate_jwt()
    url = f"https://api.github.com/app/installations/{installation_id}/access_tokens"
    
    headers = {
        "Authorization": f"Bearer {jwt_token}", 
        "Accept": "application/vnd.github+json"
    }
    
    response = requests.post(url=url, headers=headers)
    print(response.json())
    return response.json()

async def resolve_installation_context(request: Request):

    payload = await request.json()

    installation_id = payload["installation"]["id"]

    token = get_installation_token(installation_id)

    return {
        "installation_id": installation_id,
        "token": token,
        "payload": payload
    }