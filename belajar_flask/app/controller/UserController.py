from app.model.user import User

from app import response, app, db
from flask import request

def createAdmin():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        level = 1

        input = [
            {
                "name" : name,
                "email" : email,
            }
        ]

        users = User( name=name, email=email, level=level )
        users.setPassword(password)
        
        db.session.add(users)
        db.session.commit()

        return response.success(input,'Admin successfully created')
    except Exception as e:
        print(e)