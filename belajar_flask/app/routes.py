from app import app
from app.controller import DosenController 

@app.route('/')
def index():
    return 'hello flask ini testing api '

@app.route('/dosen', methods=["GET"])
def dosens():
    return DosenController.index()