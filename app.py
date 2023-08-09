from flask import Flask, flash, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb
import re

app = Flask(__name__)
app.secret_key = 'dbmsproject2023'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ahsan123'
app.config['MYSQL_DB'] = 'app'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'email' in request.form:
            email = request.form['email']

            # Validate the email (optional)
            if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                flash('Invalid email format', 'error')
            else:
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('insert into newsletter (email) values (%s)', (email,))
                mysql.connection.commit()
                cursor.close()
                flash('Successfully Subscribed!', 'success')

        # Handle other forms in the footer
        cname = request.form.get('cname')
        ccontact = request.form.get('ccontact')
        csubject = request.form.get('csubject')
        cmessage = request.form.get('cmessage')

        if cname and ccontact and csubject and cmessage:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO contact (cname, ccontact, csubject, cmessage) VALUES (%s, %s, %s, %s)',
                           (cname, ccontact, csubject, cmessage))
            mysql.connection.commit()
            cursor.close()

            message = "Your Message has been sent"

            return render_template('index.html', message=message)

    return render_template("index.html")
	
@app.route('/Balochistan')
def balochistan():
	return render_template('Balochistan.html')

@app.route('/kpk')
def kpk():
	return render_template('kpk.html')

@app.route('/Malaysia')
def Malaysia():
	return render_template('Malaysia-details.html')

@app.route('/NorthernAreas')
def NorthernAreas():
	return render_template('NorthernAreas-details.html')

@app.route('/Punjab')
def punjab():
	return render_template('Punjab.html')

@app.route('/Sindh')
def sindh():
	return render_template('Sindh.html')

@app.route('/Singapore')
def singapore():
	return render_template('Singapore-details.html')

@app.route('/Thailand')
def thailand():
	return render_template('Thailand-details.html')

@app.route('/Turkey')
def turkey():
	return render_template('Turkey-details.html')

@app.route('/UAE')
def uae():
	return render_template('uae-details.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    global userid
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s AND pass_word = %s', (username, password))
        account = cursor.fetchone()
        print(account)

        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            userid = account[0]
            session['fullname'] = account[1]
            session['username'] = account[2]
            session['password'] = account[3]
            print(userid)
            print(session['fullname'])
            # JavaScript alert for successful login
            success_alert = '''
            <script>
                alert('Login successful');
                window.location.href = '/dashboard';
            </script>
            '''
            return success_alert
        else:
            # JavaScript alert for incorrect username or password
            error_alert = '''
            <script>
                alert('Incorrect username or password!');
                window.location.href = '/login';  // Redirect back to the login page
            </script>
            '''
            return error_alert

    return render_template('login.html', msg=msg)




@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'full-name' in request.form:
        rusername = request.form['username']
        rpassword = request.form['password']
        rfullname = request.form['full-name']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s', (rusername,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[A-Za-z]', rfullname):
            msg = 'Invalid Fullname!'
        elif not re.match(r'[A-Za-z0-9]+', rusername):
            msg = 'Username must contain only characters and numbers!'
        elif not rusername or not rpassword or not rfullname:
            msg = 'Please fill out the form!'
        else:
            cursor.execute('INSERT INTO users (id, username, pass_word, fullname) VALUES (NULL, %s, %s, %s)',
                           (rusername, rpassword, rfullname,))
            mysql.connection.commit()
            
            # JavaScript alert for successful registration
            success_alert = '''
            <script>
                alert('Registration successful. Please log in.');
                window.location.href = '/login';
            </script>
            '''
            return success_alert
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('Signup.html', msg=msg)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'loggedin' in session:
        user_id = session['id']
        if request.method == 'POST':  # Check if it's a POST request
            cuname = request.form.get('cuname')
            cucontact = request.form.get('cucontact')
            cusubject = request.form.get('cusubject')
            cumessage = request.form.get('cumessage')

            if cuname and cucontact and cusubject and cumessage:
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('INSERT INTO contact (cname, ccontact, csubject, cmessage) VALUES (%s, %s, %s, %s)',
                               (cuname, cucontact, cusubject, cumessage))
                mysql.connection.commit()
                cursor.close()

                success_alert = '''
                <script>
                    alert('Your Message has been sent');
                    window.location.href = '/dashboard';
                </script>
                '''
                return success_alert

        return render_template('Dashboard.html', session=session)
    else:
        return redirect(url_for('login'))

@app.route('/checkout', methods=['POST'])
def checkout():
    if 'loggedin' in session:
        # Get the form data
        fullname = request.form.get('fullname')
        destination = request.form.get('destination')
        price = request.form.get('price')
        contactnumber = request.form.get('contactnumber')
        address = request.form.get('address')

        # Perform the database insertion
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO Booknow (fullname, destination, totalcost, contactnumber, address) VALUES (%s, %s, %s, %s, %s)',
                       (fullname, destination, price, contactnumber, address))
        mysql.connection.commit()
        cursor.close()
        success_alert = '''
                <script>
                    alert('Your Message has been sent');
                    window.location.href = '/dashboard';
                </script>
                '''

        # Redirect or show a success message
        return success_alert
    else:
        # Redirect to login page if not logged in
        return redirect(url_for('login'))

@app.route('/er')
def er():
    if 'loggedin' in session:
        user_id = session['id']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM er WHERE user_id = %s', (user_id,))
        records = cursor.fetchall()
        cursor.close()

        return render_template('er.html', records=records)
    else:
        return redirect(url_for('login'))



@app.route('/er/add', methods=['POST'])
def expense():
    userid = session['id']
    edate = request.form['edate']
    time = request.form['etime']
    expensename = request.form['ename']
    amount = request.form['eamount']
    destination = request.form['destination']
    place = request.form['place']
    paymode = request.form['ptype']
    category = request.form['category']
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('insert into er (user_id,edate, etime, ename, eamount, destination, place, ptype, category) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
               (userid, edate, time, expensename, amount, destination, place, paymode, category))

    mysql.connection.commit()
    cursor.close()

    success_alert = '''
            <script>
                alert('Expense Recorded !!!');
                window.location.href = '/er';
            </script>
            '''
    
    return success_alert


@app.route('/er/<int:record_id>/delete', methods=['POST'])
def delete_er_record(record_id):
    
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM er WHERE id = %s', (record_id,))
    mysql.connection.commit()
    cursor.close()

    return redirect('/er')



if __name__ == '__main__':
    app.run(debug=True)