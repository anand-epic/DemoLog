from fastapi import FastAPI 
from logger import create_logger

app = FastAPI("DemoLog")
log = create_logger("DemoLog")

@app.get("/demoLog")
def demoLog():
    log.info("Demo Log")
    log.info("Demo Log 1")
    return {}


