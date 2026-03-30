from pathlib import Path


class PathHandler:
    def __init__(self):
        self.PROJECT_DIRECTORY = Path(__file__)
        self.CURRENT_DIRECTORY = self.PROJECT_DIRECTORY.resolve()
    
    def get_directory(self, target: str) -> Path:
        for parent in self.CURRENT_DIRECTORY.parents:
            target_dir = parent/target

            if target_dir.exists():
                return target_dir