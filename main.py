from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import InputRequired, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.secret_key = 'BoyanSevina'


class UserForm(FlaskForm):
    email = StringField("Email", [InputRequired("Please enter your name.")])
    password = PasswordField("Password", [InputRequired("Please enter your password.")])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = UserForm(request.form)
    if form.validate():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)