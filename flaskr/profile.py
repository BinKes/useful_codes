# -*- coding: UTF-8 -*-
from datetime import datetime
#from . import Base
from db import db
(Column, Table, String, Integer, DateTime)=(db.Column, db.Table, db.String, db.Integer, db.DateTime)

class Profile(db.Model):

  #__bind_key__ = 'T_Profile'
  __tablename__ = 'T_Profile'

  profileId = Column(Integer, primary_key=True)
  userId = Column(Integer)
  name = Column(String)
  gender = Column(Integer)
  birthday = Column(DateTime)

  @property
  def userInfo(self):
    userInfo = {}
    
    # birthday -> age
    if self.birthday == None:
      userInfo['age'] = None
    else:
      # may return invalid age e.g. age < 0 or age > 150
      # Calc will handle the error
      userInfo['age'] = (datetime.now() - self.birthday).days / 365
    
    # genderCode -> genderString
    if self.gender == 1:
      userInfo['gender'] = 'male'
    elif self.gender == 2:
      userInfo['gender'] = 'female'
    else:
      userInfo['gender'] = None
    
    return userInfo
