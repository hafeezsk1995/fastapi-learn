from pydantic import BaseModel
from typing import Optional

class Blog1(BaseModel):
    title :str
    desc :Optional[str] = None
    published :bool

class ShowBlog(BaseModel):
    title :str
    class Config():
        orm_mode =  True
 

class User(BaseModel):
    name :str 
    email :str 
    password :str
            
            
class UserResponse(BaseModel):
    name :str 
    email :str 
    class Config():
        orm_mode = True
                