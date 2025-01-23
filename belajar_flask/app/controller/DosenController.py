from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa

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
        'nidn': data.nidn,
        'nama': data.name,
        'phone': data.phone,
        'alamat': data.alamat,
    }

    return data

def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id))

        if not dosen:
            return response.badRequest([],'Not Found')
        
        dataMahasiswa = formatMahasiswa(mahasiswa)
        data = singleDetailMahasiswa(dosen,dataMahasiswa)

        return response.success(data,'success')
    
    except Exception as e:
        print(e)
    
def singleDetailMahasiswa(dosen, mahasiswa):
    data = {
        'id' : dosen.id,
        'nidn':dosen.nidn,
        'nama':dosen.name,
        'phone':dosen.phone,
        'alamat':dosen.alamat,
        'mahasiswa':mahasiswa,
    }

    return data




def singleMahasiswa(mahasiwa):
    data = {
        'id':mahasiwa.id,
        'nim': mahasiwa.nim,
        'nama': mahasiwa.name,
        'phone': mahasiwa.phone,
        'alamat': mahasiwa.alamat,
    }

    return data

def formatMahasiswa(data):
    array = []
    for i in data:
        array.append(singleMahasiswa(i))

    return array


def save():
    try:
        nidn = request.form.get('nidn')
        name = request.form.get('name')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        input = [
            {
                "nidn" : nidn,
                "name" : name,
                "phone" : phone,
                "alamat" : alamat,
            }
        ]

        dosens = Dosen(nidn=nidn, name=name, phone=phone, alamat=alamat )
        db.session.add(dosens)
        db.session.commit()

        return response.success(input,'Data successfully created')
    except Exception as e:
        print(e)


# update data
def Update(id):
    try:
        nidn  = request.form.get('nidn')
        name = request.form.get('name')
        phone = request.form.get('phone')
        alamat = request.form.get('alamat')

        input = [
            {
                "nidn" : nidn,
                "name" : name,
                "phone" : phone,
                "alamat" : alamat,
            }
        ]

        dosen = Dosen.query.filter_by(id=id).first()

        dosen.nidn = nidn
        dosen.name = name
        dosen.phone = phone
        dosen.alamat = alamat

        db.session.commit()

        return response.success(input,"succes update data")
    
    except Exception as e:
        print(e)

# delete data
def Delete(id):
    try: 
        dosen = Dosen.query.filter_by(id=id).first()

        if not dosen:
            return response.badRequest([],"Not Found")
        
        db.session.delete(dosen)
        db.session.commit()
        
        return response.success('','Successfully deleting data')
    
    except Exception as e:
        print(e)
