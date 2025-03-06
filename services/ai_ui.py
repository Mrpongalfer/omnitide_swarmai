from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "OmniTide SwarmAI is running!"}

@app.get("/status")
def get_status():
    return {"status": "AI Online", "learning": True, "security": "Active"}

# Run server: uvicorn services.ai_ui:app --host 0.0.0.0 --port 5000
