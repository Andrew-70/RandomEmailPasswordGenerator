from flask import Flask, render_template
app = Flask(__name__)
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
