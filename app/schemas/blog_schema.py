def serialize_blog(blog) -> dict:
    return {
        "id": str(blog["_id"]),
        "author": blog["author"],
        "title": blog["title"],
        "body": blog["body"]
    }

def serialize_all_blog(blogs) -> list:
    return [serialize_blog(blog) for blog in blogs]