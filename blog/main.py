

from fastapi import Depends, status, Response, HTTPException
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from fastapi import FastAPI
from hasing import Hash


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    
        

@app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blogs'])
def create(request:schemas.Blog1,db:Session = Depends(get_db)):
    new_blog = models.Blog1(title=request.title,desc=request.title)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog_list",response_model=schemas.ShowBlog,tags=['blogs'])
def blog_list(db:Session = Depends(get_db)):
    blogs_lst = db.query(models.Blog1).all()
    return blogs_lst


@app.get("/blog/{id}",response_model=List[schemas.ShowBlog],tags=['blogs'])
def blog_record(id,response:Response,db:Session = Depends(get_db)):
    blog = db.query(models.Blog1).filter(models.Blog1.id==id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not fias") 
    return blog    
    
@app.delete("/blog/delete/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def blog_delete(id:int,db:Session= Depends(get_db)):
    db.query(models.Blog1).filter(models.Blog1.id==id).delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.put("/blog/update/{id}",status_code=status.HTTP_404_NOT_FOUND,tags=['blogs'])
def blog_update(id,request:schemas.Blog1,db:Session = Depends(get_db)):
    db.query(models.Blog1).filter(models.Blog1.id==id).update({'title':request.title})
    db.commit()
    return 'updated'
    
     
    

@app.post("/user",response_model=schemas.UserResponse,tags=['users'])
def create_user(req: schemas.User,db:Session = Depends(get_db)):
    hased_password = Hash.bcrypt(req.password)
    new_user =  models.UserData(name=req.name,email=req.email,password=hased_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/user/id",response_model=schemas.UserResponse,tags=['users'])
def user(id,db:Session = Depends(get_db)):
    user = db.query(models.UserData).filter(models.UserData.id == id).first()
    return user    