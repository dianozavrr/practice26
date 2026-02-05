from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
import jwt

app = FastAPI()

users = {"diana": "12345"}

SECRET = "key"
oauth = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
def login(f: OAuth2PasswordRequestForm = Depends()):
    if f.username not in users or users[f.username] != f.password:
        raise HTTPException(401, "bad login")
    token = jwt.encode({"user": f.username}, SECRET, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}

@app.get("/profile")
def profile(token: str = Depends(oauth)):
    try:
        data = jwt.decode(token, SECRET, algorithms=["HS256"])
        return {"msg": "hi " + data["user"]}
    except:
        raise HTTPException(401, "bad token")
