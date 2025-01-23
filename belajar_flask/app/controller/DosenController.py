from app.model.dosen import Dosen

from app import response, app, db
from flask import request

def index():
    try:
        dosen = Dosen.query.all()
        data = formatArray(dosen)
        return response.success(data,'success')

    except Exception as e:
        print(e)

def formatArray(datas):
    array = []
    for i in datas:
         array.append(singleObject(i))
        
    return array

def singleObject(data):
    data = {
        'id':data.id,
        'idn': data.nidn,
        'nama': data.name,
        'phone': data.phone,
        'alamat': data.alamat,
    }

    return data