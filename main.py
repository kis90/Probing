from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL,MYSQLdb
import MySQLdb.cursors

app = Flask(__name__)

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'ip-10-0-132-135'
app.config['MYSQL_USER'] = 'ubuntu'
app.config['MYSQL_PASSWORD'] = 'Capgemini@2020'
app.config['MYSQL_DB'] = 'probedb'

# Intialize MySQL
mysql = MySQL(app)

@app.route('/login', methods=['GET', 'POST'])
def login():

    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'E-Mail' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['E-Mail']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM memberlogin WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
                # If account exists in accounts table in out database
        if account:
            # Create session id, so that we can access this data in other routes
            session['id'] = account['id']
            session['username'] = account['username']
            cursor.execute('INSERT INTO memberdata (id,userid,pwd) VALUES (%s, %s,%s) ',(id,username,password))
            # Redirect to input page
            return redirect(url_for('memLandingPage'))

        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg='')



@app.route('/input1', methods=['GET', 'POST'])
def input1():
    # Output message if something goes wrong...
    msg = ''

    if request.method == 'POST' and 'Technology Platform' in request.form and 'OS Platform' in request.form and 'Connect Database' in request.form and 'DB Host name' in request.form and 'DB UserName' in request.form and 'DB Password' in request.form:
        # Create variables for easy access
        techplatform = request.form['Technology Platform']
        osplatform = request.form['OS Platform']
        dbconn = request.form['Connect Database']
        hostn = request.form['DB Host name']
        usern = request.form['DB UserName']
        pwd = request.form['DB Password']
        # adding these details under same id
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO memberdata (ct1, ct2,dbconn,hostn,usern, pass) VALUES (%s, %s,%s,%s, %s, %s) where id = %s', (techplatform, osplatform, dbconn, hostn, usern, pwd , id))
        mysql.connection.commit()
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'

    return render_template('index.html', msg=msg)


@app.route('/input2', methods=['GET', 'POST'])
def input2():
    # Output message if something goes wrong...
    msg = ''

    if request.method == 'POST' and 'Connect ETL' in request.form and 'ETL Host name' in request.form and 'ETL UserName' in request.form and 'ETL Password' in request.form and 'Connect BiTool' in request.form and 'BI Host name' in request.form and 'BI UserName' in request.form and 'BI Password' in request.form:
        # Create variables for easy access
        etlr = request.form['Connect ETL']
        hostna = request.form['ETL Host name']
        userna = request.form['ETL UserName']
        pwd1 = request.form['ETL Password']
        bitr = request.form['Connect BiTool']
        hostnam = request.form['BI Host name']
        usernam = request.form['BI UserName']
        pwd2 = request.form['BI Password']
        # adding these details under same id
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO memberdata (etlcon, hostna, userna, passw, bitconn, hostnam, usernam , passwo) VALUES (%s,%s, %s, %s,%s,%s, %s, %s) where id = %s', (etlr, hostna, userna, pwd1, bitr, hostnam,usernam, pwd2 , id))
        mysql.connection.commit()
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'

    return render_template('index.html', msg=msg)


@app.route('/input3', methods=['GET', 'POST'])
def input3():
    # Output message if something goes wrong...
    msg = ''

    if request.method == 'POST' and 'Success Host name' in request.form and 'Growth Estimation' in request.form and 'Data Retention' in request.form and 'Data Archival' in request.form and 'DR Strategy' in request.form and 'Prod Cp' in request.form and 'Teradata License' in request.form and 'Expected Growthr' in request.form and 'ETL Tools' in request.form :
        # Create variables for easy access
        migsuc= request.form['Success Host name']
        growth = request.form['Growth Estimation']
        dataret = request.form['Data Retention']
        dataarch = request.form['Data Archival']
        drst = request.form['DR Strategy']
        prodcp= request.form['Prod Cp']
        tdlis = request.form['Teradata License']
        growthper= request.form['Expected Growth']
        etltool = request.form['ETL Tools']
        # adding these details under same id
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO memberdata (migsuc,growth, dataret,dataarch,drst, prodcp,tdlis,growthper,etltool) VALUES (%s,%s,%s,%s, %s,%s,%s, %s, %s) where id = %s', (migsuc,growth, dataret,dataarch,drst, prodcp,tdlis,growthper,etltool, id))
        mysql.connection.commit()
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'

    return render_template('index.html', msg=msg)


if __name__ =='__main__':
	app.run(Debug=True)
