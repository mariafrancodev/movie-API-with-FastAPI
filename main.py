from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.login import login_router
from routers.home import home_router


app = FastAPI()
app.title = "My app with FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(login_router)
app.include_router(home_router)


Base.metadata.create_all(bind=engine)
