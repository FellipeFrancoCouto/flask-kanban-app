#  Import relevant libraries
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from flask import Flask, render_template, request, redirect

db = SQLAlchemy()



class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Task %r>, content %r, status %r' % (self.id, self.content, self.status)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

    app.app_context().push()
    db.init_app(app)

    db.create_all()

    @app.route('/', methods=['POST', 'GET'])
    def index():
        if request.method == 'POST':
            task_content = request.form['content']
            new_task = Todo(content=task_content, status=0)

            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect('/')
            except Exception as e:
                return e
        else:
            tasks = Todo.query.order_by(Todo.date_created).all()
            print(tasks)
            return render_template('index.html', tasks=tasks)

    @app.route('/delete/<int:id>')
    def delete(id):
        task_to_delete = Todo.query.get_or_404(id)
        try:
            db.session.delete(task_to_delete)
            db.session.commit()
            return redirect('/')
        except:
            return 'Failure to delete task'

    @app.route('/update/<int:id>', methods=['GET', 'POST'])
    def update(id):
        task = Todo.query.get_or_404(id)

        if request.method == 'POST':
            task.content = request.form['content']

            try:
                db.session.commit()
                return redirect('/')
            except:
                return 'Failure to update your task'

        else:
            return render_template('update.html', task=task)

    @app.route('/statusChange/<int:id>', methods=['POST'])
    def statuschange(id):
        task = Todo.query.get_or_404(id)
        task.status = request.form['status']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Failure to change the status of your task'

        else:
            return redirect('/')
    return app


