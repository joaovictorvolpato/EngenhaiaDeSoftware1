import os

class Path:
    src_path = ""
    
    @staticmethod
    def set_src_path(path: str) -> None:
        Path.src_path = path

    @staticmethod
    def relative_to_src(path: str) -> str:
        return os.path.join(Path.src_path, path)
