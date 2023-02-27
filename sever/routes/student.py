from fastapi import APIRouter
from schemas.student import Student
from config.db import conn
from models.index import student
from sqlalchemy import insert,update,delete

studentS = APIRouter()


@studentS.get('/api/students')
async def index():
    students = []
    for row in conn.execute(student.select()).fetchall():
        student_data = {
            'id': row.id,
            'name': row.name,
            'email': row.email,
            'age': row.age,
            'country': row.country
        }
        students.append(student_data)

    return {'data': students}


@studentS.get('/api/student/{id}')
async def fetchUser(id :int):
    students = []
    for row in conn.execute(student.select().where(student.c.id == id)).fetchall():
        student_data = {
            'id': row.id,
            'name': row.name,
            'email': row.email,
            'age': row.age,
            'country': row.country
        }
        students.append(student_data)

    return {'data': students}

@studentS.post('/api/student')
async def store(student_body:Student):
    stmt = (
        insert(student).
        values(
            name = student_body.name,
            email = student_body.email,
            age = student_body.age,
            country = student_body.country,
        )
    )   
    conn.execute(stmt)
    conn.commit()
    return True


@studentS.put('/api/student/{id}')
async def update_data(student_body:Student, id :int):
    stmt = (
        update(student).
        values(
            name = student_body.name,
            email = student_body.email,
            age = student_body.age,
            country = student_body.country,
        ).where(student.c.id == id)
    )
    conn.execute(stmt)
    conn.commit()


@studentS.delete('/api/student/{id}')
async def delete_data(id :int):
    stmt = (
    delete(student).
    where(student.c.id == id)
)
    conn.execute(stmt)
    conn.commit()