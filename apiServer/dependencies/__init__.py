from fastapi import Header, HTTPExecption

async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPExecption(status_code=400, detail="X-Token header invalid")

async def get_query_token(token: str):
    if token != "celeste":
        raise HTTPExecption(status_code=400, detail="No Celeste token provider")