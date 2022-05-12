from typing import Optional
from pydantic import BaseModel, Field

class Book (BaseModel):
    id: int
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book",
                                    max_length=100,
                                    min_length=1)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Lovely Title",
                "author": "Ahamd Kd",
                "description": "One Lovely Description"
            }
        }


class BookNoID (BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book",
                                    max_length=100,
                                    min_length=1)

    class Config:
        schema_extra = {
            "example": {
                "title": "Lovely Title",
                "author": "Ahamd Kd",
                "description": "One Lovely Description"
            }
        }