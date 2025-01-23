from app import app
from app.controller import DosenController 
from app.controller import UserController
from flask import request

@app.route('/')
def index():
    return 'hello flask ini testing api '

@app.route('/dosen', methods=["GET","POST"])
def dosens(): 
    if request.method == "GET":
        return DosenController.index()
    else:
        return DosenController.save()
    

@app.route('/dosen/<id>', methods=["GET", "PUT", "DELETE"])
def dosenDetail(id):
    if request.method == 'GET':
        return DosenController.detail(id)
    elif request.method == 'PUT':
        return DosenController.Update(id)
    else:
        return DosenController.Delete(id)
    
@app.route('/create-admin', methods=["POST"])
def users(): 
    # if request.method == "GET":
    #     return UserController.index()
    # else:
    return UserController.createAdmin()
    