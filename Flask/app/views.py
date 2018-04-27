from app import app
from datetime import datetime
from datetime import timedelta
import sqlite3
import hashlib
import re
from flask import render_template, g, redirect, request, make_response
#import pdfkit
#import qrcode
from PIL import Image as pimg

from .models import WhatsOn, Movie, Booking, User

import json

DATABASE = 'app/database/cinema.db'


##Function to execute an SQL query
def execute_query(query, method):
    conn = get_db()
    c = conn.cursor()
    try:
        if method == 'GET':
            c.execute(query)
            r = [dict((c.description[i][0], value)
                      for i, value in enumerate(row)) for row in c.fetchall()]
            # json_output = json.dumps(r)
            return r
        elif method == 'POST' or method == 'DELETE':
            c.execute(query)
            conn.commit()
            return "{Status: 200}"
    except sqlite3.IntegrityError:
        return "{Status:400}"


def getMovies():
    movies_db = execute_query("SELECT * FROM MOVIES;", "GET")
    movies = []
    for item in movies_db:
        movies.append(
            Movie(item["Movie_ID"], item["Movie_Name"], item["Movie_Rating"], item["Movie_Runtime"], item["Movie_Info"],
                  item["Movie_Image"], item["Movie_Director"], item["Movie_Actors"]))

    return movies


def getMoviebyID(id):
    movie = execute_query("SELECT * FROM MOVIES where Movie_ID=%s" % id, "GET")
    if movie:
        item = movie[0]
        return Movie(item["Movie_ID"], item["Movie_Name"], item["Movie_Rating"], item["Movie_Runtime"],
                     item["Movie_Info"], item["Movie_Image"])


def getWhatsOn():
    screenings = execute_query("SELECT * FROM Whats_On;", "GET")
    whatson = []

    for idScreening in screenings:
        whatson.append(getWhatsOnbyID(idScreening["Screening_ID"]))

    return whatson


def getWhatsOnByMovieID(id):
    screenings = execute_query("SELECT * FROM Whats_On where Movie_ID=%s;" % id, "GET")
    whatson = []

    for idScreening in screenings:
        whatson.append(getWhatsOnbyID(idScreening["Screening_ID"]))
    return whatson


def getWhatsOnbyID(id):
    whatson = execute_query("SELECT * FROM Whats_On where Screening_ID=%s;" % id, "GET")
    if whatson:
        item = whatson[0]
        return WhatsOn(item["Screening_ID"], item["Movie_ID"], item["Screen_ID"], item["Start_Time"])


def getUserbyID(id):
    user = execute_query("SELECT * FROM Users where User_ID=%s;" % id, "GET")
    if user:
        item = user[0]
        return User(item["User_ID"], item["Username"], item["Password"])


def getUserByUsername(username):
    user = execute_query("SELECT * FROM Users where Username=%s;" % ("\"" + username + "\""), "GET")
    if user:
        item = user[0]
        return User(item["User_ID"], item["Username"], item["Password"])


def addUser(username, password):
    conn = get_db()
    c = conn.cursor()
    max_id_list = c.execute("SELECT Max(User_ID) from Users;").fetchall()
    max_id_list2 = max_id_list[0]
    number_of_rows = max_id_list2[0]
    query = "INSERT INTO Users VALUES(" + str(
        number_of_rows + 1) + ", " + "\"" + username + "\"" + "," + "\"" + password + "\"" + ");"
    execute_query(query, "POST")


def getBookingbyID(id):
    booking = execute_query("SELECT * FROM Bookings where Screening_ID=%s;" % id, "GET")
    bookings = []
    for item in booking:
        bookings.append(Booking(item["Screening_ID"], item["Row_Num"], item["Column_Num"]))
    return bookings


def addBooking(screening, row, column):
    conn = get_db()
    c = conn.cursor()
    print(str(row))
    print(str(column))
    query = "INSERT INTO Bookings VALUES(" + str(screening) + ", " + "\"" + str(row) + "\"" + "," + "\"" + str(
        column) + "\"" + ");"
    execute_query(query, "POST")


##Get the database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE, check_same_thread=False)
    return db


##On program close, close db connection
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


#####################################################################################################################

# Global variables
seat = (7, 7)
vip = False
bookingID=0
row = 7
column = 7

@app.route('/')
def index():
    now = datetime.now()
    days = []
    days.append(("Today",now))
    for i in range(1,7):
        date = now + timedelta(days=i)
        day = date.strftime("%A")
        days.append((day, date))

    # input from screening table
    movies = getMovies()
    whatsons = []
    present = False
    for m in movies:
        futureWhatsOn = []
        whatsOn = getWhatsOnByMovieID(m.Movie_ID)
        for w in whatsOn:
            startTime = datetime.strptime(w.Start_Time, "%Y-%m-%dT%H:%M:%S" )
            if(startTime > now):
                present = True
                futureWhatsOn.append(w)
        if(present):
            whatsons.append((m, futureWhatsOn))

    return render_template('index.html', whatsons=whatsons, daysOfWeek = days, msg="Today", date=now.strftime("%Y-%m-%d %H:%M:%S"));


@app.route('/day/<choice>')
def day(choice):
    now = datetime.now()
    days = []
    days.append(("Today",now))

    for i in range(1,7):
        date = now + timedelta(days=i)
        day = date.strftime("%A")
        days.append(day)

    for d in days:
        if( choice == d[0]):
            chosenDate = day[1].strftime("%Y-%m-%d %H:%M:%S")

    # input from screening table
    movies = getMovies()
    whatsons = []
    futureWhatsOn = []
    print(now)
    for m in movies:
        whatsOn = getWhatsOnByMovieID(m.Movie_ID)
        for w in whatsOn:
            startTime = datetime.strptime(w.Start_Time, "%Y-%m-%dT%H:%M:%S" )
            if(startTime > chosenDate):
                present = True
                futureWhatsOn.append(w)
        if(present):
            whatsons.append((m, futureWhatsOn))

    return render_template('index.html', whatsons=whatsons, msg=choice, daysOfWeek = days, date=chosenDate);

@app.route('/seatselect/<id>')
def tickets(id):
    seats = getBookingbyID(id)
    allSeats = []
    if not seats:
        for i in range(1, 6):
            for j in range(1, 6):
                allSeats.append((i, j, False, (i, j)))
                print("problem")
    else:
        for i in range(1, 6):
            for j in range(1, 6):
                booked = False
                for seat in seats:
                    if ((int(seat.Row_Num) == i) and (int(seat.Column_Num) == j) and (int(seat.Screening_ID) == int(id))):
                        allSeats.append((i, j, True, (i, j)))
                        booked = True
                if booked == False:
                    allSeats.append((i, j, False, (i, j)))
    global bookingID
    bookingID = id
    return render_template('seatselect.html', allSeats=allSeats)

@app.route('/storeSeat/<id>/<Row>/<Column>')
def storeSeats(id,Row,Column):
    global seat
    seat = id
    global row
    row = Row
    global column
    column = Column
    print(Row)
    if(int(Row) == 3):
        global vip
        vip=True
    return "",204


@app.route('/login')
def login():
    return render_template('login.html', msg=None)

@app.route('/loginrequest', methods=['POST'])
def loginRequest():
    # Get the details from the form
    username = request.form.get('Username')
    password = request.form.get('Password')
    password = password + "saltyquail"
    if type(password) == str:
        password = str.encode(password)
    passwordHashed = hashlib.sha256()
    passwordHashed.update(password)

    user = getUserByUsername(username)

    # Check they are the details of a known user
    if (user):
        if (user.Password == passwordHashed.hexdigest()):
            return redirect('/')
        else:
            return render_template('login.html', msg="Incorrect Username/Password combination")
    else:
        return render_template('login.html', msg="Username not recognised")


@app.route('/register')
def register():
    return render_template('register.html', msg=None)


@app.route('/registerrequest', methods=['POST'])
def registerRequest():
    # Get the login details from the form
    username = request.form.get('Username')
    password = request.form.get('Password')
    passwordConfirm = request.form.get('Confirm Password')

    # Check if the details are valid
    if username == "":
        return render_template('register.html', msg="No username entered")

    if password != passwordConfirm:
        return render_template('register.html', msg="Passwords do not match")

    # Salt and hash the password
    password = password + "saltyquail"
    if type(password) == str:
        password = str.encode(password)
    passwordHashed = hashlib.sha256()
    passwordHashed.update(password)

    # Add the details to the database
    addUser(username, passwordHashed.hexdigest())

    return render_template('register.html', msg="Registration Successful")


@app.route('/payment', methods=['POST'])
def paymentNoType():
    # Get the ticket type from the drop down box
    ticketType = request.form.get("selectTicket")
    if(bookingID!=0 and seat!=(7,7)):
        addBooking(bookingID,row,column)
    if(seat == (7,7)):
        return "",204
    else:
        return redirect('/payment/' + ticketType.lower())


@app.route('/payment/<ticketType>')
def payment(ticketType):
    # Set the price according to the ticket type
    if ticketType == "adult":
        price = 8
    elif ticketType == "child" or ticketType == "senior":
        price = 4
    if vip == True:
        price = (price*1.5)

    return render_template('payment.html', ticketType=ticketType.title(), price=price, msg=None)


@app.route('/processPayment/<ticketType>/<price>', methods=['POST'])
def processPayment(ticketType, price):
    # Get card details from the form
    name = request.form.get('Name')
    cardNumber = request.form.get('Card Number')
    expiryDate = request.form.get('Expiry Date')
    securityCode = request.form.get('Security Code')

    # Check the validity of the card details and return an appropriate message if any are wrong
    if name != "":
        if cardNumber and len(cardNumber) <= 19:
            if re.match('[0-9]{2}/[0-9]{2}', expiryDate):
                if re.match('^[0-9]{3,4}$', securityCode):
                    img = qr_code(ticketType.title(), price, name)
                    return render_template('payment.html', ticketType=ticketType.title(), price=price,
                                           msg="Payment Confirmed")
                else:
                    return render_template('payment.html', ticketType=ticketType.title(), price=price,
                                           msg="Security code was not in the correct format")
            else:
                return render_template('payment.html', ticketType=ticketType.title(), price=price,
                                       msg=" Expiry date was not in the correct format")
        else:
            return render_template('payment.html', ticketType=ticketType.title(), price=price,
                                   msg="Card number must be less than 19 digits")
    else:
        return render_template('payment.html', ticketType=ticketType.title(), price=price, msg="A name must be entered")

# @app.route('/<ticketType>/<price>/<name>')
# def qr_code(ticketType, price, name):
#     img = qrcode.make(name)
#     img.save('qr_codes/'+name+'.PNG')
#     return img
