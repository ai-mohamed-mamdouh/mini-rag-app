from src.controllers.BaseController import BaseController
import os
from pathlib import Path
from uuid import uuid4

class ProjectController(BaseController) :
    def __init__(self) :
        super().__init__()

    def get_project_path(self, project_id : str) :
        project_dir = self.files_dir / project_id

        if not os.path.exists(project_dir) :
            os.makedirs(project_dir) 
        
        return project_dir

    def get_unique_key(self, project_files_dir: str | Path, filename: str) -> str:
        project_files_dir = Path(project_files_dir)
        project_files_dir.mkdir(parents=True, exist_ok=True)

        file_path = project_files_dir / filename

        while file_path.exists():
            stem = file_path.stem
            suffix = file_path.suffix

            unique_name = f"{stem}_{uuid4().hex[:8]}{suffix}"
            file_path = project_files_dir / unique_name

        return str(file_path), unique_name
