from uvicorn import run
from fastapi import FastAPI
from typing import Optional

from ocr import OCR

app = FastAPI(
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    title="OCR",
    description="Convert scanned documents and images into editable text"
)


@app.get("/")
def home(file_path: Optional[str] = None):
    ocr_tool = OCR()
    return ocr_tool.run_ocr(file_path)


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)