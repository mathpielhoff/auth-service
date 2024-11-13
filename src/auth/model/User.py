from sqlalchemy import Column, Integer, String, Sequence
from shared_lib.utils.db_utils import Base

# Define a sequence for tenant IDs
tenant_id_seq = Sequence('tenant_id_seq', start=1000, increment=1)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)
    tenant_id = Column(Integer,  tenant_id_seq)