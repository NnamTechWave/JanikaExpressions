import hashlib
from flask import Flask, jsonify, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import string


# Import the config
app = Flask(__name__)
app.config.from_object('config')
mysql = MySQL(app)

@app.route('/') 
def index():
    return render_template('index.html')
    # if 'user_id' in session:
    #     return render_template('home.html', username=session['username'])
    # return render_template('index.html', username=None)


# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         reg_code = request.form['reg_code']
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
        
#         if reg_code not in codes:
#             flash('Invalid code', 'error')
#             return redirect(url_for('signup'))
        
#         code_details = codes[reg_code]
        
#         if code_details['used']:
#             flash('Code already used', 'error')
#             return redirect(url_for('signup'))
        
#         if datetime.now() > code_details['expiration_date']:
#             flash('Code expired', 'error')
#             return redirect(url_for('signup'))
        
#         hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
#         try:
#             cursor = mysql.connection.cursor()
#             cursor.execute('SELECT id FROM users WHERE username = %s OR email = %s', (username, email))
#             existing_user = cursor.fetchone()
            
#             if existing_user:
#                 flash('Username or email already exists', 'error')
#                 return redirect(url_for('signup'))
            
#             cursor.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s)', (username, hashed_password, email))
#             mysql.connection.commit()
#             cursor.close()
            
#             # Mark the code as used
#             codes[reg_code]['used'] = True
            
#             flash('Signup successful!', 'success')
#             return redirect(url_for('login'))
#         except Exception as e:
#             flash('Error during signup: ' + str(e), 'error')
#             return redirect(url_for('signup'))
    
#     return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT id FROM users WHERE username = %s AND password = %s', (username, hashed_password))
            user = cursor.fetchone()
            cursor.close()

            if user:
                session['user_id'] = user[0]
                session['username'] = username
                flash('Login successful!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid username or password', 'error')
        except Exception as e:
            flash('Error during login: ' + str(e), 'error')
    
    return render_template('login.html')

# @app.route('/logout')
# def logout():
#     session.pop('user_id', None)
#     session.pop('username', None)
#     flash('You were logged out.', 'success')
#     return redirect(url_for('index'))

@app.route('/FAQ')
def FAQ():
    return render_template('faqS.html')

@app.route('/Meet_Janika')
def Meet_Janika():
    return render_template('meet_janika.html')

# privacy
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')
if __name__ == '__main__':
    app.run(debug=True)
