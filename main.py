from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes.blog_routes import router as blog_routes

load_dotenv()

app = FastAPI()

app.include_router(blog_routes, prefix="/api/v1/blogs", tags=["Blogs"])
