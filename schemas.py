from pydantic import BaseModel


class Book(BaseModel):
    id: int
    name: str
    isbn: str
    quantity: int
    class Config:
        schema_extra = {
            "example": {
                'id':0,
                'name': "name",
                'isbn': "isbn",
                'quantity': 0,
                }}

class Author(BaseModel):
    id: int
    name: str
    class Config:
        schema_extra = {
            "example": {
                'id':0,
                'name': "name",
                }}

class AuthorName(BaseModel):
    name: str
    class Config:
        schema_extra = {
            "example": {
                'name': "name",
                }}

class removeAuthor(BaseModel):
    id: int
    class Config:
        schema_extra = {
            "example": {
                'id': 0,
                }}