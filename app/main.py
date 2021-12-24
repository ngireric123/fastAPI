from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post,user, auth, vote
from .config import settings

#since we have added Alembic let us comment out models.Base.metadata
#models.Base.metadata.create_all(bind=engine)

#lists of URLs that can talk to my API if u want ur api to talk to any URL u just write ["*"]

origins = ["https://www.google.com", "https://www.youtube.com"]

app = FastAPI()
#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers 
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# ROOT
@app.get("/")
def root():
    return {"message": "Welcome to Our App !!!"}



