from contextlib import redirect_stderr
from flask import Flask, render_template, request, url_for, flash, redirect

app=Flask(__name__)
app.config['SECRET_KEY']='df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'

messages = [{'title': 'Message One',
            'content': 'Message One Content' },
            {'title': 'Message Two',
            'content': 'Message Two Content'}]

@app.route('/create/', methods=('GET', 'POST'))
def create():
      if request.method== 'POST':
            title= request.form['title']    
            content= request.form['content']
            
            if not title:
                  flash('Title is required!')
            elif not content:
                  flash('Content is required!')
            else:
                  messages.append({'title': title, 'content': content})
                  name = "Udhaya"
                  return redirect(url_for('index', messages=name ))

      return render_template('create.html')


@app.route('/')
def index():
      return render_template('index.html',messages=messages)

@app.route('/admin')
def hello_admin():
      return 'Hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
      return'Hello %s as Guest'%guest


