from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
import email_validator
from wtforms.validators import DataRequired, Email, Length, email_validator



class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(message="Invalid email")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message="Password must be 8 characters long.")])
    submit = SubmitField("Login")

app = Flask(__name__)
app.secret_key = "hawernasdofnwem"

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email.data)
    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)