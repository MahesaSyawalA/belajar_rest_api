from app import app

@app.route('/')
def index():
    return 'hello flask ini testing api '