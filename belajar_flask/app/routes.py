from app import app
from app.controller import DosenController 

@app.route('/')
def index():
    return 'hello flask ini testing api '

@app.route('/dosen', methods=["GET"])
def dosens():
    return DosenController.index()

@app.route('/dosen/<id>', methods=["GET"])
def dosenDetail(id):
    return DosenController.detail(id)