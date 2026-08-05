from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# Dummy example of posts
text_post = {
    1: {"title": "New Test Post", "content": "cool test post"},
    2: {"title": "Morning Coffee", "content": "third cup and still counting"},
    3: {"title": "Weekend Plans", "content": "hiking if the weather holds"},
    4: {"title": "Book Review", "content": "finished it in two sittings"},
    5: {"title": "Kitchen Experiment", "content": "the sourdough finally rose"},
    6: {"title": "Late Night Debugging", "content": "it was a missing comma"},
    7: {"title": "New Camera Lens", "content": "everything looks better at f/1.8"},
    8: {"title": "Running Log", "content": "five kilometres, no complaints"},
    9: {"title": "Garden Update", "content": "the tomatoes are winning"},
    10: {"title": "Rainy Day", "content": "good excuse to stay inside"},
}

#Normal path endpoint with a limit
@app.get("/posts")
def get_all_posts(limit: int = None): #Specifies that we can add a limit to the returned posts, by setting = none we make it obligatory
    if limit:
        return list(text_post.values())[:limit]
    return text_post
#We need to specify the types in FastAPI so that the functions can be really good docs and so it has the data validations

#Query parameter endpoint
@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_post.get(id)


@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_post[max(text_post.keys()) + 1] = {"title": post.title, "content": post.content}
    return new_post





