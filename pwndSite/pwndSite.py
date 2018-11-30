from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
	{
		'author': 'Holden Hewett',
		'title': 'Blog Test 1',
		'content': 'I have a hot wife!',
		'date_posted': 'November 16, 2018'
	},
	{
		'author': 'Bill Lumberg',
		'title': 'Blog Test 2',
		'content': "Yes, yes you do! And she's pregnant!",
		'date_posted': 'November 17, 2018'
	},
	{
		'author': 'Holden Hewett',
		'title': 'Blog Test 3',
		'content': "It's going to be a girl!",
		'date_posted': 'The future!!!! Ohhhhhhh'
	}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


#allows app to run directly from python cli inturpreter
if __name__ =='__main__':
    app.run(host='127.0.0.1',port='5001',debug=True)
