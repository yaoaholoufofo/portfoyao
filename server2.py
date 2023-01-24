
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

#Temolate route fuction
@app.route("/index.html")
def my_home():
    return render_template('index.html')


#@app.route("/<string:page_name>")
#def html_page(page_name):
    #return render_template('page_name')

#Temolate route fuction
@app.route("/about.html")
def about():
    return render_template('about.html')

#Temolate route fuction
@app.route("/works.html")
def works():
    return render_template('works.html')

#Temolate route fuction
@app.route("/work.html")
def work():
    return render_template('work.html')

#Temolate route fuction
@app.route("/contact.html")
def contact_pg():
    return render_template('contact.html')

#Temolate route fuction
@app.route("/thankyou.html")
def thank_you():
    return render_template('thankyou.html')

#Storage data to txt file function
def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject=  data['subject']
		message =  data['message']
		file = database.write(f'\n{email},{subject},{message}')

#Storage data to csv file function
def write_to_csv(data):
	with open('database.csv',newline='', mode='a') as database2:
		email = data['email']
		subject=  data['subject']
		message =  data['message']
		csv_writer = csv.writer(database2, delimiter =',', quotechar='"', quoting= csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])


#Data posted capture function
#@app.route('/submit_form', methods=['POST', 'GET'])
#def submit_form():
	#if request.method == 'POST':
		#data = request.form.to_dict()
		#write_to_csv(data)
		#return redirect('/thankyou.html')
	#else:
		#return 'somethink went wrong. Try again!'
    
#Data posted capture function
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'did not save to database'
	else:
		return 'something went wrong. Try again'
		
    