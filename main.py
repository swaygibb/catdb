from fastapi import FastAPI
from lib.cat import Cat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins (for development purposes)
origins = ["*"]

# Enable CORS for all routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_cats():
    cat = Cat()
    return {"cats": cat.get_cats()}

@app.get("/cats/{cat_id}")
def get_cat(cat_id: int):
    cat = Cat()
    return {"cat": cat.get_cat(cat_id)}
