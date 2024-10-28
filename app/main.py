from fastapi import FastAPI
from routers import task
from routers import user

app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True})


@app.get('/')
async def get_welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)