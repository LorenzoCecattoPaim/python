from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATANASE_URI']='sqlite:///ecommerce.db'

db=SQLAlchemy(app)

#produto(id,nome,preço,descrição) TABELA
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price =  db.Column(db.Float, nullable=False)
    description= db.Column(db.Texte,nullable=True)
@app.route('/')
def helloWord():
    return 'Hello Word'

if __name__ == "__main__":
    app.run(debug=True)

