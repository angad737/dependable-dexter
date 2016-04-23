
from flask import Flask, render_template, url_for
app = Flask(__name__)

from bwDB_setup import Base, Person, Recruiter, Employer, Helper, Job
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB ##
engine = create_engine('sqlite:///breadwinnerTester.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/index')
def HelloWorld():
    helper = session.query(Helper).all()
    jobs = session.query(Job).all()
    print "" + url_for('static', filename='img/agency-img.jpg')
    return render_template('index.html', helper=helper, jobs=jobs)

@app.route('/helper/<int:helper_id>')
def showHelper(helper_id):
	helper = session.query(Helper).filter_by(id=helper_id).one()
	output = ''
	output += "Name: " + helper.fName + " " + helper.lName + '</br>'
	output += "Recruiter ID: " + str(helper.recruiter_id) + '</br>'
	output += "Phone: " + str(helper.phone) + '</br>'
	output += "DoB: " + str(helper.DoB) + '</br>'
	output += "Languages" + helper.languages + '</br>'

	return output

@app.route('/browse')
def showHelpers():
	return "You have reached the page where users will browse Helper Profiles"

@app.route('/recruiterlogin')
def recruiterLogin():
	return "You have reached the page where users will Sign In or Sign Up to access Recruiter previlages"

@app.route('/recruiter/signup')
def recruiterSignup():
	return "Here the user will register by providing information necessary to become a recruiter"

@app.route('/interview')
def setInterview():
	return "Here we collect Employer Info, Interview Info and Payment Info"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)