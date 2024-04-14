from fastapi import FastAPI
from db import init_db
from api.routes import api_router
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Kreiranje SQLite engine-a
engine = create_engine('sqlite:///vozni_park.db')

# Definisanje Base klase za deklarativno definisanje modela
Base = declarative_base()

# Session maker za interakciju sa bazom
Session = sessionmaker(bind=engine)
session = Session()

# Inicijalizujte bazu podataka kada aplikacija počne sa radom
@app.on_event("startup")
def startup_event():
    init_db()  

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Dodavanje ruta
app.include_router(api_router)
