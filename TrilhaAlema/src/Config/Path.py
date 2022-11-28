import os

class Path:
    src_path = os.path.join(os.getcwd())

    @staticmethod
    def relative_to_assets(path: str) -> str:
        print(Path.src_path)
        return os.path.join(Path.src_path, "Assets", path)
    
    @staticmethod
    def relative_to_config(path: str) -> str:
        return os.path.join(Path.src_path, "Config", path)
