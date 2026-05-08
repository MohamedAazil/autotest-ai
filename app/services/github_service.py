import requests

class GithubService:
    
    def __init__(self, token: str):
        self.token = token
        self.paths = []
    
    def get_repo_contents(self, repo_full_name: str, path: str = ""):
        url = f"https://api.github.com/repos/{repo_full_name}/contents/{path}"
        
        headers = {
            "Authorization": f"Bearer {self.token}", 
            "Accept": "application/vnd.github+json"
        }
        
        response = requests.get(url=url, headers=headers)
        
        if response.status_code != 200:
            print("GitHub API Error:")
            print(response.text)
            return None
        
        response_json = response.json()

        if isinstance(response_json, list):

            discovered_paths = [
                item["path"]
                for item in response_json
            ]

            self.paths.extend(discovered_paths)
        
        return response_json