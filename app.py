from api import createApp
#from flask_sqlalchemy import SQLAlchemy


app = createApp()
    # add database
#app.app_context().push()
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////C:\\Developer\\Website\\moveables_app_backend_python2\\moveables_app_backend_python\\test.db'

#db = SQLAlchemy(app)
#class Users(db.Model):
#    key = db.Column(db.Integer, primary_key=True)
#    id = db.Column(db.String(80), unique=True, nullable=False)
#    password = db.Column(db.String(80), unique=True, nullable=False)
#    email = db.Column(db.String(120), unique=True, nullable=False)
#
#    def __repr__(self):
#        return f"User(id = {self.id}, password = {self.password}, email = {self.email}"


if __name__ == '__main__':
    app.run(debug=True)
