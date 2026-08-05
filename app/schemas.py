from pydantic import BaseModel

#Use this BaseModel since FastAPI uses it to create docu
class PostCreate(BaseModel): 
    title: str
    content: str

class PostResponse(BaseModel): 
    title: str
    content: str

