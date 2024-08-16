from fastapi import FastAPI

app = FastAPI()

@app.get("/check-health")
def check_health():
    return {"status": "ok"}

