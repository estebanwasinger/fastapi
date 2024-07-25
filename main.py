import os
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/env/")
async def get_env_variable(var_name: str):
    env_value = os.getenv(var_name)
    if not env_value:
        raise HTTPException(status_code=404, detail=f"Environment variable '{var_name}' not found")
    
    first_four_words = ' '.join(env_value.split()[:4])
    return {"env_var_name": var_name, "first_four_words": first_four_words}