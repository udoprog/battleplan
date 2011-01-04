"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import types
from battleplan.model.meta import Session, Base

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

def init_systems():
    from battleplan.lib import systems, system_names
    
    for ss in Session.query(SolarSystem).all():
        systems[ss.solarSystemID] = ss;
        system_names.append(ss.solarSystemName)

    return systems;

def init_jumps():
    from battleplan.lib import jumps
    
    for ssj in Session.query(SolarSystemJump).all():
        if ssj.fromSolarSystemID not in jumps:
            jumps[ssj.fromSolarSystemID] = list()
        jumps[ssj.fromSolarSystemID].append(ssj.toSolarSystemID)
    
    return jumps;

class SolarSystem(Base):
    __tablename__ = "mapSolarSystems"
    #__mapper_args__ = dict(order_by="date desc")

    solarSystemID = sa.Column(types.Integer, primary_key=True)
    solarSystemName = sa.Column(types.Unicode(100))
    regionID = sa.Column(types.Integer)
    constellationID = sa.Column(types.Integer)
    security = sa.Column(types.Float)
    x = sa.Column(types.Float)
    y = sa.Column(types.Float)
    z = sa.Column(types.Float)

class SolarSystemJump(Base):
    __tablename__ = "mapSolarSystemJumps"
    #__mapper_args__ = dict(order_by="date desc")
    
    fromSolarSystemID = sa.Column(types.Integer, primary_key=True)
    toSolarSystemID = sa.Column(types.Integer, primary_key=True)
