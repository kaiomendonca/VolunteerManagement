from fastapi import FastAPI
from volunteer_management.routers import volunteers

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API is working!"}


app.include_router(volunteers.router)
