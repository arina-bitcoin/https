from flask import Blueprint


auth = Blueprint('auth', __name__)

@auth.route('/sign-in')
def sign_in():
    return '<p>Sign in</p>'

@auth.route('/sign-out')
def sign_out():
    return '<p>Sign out</p>'

@auth.route('/sign-up')
def sign_up():
    return '<p>Sign up</p>'