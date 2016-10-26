# -*- coding: UTF-8 -*-
from datetime import datetime
#from . import Base
from db import db
#db.create_all(bind=['T_Profile'])

class Profile(db.Model):

  #__bind_key__ = 'T_Profile'
  __tablename__ = 'T_Profile'

  profileId = db.Column(db.Integer, primary_key=True)
  userId = db.Column(db.Integer)
  name = db.Column(db.String)
  gender = db.Column(db.Integer)
  birthday = db.Column(db.DateTime)

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
