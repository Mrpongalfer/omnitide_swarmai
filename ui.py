from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "OmniTide SwarmAI is running!", "status": "Online"}

@app.get("/core-team")
def get_core_team():
    return {
        "Tony Stark": "Performance & Optimization",
        "Rick Sanchez": "Debugging & Self-Improvement",
        "Sherlock Holmes": "Security & Threat Detection",
        "Rocket Raccoon": "Cybersecurity & Defense",
        "Yoda": "Task Prioritization & AI Swarm",
        "Harley Quinn": "Chaos Testing & Resilience",
        "Power": "Failover & Backup",
        "Makima": "AI Coordination & High-Level Execution",
        "Denji": "Resource Optimization",
        "Deku": "Long-Term AI Task Execution",
        "All Might": "System Stability"
    }

@app.get("/status")
def get_status():
    return {
        "AI Learning": "Active",
        "Security": "Protected",
        "Self-Healing": "Enabled",
        "Knowledge Scraper": "Running"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
