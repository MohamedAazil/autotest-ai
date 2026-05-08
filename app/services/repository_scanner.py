from .github_service import GithubService

class RepositoryScannerService: 
    def __init__(self, github_service):
        self.github_service = github_service
        self.paths = []
    
    def scan(self, repo_full_name: str, path: str = ""):
        contents = self.github_service.get_repo_contents(repo_full_name, path)
        
        if not contents: 
            return 
        
        if not isinstance(contents, list): 
            return 

        for item in contents: 
            item_path = item["path"]
            item_type = item["type"]
            
            self.paths.append({
                "path":item_path, 
                "type":item_type
            })
            
            print(f"{item_type}: {item_path}")
            
            if item_type == "dir":
                self.scan(repo_full_name=repo_full_name, path=item_path)