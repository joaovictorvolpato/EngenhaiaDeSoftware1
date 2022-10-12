from pathlib import Path

class GamePath:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return GamePath.ASSETS_PATH / Path(path)
