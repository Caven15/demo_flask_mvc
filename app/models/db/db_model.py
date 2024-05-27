from sqlalchemy import Boolean, Integer, String, Column
from sqlalchemy.orm import declarative_base

base = declarative_base()

class Utilisateur(base):
    __tablename__ = 'utilisateur'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(35), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    statut_compte = Column(Boolean, default=True)