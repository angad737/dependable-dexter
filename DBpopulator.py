
# imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

# import DB Setup file
from bwDB_setup import Base, Person, Employer, Recruiter, Helper, Job, Task, Account, IdDoc, Reference

engine = create_engine('sqlite:///breadwinnerTester.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



################ Create Dummy Data ###################

# ACTION ITEM 1: Create Person

## Step 0: We currently have an empty miniworld in which there are no
## Entities. So we first must begin by creating our first Person

#creates a sample user
person1 = Person(name = "Angad Singh",
	phone = 9599240963,
	email = "angad737@gmail.com",
	picture = 'https://lh5.googleusercontent.com/-T-LHT-1l1xQ/AAAAAAAAAAI/AAAAAAAAAtA/WDx6C93qTrE/photo.jpg')
session.add(person1)
session.commit() # commits the created person to the DB

#creates a sample user
person1 = Person(name = "Ahsas Sharma",
	phone = 8146303333,
	email = "sharma.ahsas@gmail.com",
	picture = 'https://pbs.twimg.com/media/BybJmN2IcAALUuF.jpg')
session.add(person1)
session.commit() # commits the created person to the DB

person1 = Person(name = "Romit Humagai",
	phone = 6032898238,
	email = "romitdevilsworld@hotmail.com",
	picture = 'http://s3-us-west-2.amazonaws.com/docjokes-com/i/a6/ce/1f/c6/13/oh-hell-no-meme-5058-oh-no-meme-memeshappen_original.jpg?1446204510')
session.add(person1)
session.commit() # commits the created person to the DB

## Step 1.0: Now that we have at least one person on the platform, we can
## allow them to register to become recruiters

# the we first search for the person who wishes to become a recruiter
# in the Person database by name
newRecruit = session.query(Person).filter_by(name = 'Angad Singh').one()
Recruiter1 = Recruiter(person_id = newRecruit.id)
session.add(Recruiter1)
session.commit() # commits the created recruiter to the DB

newRecruit = session.query(Person).filter_by(name = 'Ahsas Sharma').one()
Recruiter1 = Recruiter(person_id = newRecruit.id)
session.add(Recruiter1)
session.commit() # commits the created recruiter to the DB

## Step 1.1: Now that we have registered the recruiter, we must register their
## Account
newRecruit = session.query(Person).filter_by(name = 'Angad Singh').one()
Account1 = Account(accountNumber = 1234123412341234,
	person_id = newRecruit.id,
	bankName = "ICICI Bank",
	bankBranch = "Gurgaon Sector 14",
	bankIFSC = "WXYZ123",
	beneficiaryName = "Angad Singh",
	beneficiaryPhNumber = 9599240963,
	billingAddress = "963 Sec 17B, Gurgaon, HR, 122001")
session.add(Account1)
session.commit()

newRecruit = session.query(Person).filter_by(name = 'Ahsas Sharma').one()
Account1 = Account(accountNumber = 4567456745674567,
	person_id = newRecruit.id,
	bankName = "HDFC Bank",
	bankBranch = "Nangal Central ",
	bankIFSC = "HDFCIFSC",
	beneficiaryName = "Ahsas Sharma",
	beneficiaryPhNumber = 9599240963,
	billingAddress = "HNo X, Nangal, PJ, 948845")
session.add(Account1)
session.commit()

# Step 2.0: Now that we have registered recruiters we may begin to upload
# Helpers onto the platform


################ HELPER DATA LOADING BEGINS HERE###################
##############-------------------------------------################
##########-----------------------------------------------##########

#$$$$$$$$$$$Start ----------------- Upload Naresh the Destroyer
recruit = session.query(Recruiter).filter_by(id = 1).one()
helper1 = Helper(recruiter_id = recruit.id,
	fName = "Naresh",
	lName = "The Destroyer",
	phone = 8860663620,
	DoB = date(1973,5,21),
	languages = "AD",
	education = 1,
	pJobTitle = "Security Guard",
	pJobLocation = "Maruti Factory, Gurgaon",
	pJobDuration = 48,
	currentAddress = "87/3 Sukhrali, Gurgaon, HR",
	permanentAddress = "169 Destroyerville, Bhand, UP")
session.add(helper1)
session.commit()

## Step 2.1: Refrences-------BR-Ref:2 refrences per helper------------

newHelper = session.query(Helper).filter_by(id = 1).one()
ref1 = Reference(helper_id = newHelper.id,
	refName = "Neena Singh",
	refNumber = 9811265444,
	refRelation = "Boss")
session.add(ref1)

ref2 = Reference(helper_id = newHelper.id,
	refName = "Suresh the Destroyer",
	refNumber = 8860666612,
	refRelation = "Daddy Destroyer")
session.add(ref2)
session.commit()

## Step 2.2: IdDoc----------BR-Id1 Validate ID Type, Approve Image Clarity, ID_validity

IdDoc1 = IdDoc(helper_id = newHelper.id,
	ID_number = "ABCD1234",
	ID_type = 2,
	ID_image = 'http://innovativenurse.com/wp-content/uploads/2012/03/mclovin_license.jpg',
	ID_expiry = date(2008,06,03))
session.add(IdDoc1)
session.commit()

## Step 2.3: Job
# jobSet Key:
# 1 = Cleaning, 2 = Cooking, 3 = Assistant

job1 = Job(helper_id = newHelper.id,
	jobSet = 1,
	totalWage = 6000)
session.add(job1)
session.commit()

job1 = session.query(Job).filter_by(helper_id = newHelper.id).one()
task1 = Task(job_id = job1.id,
	task_Name = "Dusting")
session.add(task1)
task2 = Task(job_id = job1.id,
	task_Name = "Sweeping/Mopping")
session.add(task2)
task3 = Task(job_id = job1.id,
	task_Name = "Cleaning Bathrooms")
session.add(task3)
session.commit()

job2 = Job(helper_id = newHelper.id,
	jobSet = 2,
	totalWage = 8000)
session.add(job2)
session.commit()

job2 = session.query(Job).filter_by(helper_id = newHelper.id, jobSet = 2).one()
task1 = Task(job_id = job2.id,
	task_Name = "Dusting")
session.add(task1)
task2 = Task(job_id = job2.id,
	task_Name = "Sweeping/Mopping")
session.add(task2)
task3 = Task(job_id = job2.id,
	task_Name = "Cleaning Bathrooms")
session.add(task3)
session.commit()

## Now that we have created a Helper complete with IdDocs, Refrences
########## END--------------------Upload Naresh est Fini
#########

#########
########## Start ----------------- Upload Amarnath
recruit = session.query(Recruiter).filter_by(id = 2).one()
helper1 = Helper(recruiter_id = recruit.id,
	fName = "Amarnath",
	lName = "The Voyeager",
	phone = 8800112233,
	DoB = date(1978,3,20),
	languages = "A1P",
	education = 3,
	pJobTitle = "Chauffeur",
	pJobLocation = "American Embessey",
	pJobDuration = 60,
	currentAddress = "394 Brigade Colony, Nangal, PJ",
	permanentAddress = "149 Voyageville, Ryder, PJ")
session.add(helper1)
session.commit()

## Step 2.1: Refrences

newHelper = session.query(Helper).filter_by(id = 1).one()
ref1 = Reference(helper_id = newHelper.id,
	refName = "Neena Singh",
	refNumber = 9811265444,
	refRelation = "Boss")
session.add(ref1)

ref2 = Reference(helper_id = newHelper.id,
	refName = "Suresh the Destroyer",
	refNumber = 8860666612,
	refRelation = "Daddy Destroyer")
session.add(ref2)
session.commit()

## Step 2.2: IdDoc

IdDoc1 = IdDoc(helper_id = newHelper.id,
	ID_number = "ABCD1234",
	ID_type = 2,
	ID_image = 'http://innovativenurse.com/wp-content/uploads/2012/03/mclovin_license.jpg',
	ID_expiry = date(2008,06,03))
session.add(IdDoc1)
session.commit()

## Step 2.3: Job

job1 = Job(helper_id = newHelper.id,
	jobSet = 1,
	totalWage = 6000)
session.add(job1)
session.commit()

job1 = session.query(Job).filter_by(helper_id = newHelper.id).one()
task1 = Task(job_id = job1.id,
	task_Name = "Dusting")
session.add(task1)
task2 = Task(job_id = job1.id,
	task_Name = "Sweeping/Mopping")
session.add(task2)
task3 = Task(job_id = job1.id,
	task_Name = "Cleaning Bathrooms")
session.add(task3)
session.commit()

job2 = Job(helper_id = newHelper.id,
	jobSet = 2,
	totalWage = 8000)
session.add(job2)
session.commit()

job2 = session.query(Job).filter_by(helper_id = newHelper.id, jobSet = 2).one()
task1 = Task(job_id = job2.id,
	task_Name = "Dusting")
session.add(task1)
task2 = Task(job_id = job2.id,
	task_Name = "Sweeping/Mopping")
session.add(task2)
task3 = Task(job_id = job2.id,
	task_Name = "Cleaning Bathrooms")
session.add(task3)
session.commit()

## Now that we have created a Helper complete with IdDocs, Refrences

# Start New Helper
recruit = session.query(Recruiter).filter_by(id = 2).one()
helper1 = Helper(recruiter_id = recruit.id,
	fName = "Happy",
	lName = "Himesh",
	phone = 5002002777,
	DoB = date(1985,5,10),
	languages = "A1D",
	education = 2,
	pJobTitle = "Medical Assistant",
	pJobLocation = "Suroor Hospital",
	pJobDuration = 8,
	currentAddress = "22 TeraTera, Suroor, MH",
	permanentAddress = "33 MeraTera, Suroor, MH")
session.add(helper1)
session.commit()

## Step 2.1: Refrences

newHelper = session.query(Helper).filter_by(id = 1).one()
ref1 = Reference(helper_id = newHelper.id,
	refName = "Neena Singh",
	refNumber = 9811265444,
	refRelation = "Boss")
session.add(ref1)

ref2 = Reference(helper_id = newHelper.id,
	refName = "Suresh the Destroyer",
	refNumber = 8860666612,
	refRelation = "Daddy Destroyer")
session.add(ref2)
session.commit()

## Step 2.2: IdDoc

IdDoc1 = IdDoc(helper_id = newHelper.id,
	ID_number = "ABCD1234",
	ID_type = 2,
	ID_image = 'http://innovativenurse.com/wp-content/uploads/2012/03/mclovin_license.jpg',
	ID_expiry = date(2008,06,03))
session.add(IdDoc1)
session.commit()

## Step 2.3: Job

job1 = Job(helper_id = newHelper.id,
	jobSet = 1,
	totalWage = 6000)
session.add(job1)
session.commit()

job1 = session.query(Job).filter_by(helper_id = newHelper.id).one()
task1 = Task(job_id = job1.id,
	task_Name = "Dusting")
session.add(task1)
task2 = Task(job_id = job1.id,
	task_Name = "Sweeping/Mopping")
session.add(task2)
task3 = Task(job_id = job1.id,
	task_Name = "Cleaning Bathrooms")
session.add(task3)
session.commit()

job2 = Job(helper_id = newHelper.id,
	jobSet = 2,
	totalWage = 8000)
session.add(job2)
session.commit()

job2 = session.query(Job).filter_by(helper_id = newHelper.id, jobSet = 2).one()
task1 = Task(job_id = job2.id,
	task_Name = "Dusting")
session.add(task1)
task2 = Task(job_id = job2.id,
	task_Name = "Sweeping/Mopping")
session.add(task2)
task3 = Task(job_id = job2.id,
	task_Name = "Cleaning Bathrooms")
session.add(task3)
session.commit()

## Now that we have created a Helper complete with IdDocs, Refrences
########## END--------------------Upload Amarnath
#########

#########
########## Start ----------------- Upload Seema

recruit = session.query(Recruiter).filter_by(id = 2).one()
helper1 = Helper(recruiter_id = recruit.id,
	fName = "Sincere",
	lName = "Seema",
	phone = 9949202832,
	DoB = date(1981,9,30),
	languages = "AK",
	education = 2,
	pJobTitle = "Maid",
	pJobLocation = "144 Sector 15, Noida, UP",
	pJobDuration = 32,
	currentAddress = "4895 SincereFolk, Jalandhar, PJ",
	permanentAddress = "149 Helperville, Weezy, HP")
session.add(helper1)
session.commit()

## Step 2.1: Refrences

newHelper = session.query(Helper).filter_by(id = 1).one()
ref1 = Reference(helper_id = newHelper.id,
	refName = "Neena Singh",
	refNumber = 9811265444,
	refRelation = "Boss")
session.add(ref1)

ref2 = Reference(helper_id = newHelper.id,
	refName = "Suresh the Destroyer",
	refNumber = 8860666612,
	refRelation = "Daddy Destroyer")
session.add(ref2)
session.commit()

## Step 2.2: IdDoc

IdDoc1 = IdDoc(helper_id = newHelper.id,
	ID_number = "ABCD1234",
	ID_type = 2,
	ID_image = 'http://innovativenurse.com/wp-content/uploads/2012/03/mclovin_license.jpg',
	ID_expiry = date(2008,06,03))
session.add(IdDoc1)
session.commit()

## Step 2.3: Job

job1 = Job(helper_id = newHelper.id,
	jobSet = 1,
	totalWage = 6000)
session.add(job1)
session.commit()

job1 = session.query(Job).filter_by(helper_id = newHelper.id).one()
task1 = Task(job_id = job1.id,
	task_Name = "Dusting")
session.add(task1)
task2 = Task(job_id = job1.id,
	task_Name = "Sweeping/Mopping")
session.add(task2)
task3 = Task(job_id = job1.id,
	task_Name = "Cleaning Bathrooms")
session.add(task3)
session.commit()

job2 = Job(helper_id = newHelper.id,
	jobSet = 2,
	totalWage = 8000)
session.add(job2)
session.commit()

job2 = session.query(Job).filter_by(helper_id = newHelper.id, jobSet = 2).one()
task1 = Task(job_id = job2.id,
	task_Name = "Dusting")
session.add(task1)
task2 = Task(job_id = job2.id,
	task_Name = "Sweeping/Mopping")
session.add(task2)
task3 = Task(job_id = job2.id,
	task_Name = "Cleaning Bathrooms")
session.add(task3)
session.commit()

## Now that we have created a Helper complete with IdDocs, Refrences
## Step 2 (cont): Now that we have a registered helper we may create
## - (2.1) Refrences
## - (2.2) IdDoc
## - (2.3) Job

## Step 2.1: Refrences

newHelper = session.query(Helper).filter_by(id = 1).one()
ref1 = Reference(helper_id = newHelper.id,
	refName = "Neena Singh",
	refNumber = 9811265444,
	refRelation = "Boss")
session.add(ref1)

ref2 = Reference(helper_id = newHelper.id,
	refName = "Suresh the Destroyer",
	refNumber = 8860666612,
	refRelation = "Daddy Destroyer")
session.add(ref2)
session.commit()

## Step 2.2: IdDoc

IdDoc1 = IdDoc(helper_id = newHelper.id,
	ID_number = "ABCD1234",
	ID_type = 2,
	ID_image = 'http://innovativenurse.com/wp-content/uploads/2012/03/mclovin_license.jpg',
	ID_expiry = date(2008,06,03))
session.add(IdDoc1)
session.commit()

## Step 2.3: Job

job1 = Job(helper_id = newHelper.id,
	jobSet = 1,
	totalWage = 6000)
session.add(job1)
session.commit()

job1 = session.query(Job).filter_by(helper_id = newHelper.id).one()
task1 = Task(job_id = job1.id,
	task_Name = "Dusting")
session.add(task1)
task2 = Task(job_id = job1.id,
	task_Name = "Sweeping/Mopping")
session.add(task2)
task3 = Task(job_id = job1.id,
	task_Name = "Cleaning Bathrooms")
session.add(task3)
session.commit()

job2 = Job(helper_id = newHelper.id,
	jobSet = 2,
	totalWage = 8000)
session.add(job2)
session.commit()

job2 = session.query(Job).filter_by(helper_id = newHelper.id, jobSet = 2).one()
task1 = Task(job_id = job2.id,
	task_Name = "Dusting")
session.add(task1)
task2 = Task(job_id = job2.id,
	task_Name = "Sweeping/Mopping")
session.add(task2)
task3 = Task(job_id = job2.id,
	task_Name = "Cleaning Bathrooms")
session.add(task3)
session.commit()

## Now that we have created a Helper complete with IdDocs, Refrences
## Jobs and Tasks