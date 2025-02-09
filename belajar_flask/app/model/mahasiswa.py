from app import db
from app.model.dosen import Dosen

class Mahasiswa(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nim = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    phone = db.Column(db.String(250), nullable=False)
    alamat = db.Column(db.String(250), nullable=False)
    dosen_satu = db.Column(db.BigInteger, db.ForeignKey(Dosen.id, ondelete='CASCADE'))
    dosen_dua = db.Column(db.BigInteger, db.ForeignKey(Dosen.id,  ondelete='CASCADE'))
    

    def __repr__(self):
        return '<Mahasiswa {}>'.format(self.name)