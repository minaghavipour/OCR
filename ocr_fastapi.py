from uvicorn import run
from fastapi import FastAPI, Query
from typing import Optional

from ocr_cmd import ocr_project

app = FastAPI(
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    title="OCR",
    description="Convert scanned documents and images into editable text"
)


@app.get("/")
def home(file_path: Optional[str] = None):
    return ocr_project(file_path)


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)