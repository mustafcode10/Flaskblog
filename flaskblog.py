from flask import Flask,render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'a4ac4fd2fb80d138ab8a3a7412132d09'

posts = [
    {
        'author':'Mustaf',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted': 'april 20, 2018'
    },

    {
        'author':'Ahmed',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted': 'april 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    # return "<h1>Home Page!<h1>"
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    # return "<h1>About Page!<h1>"   
    return render_template('about.html', title ='About')

@app.route("/register", methods =['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for  {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title ='Register', form = form)  
@app.route("/login")
def login():
    # return "<h1>About Page!<h1>" 
    form = LoginForm()
    return render_template('login.html', title ='Login', form = form)       


if __name__=='__main__':
    app.run(debug=True)