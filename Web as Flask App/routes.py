from flask import Blueprint, render_template

portfolio = Blueprint('portfolio', 
						__name__)

@portfolio.route('/')
def homepage():
	return render_template("index.html")

@portfolio.route('/projects/<project_name>')
def project(project_name):
	try:
		return render_template(project_name + ".html")
	except Exception as e:
		return str(e)