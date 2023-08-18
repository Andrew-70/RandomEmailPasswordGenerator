from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '804e4596a49c080116aae06d6663081a'

posts = [
    {
        'author': 'Bugie',
        'title': 'web development with flask',
        'content': 'using templates',
        'date_posted': 'August 14, 2023'
    },
{
        'author': 'Ros',
        'title': 'test automation',
        'content': 'using selenium',
        'date_posted': 'August 14, 2023'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)