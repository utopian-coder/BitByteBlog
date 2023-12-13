from fastapi import APIRouter, HTTPException, Path
from typing import Annotated
from bson import ObjectId
from ..config.database import mongo_client
from ..schemas.blog_schema import serialize_all_blog, serialize_blog
from ..models.blog_model import Blog

router = APIRouter()

db = mongo_client.blogs
blog_collection = db.blogs

@router.get('/', status_code=200)
def get_all_blogs():
    try:
        blogs = serialize_all_blog(blog_collection.find())
        if (blogs):
            return {"status": "success", "blogs": blogs}
        else:
            return {"status": "success", "blogs": "Didn't find any blog!"}
    except:
        raise HTTPException(status_code=404, detail="Something went wrong!")
    
@router.get('/{blog_id}', status_code=200)
def get_a_blog(blog_id):
    try:
        blog = serialize_blog(blog_collection.find_one({"_id": ObjectId(blog_id)}))
        if (not blog):
            raise HTTPException(status_code=404, detail="There's no blog with this id!")
        return {"status": "success", "blog": blog}
    except:
        raise HTTPException(status_code=404, detail='Something went wrong!')
    
@router.post('/', status_code=201)
def create_blog(blog: Blog):
    try:
        blog_collection.insert_one(blog.model_dump())
        return {"status": "success", "message": "Successfully created the blog!"}
    except:
        raise HTTPException(status_code=500, detail="Something went wrong, try again!")
    
@router.delete('/{blog_id}', status_code=204)
def delete_blog(blog_id: Annotated[str, Path(title="The id of the item to get!")]):
    try:
        blog_collection.find_one_and_delete({"_id": ObjectId(blog_id)})
        return {"status": "success", "message": "Successfully deleted!"}
    except:
        raise HTTPException(status_code=500, detail="Something went wrong, please try again!")
    
@router.put("/{blog_id}", status_code=200)
def update_blog(blog_id, new_blog: Blog):
    try:
        blog_collection.find_one_and_update({"_id": ObjectId(blog_id)}, { "$set": new_blog.model_dump() })
        return {"status": "success", "message": "Successfully updated!"}
    except:
        raise HTTPException(status_code=200, detail="Something went wrong, try again!")

#Created for DB cleanup in dev phase!
@router.delete("/")
def delete_all_blogs():
    blog_collection.delete_many({})
    return {"status": "success"}