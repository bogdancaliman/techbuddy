import hashlib
from typing import Optional
from fastapi import Cookie, Depends, FastAPI, HTTPException, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel  
from utils.jwt_utils import create_jwt_token, verify_jwt_token

app = FastAPI()

# Fake user data with hashed password
FAKE_USER = {
    "name": "John",
    "email": "john-doe@email.com",
    "password": hashlib.sha256("password123".encode()).hexdigest()  # Fake hashed password
}

# Pydantic model for login request
class LoginData(BaseModel):
    email: str
    name: str
    password: str

@app.get("/") 
async def main_route():     
  return {"message": "Hello World!"}

@app.post("/login")
async def login(data: LoginData, response: Response):
    # Simple verification with fake user data
    hashed_password = hashlib.sha256(data.password.encode()).hexdigest()
    if (
        data.email == FAKE_USER["email"]
        and data.name == FAKE_USER["name"]
        and hashed_password == FAKE_USER["password"]
    ):
        # Create a fake JWT token
        token = create_jwt_token({"sub": FAKE_USER["email"]})
        response.set_cookie(key="access_token", value=token, httponly=True)
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/protected")
async def protected(access_token: Optional[str] = Cookie(None)):
    # Verify the JWT token
    print(access_token)
    if access_token is None:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    payload = verify_jwt_token(access_token)
    if payload:
        return {"message": "You have access to protected content!"}
    else:
        raise HTTPException(status_code=403, detail="Invalid or expired token")
