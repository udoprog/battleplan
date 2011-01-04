"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import types
from sqlalchemy.orm import relation
from battleplan.model.meta import Session, Base

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

def init_systems():
    systems = dict()
    
    for ss in Session.query(SolarSystem).all():
        systems[ss.solarSystemID] = ss;
    
    return systems;

def init_jumps():
    jumps = dict()
    
    for ssj in Session.query(SolarSystemJump).all():
        if ssj.fromSolarSystemID not in jumps:
            jumps[ssj.fromSolarSystemID] = list()
        jumps[ssj.fromSolarSystemID].append(ssj.toSolarSystemID)
    
    return jumps;

class Region(Base):
    __tablename__ = "mapRegions"

    regionID = sa.Column(types.Integer, primary_key=True)
    regionName = sa.Column(types.Unicode(100))

class Constellation(Base):
    __tablename__ = "mapConstellations"

    constellationID = sa.Column(types.Integer, primary_key=True)
    constellationName = sa.Column(types.Unicode(100))

class SolarSystem(Base):
    __tablename__ = "mapSolarSystems"
    #__mapper_args__ = dict(order_by="date desc")

    solarSystemID = sa.Column(types.Integer, primary_key=True)
    solarSystemName = sa.Column(types.Unicode(100))
    regionID = sa.Column(types.Integer, sa.ForeignKey("mapRegions.regionID"))
    region = relation(Region)
    constellationID = sa.Column(types.Integer, sa.ForeignKey("mapConstellations.constellationID"))
    constellation = relation(Constellation, lazy=False)
    security = sa.Column(types.Float)
    x = sa.Column(types.Float)
    y = sa.Column(types.Float)
    z = sa.Column(types.Float)
    
    @classmethod
    def by_name(klass, name):
        return Session.query(klass).filter(klass.solarSystemName == name)

    @classmethod
    def get(klass, id):
        return Session.query(klass).filter(klass.solarSystemID == id)

class SolarSystemJump(Base):
    __tablename__ = "mapSolarSystemJumps"
    #__mapper_args__ = dict(order_by="date desc")
    
    fromSolarSystemID = sa.Column(types.Integer, primary_key=True)
    toSolarSystemID = sa.Column(types.Integer, primary_key=True)

from battleplan.lib.types import id_column

import datetime

class Report(Base):
    __tablename__ = "reports"
    id = id_column("id")
    text = sa.Column(types.String(140))
    solarSystemID = sa.Column(types.Integer, sa.ForeignKey('mapSolarSystems.solarSystemID'))
    solarSystem = relation(SolarSystem)
    created = sa.Column(types.DateTime, default=datetime.datetime.now)

    @classmethod
    def by_solarsystem(klass, solarSystem):
        return Session.query(klass).filter(klass.solarSystem == solarSystem).order_by(klass.created.desc())
    
    def __init__(self):
        import uuid
        Base.__init__(self)
        self.id = uuid.uuid4()
