from fastapi import FastAPI

app = FastAPI()

# the last part, :path, tells it that the parameter should match any path.
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}