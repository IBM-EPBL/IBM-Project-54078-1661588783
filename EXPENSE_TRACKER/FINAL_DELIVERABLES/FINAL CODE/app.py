# import ibm_db2
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")



# dsn_hostname="764264db-9824-4b7c-82df-40d1b13897c2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
# dsn_uid="o6Bz1HKZJ5ZfMCof"
# dsn_pwd="dtv66436"
# dsn_driver="{IBM DB2 ODBC DRIVER}"
# dsn_database="bludb"   
# dsn_port= "32536"
# dsn_protocol="TCPIP"

# dsn=(
#     "DRIVER={0};"
#     "DATABASE={1};"
#     "HOSTNAME={2};"
#     "PORT={3};"
#     "PROTOCOL={4};"
#     "UID={5};"
#     "PWD={6};").format(dsn_driver,dsn_database,dsn_hostname,dsn_port,dsn_protocol,dsn_uid,dsn_pwd)
# print(dsn)

# try:
#     conn=ibm_db.connect(dsn,"","")
    # print("connection to database: ", dsn_database,"as user: ", dsn_uid, "on host: ",dsn_hostname)
# except:
    # print( "unable to connect: ", ibm_db.conn_errormsg() )


# server=ibm_db.server_info(conn)
# print("DBMS_NAME: ", server.DBMS_NAME)
# print("DBMS_VER: ", server.DBMS_VER)
# print("DB_NAME: ", server.DB_NAME)

def index():
    return render_template('index.html')
    
@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
SENDGRID_API_KEY = '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'

# SENDGRID_API_KEY = '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'


# message = Mail(
#                from_mail='abc@gmail.com',
#                to_mails='somanathdas.r@gmail.com',
#                subject='sending with twilio SendGrid is Fun',
#                plain_text_content='and easy to do anywhere, even with python.',
#                html_content='<strong> and easy to do anywhere, even with Python</strong>'
#                )
# try:
#     sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)