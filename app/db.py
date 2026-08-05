#ORM (Object realational mapping): Instead of using sql code allows us to write python code to retrieve data
from collections.abc import AsyncGenerator
import uuid

from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncConnection, create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime

DATABASE_URL = "sqlite+aiosqlite:///./test.db" #This is a local database, we set up this to get it running
#If we decide to change to a another production data base we just need to change this

#For some reason we cannot inherit directly from Base, but we need the base so that we can use it 
class Base(DeclarativeBase):
    pass

#Our schemas or classes would normally be in another file for the sake of organization
class Post(Base): #Inherits from Declarativebase so it knows we are making a data model
    __tablename__ = "posts"
    #
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    caption = Column(Text)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

#This is what actually creates the database
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

#Creates the databases and the tables
async def create_db_and_tables():
    async with engine.begin() as conn:#Starts it 
        await conn.run_sync(Base.metadata.create_all) #And creates the tables

#This gives us a session where we can read and write stuff in the database
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

