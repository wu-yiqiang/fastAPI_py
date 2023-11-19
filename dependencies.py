from fastapi import HTTPException

async def get_query_token(x_token: str):
    if x_token != "secret-token":
        raise HTTPException(status_code=400, detail="no secret-token...")