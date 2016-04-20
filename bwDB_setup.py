# Angad Singh April 13, 2016, P3 Item Catalog (Resume Catalog)
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

# For the sake of adding a personalized touch to the project and following
# the rubric I thought to create an online resume catalog, like an online
# job portal where instead of Items there are Resumes, the Catagories are
# Job Types.

Base = declarative_base()

class Person(Base):

	__tablename__ = 'person'

	id = Column(
		Integer, primary_key = True)

	phone = Column(
		Float(10), nullable = False, unique = True)

	name = Column(
		String(250), nullable = False)

	email = Column(
		String(250), nullable = False, unique = True)

	picture = Column(
		String(250))

	memberSince = Column(
		DateTime, default=datetime.datetime.utcnow)

	lastActive = Column(
		DateTime, onupdate=datetime.datetime.utcnow)

class Recruiter(Base):

	__tablename__ = 'recruiter'

	id = Column(
		Integer, primary_key = True)

	person_id = Column(
		Integer, ForeignKey('person.id'))
	person = relationship(Person)

	rating = Column(
		Float, default = -1)

	recruiterSince = Column(
		DateTime, default=datetime.datetime.utcnow)

	lastActive = Column(
		DateTime, onupdate=datetime.datetime.utcnow)

	lastUpload = Column(
		DateTime)

	TotalHelpers = Column(
		Integer, default = 0)



class Employer(Base):

	__tablename__ = 'employer'

	id = Column(
		Integer, primary_key = True)

	person_id = Column(
		Integer, ForeignKey('person.id'))
	person = relationship(Person)

	employerAddress = Column(
		String(250), nullable = False)

	employerPhone = Column(
		Float(10), nullable = False)

class Helper(Base):

	__tablename__ = 'helper'

	id = Column(
		Integer, primary_key = True)

	recruiter_id = Column(
		Integer, ForeignKey('recruiter.id'), nullable = False)
	recruiter = relationship(Recruiter)

	fName = Column(
		String(250), nullable = False)

	lName = Column(
		String(250), nullable = False)

	phone = Column(
		Float(10), nullable = False)

	DoB = Column(
		Date, nullable = False)

	languages = Column(
		String(80), nullable = False)

	education = Column(
		Integer(1), nullable = False)

	# 0 = Uneducated, 1 = Upto Class 10, 2 = Upto Class 12,
	# 3 = Attended College, 4 = Professionally Trained

	pJobTitle = Column(
		String(250))

	pJobLocation = Column(
		String(250))

	pJobDuration = Column(
		Integer(5))
	# Duration measured in Months

	currentAddress = Column(
		String(250), nullable = False)

	permanentAddress = Column(
		String(250), nullable = False)

	@property
	def serialize(self):
		return {
			'id':self.id,
			'recruiter_id':self.recruiter_id,
			'fName':self.fName,
			'lName':self.lName,
			'phone':self.phone,
			'DoB':self.DoB,
			'languages':self.languages,
			'education':self.education,
			'pJobTitle':self.pJobTitle,
			'pJobLocation':self.pJobLocation,
			'pJobDuration':self.pJobDuration,
			'currentAddress':self.currentAddress,
			'permanentAddress': self.permanentAddress
		}

class IdDoc(Base):

	__tablename__ = 'iddoc'

	id = Column(
		Integer, primary_key = True)

	helper_id = Column(
		Integer, ForeignKey('helper.id'))
	helper = relationship(Helper)

	ID_number = Column(
		String(80), nullable = False, unique = True)

	ID_type = Column(
		Integer(10), nullable = False)
	# ID_type Key:
	# 0 = ID Missing
	# 1 = Aadhar Card, 2 = Drivers Licence, 3 = ...
	ID_image = Column(
		String, nullable = False)

	ID_expiry = Column(
		Date)

class Reference(Base):

	__tablename__ = 'reference'

	id = Column(
		Integer, primary_key = True)

	helper_id = Column(
		Integer, ForeignKey('helper.id'))
	helper = relationship(Helper)

	refName = Column(
		String(250), nullable = False)

	refNumber = Column(
		Float(10), nullable = False)

	refRelation = Column(
		String(80), nullable = False)

class Account(Base):

	__tablename__ = 'account'

	accountNumber = Column(
		Float, primary_key = True)

	person_id = Column(
		Integer, ForeignKey('person.id'))
	person = relationship(Person)

	bankName = Column(
		String, nullable = False)

	bankBranch = Column(
		String, nullable = False)

	bankIFSC = Column(
		String, nullable = False)

	beneficiaryName = Column(
		String(80), nullable = False)

	beneficiaryPhNumber = Column(
		Float(10), nullable = False)

	billingAddress = Column(
		String(250), nullable = False)

class Job(Base):

	__tablename__ = 'job'

	id = Column(
		Integer, primary_key = True)

	helper_id = Column(
		Integer, ForeignKey('helper.id'))
	helper = relationship(Helper)

	jobSet = Column(
		Integer(4), nullable = False)

	taskParam_code = Column(
		String(350), nullable = False)
	# Format a string of task parameters for the job example below
	# Job(Cleaner)>Tasks(Dusting, Sweep/Mop, Clean Bathrooms, CarWash@500/month)
	#		= "DU+SM+CB+CW@500/Mth"
	# In the above
	# Task Letter Codes: DU = DUsing, SM = SweepMop, etc
	# Delimter: '+' indicates seperators between tasks
	# Parameters: 'CW@500/Mth' = Car Washing optional addition @ Rs.500/Month
	# Parameters: '?Special Needs Child Attendent' = '?' New Task called 'Special Needs Child Attendent' @ Rs.500/Hr
	# Job(Cook)>Tasks(Cook, Dusting, Sweep/Mop, ?newTask:SpecialNeeds)
	#		= "CO+DU+SM+?Special Needs Child Care"
	# Task Letter Codes: CO = COoking, DU, SM, '?' indicates custom task entry followed by task name.

	totalWage = Column(
		Integer(6), nullable = False)


class Task(Base):

	__tablename__ = 'task'

	id = Column(
		Integer, primary_key = True)

	job_id = Column(
		Integer, ForeignKey('job.id'))
	job = relationship(Job)

	task_Name = Column(
		String(80), nullable = False)

	task_code = Column(
		String(10), nullable = False)

	optional = Column(
		Integer(6))

	task_Metric = Column(
		String(25))



engine = create_engine('sqlite:///breadwinnerTester.db')
# will create a new file, similar to a new robust DB

Base.metadata.create_all(engine)
#this goes into the database and adds the class we will soon create in our new database