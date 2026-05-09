
class TestDiscoveryService:
    def __init__(self, paths):
        self.paths = paths
        self.test_names = [
            "test", 
            "e2e", 
            "unit", 
            "integration"
        ]
        
    def isTestFile(self, item):
        path = item['path'].lower()
        for test_name in self.test_names: 
            if test_name in path: 
                return True
        return False 
        
        
    def discover_tests(self): 
        testPaths = list(filter(self.isTestFile, self.paths))
        return testPaths