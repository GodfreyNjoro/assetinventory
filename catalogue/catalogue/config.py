import os


class Config:
	DEBUG = True
	SECRET_KEY='a4ee95e8dfb3e5aea17094865260e1b5'
	SQLALCHEMY_DATABASE_URI='mysql+pymysql://user:password@localhost:3306/site'
	SQLALCHEMY_ECHO = True
	