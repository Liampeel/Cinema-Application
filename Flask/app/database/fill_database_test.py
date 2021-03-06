#Alexander Hoare
#Placing start information into database

#Importing sqlite3
import sqlite3
#Importing random to create random test data
import random

from datetime import datetime
from datetime import timedelta

#Connecting to database
db = sqlite3.connect('cinema.db')
cursor = db.cursor()


##Initial user information
id1 = 1
username1 = 'kieron.hushon@gmail.com'
#SHA256 hash of 'password'
password1 = '56564387AE573084485D94C7BEBF8907BABF4EAA5B409C0A9C9C23F24D5C848E'

id2 = 2
username2 = 'alexander_hoare@hotmail.co.uk'
#SHA256 hash of 'hunter2'
#password2 = 'F52FBD32B2B3B86FF88EF6C490628285F482AF15DDCB29541F94BCF526A3F6C7'
password2 = 'e85c15f396d69cbe9f6d080dae41f7b512223b8a4ab32c162ca296cc5a3dd931'


##Card details
c_uid1 = 1
c_n1 = "Alexander Hoare"
c_num1 = "BBBBCCCCDDDDEEEE"
ce1 = "02/20"
c_s1 = "BBE"

c_uid2 = 2
c_n2 = "Kieron Hushon"
c_num2 = "FFFFGGGGHHHHIIII"
ce2 = "05/21"
c_s2 = "FFF"

##Initial movie information
movie_Id1 = 1
movie_Name1 = 'Batman Begins'
movie_Rating1 = '12A'
movie_Runtime1 = 7200
movie_Info1 = 'Man scared of bats dresses up to beat up people'
movie_Director1 = 'Christopher Nolan'
movie_Actors1 = 'Christian Bale, Danny Nay, Natalie Portman'
movie_Image1 = '../static/img/batman_begins.jpg'

movie_Id2 = 2
movie_Name2 = 'Superman: Man of Steel'
movie_Rating2 = '15'
movie_Runtime2 = 8400
movie_Info2 = 'Is it a bird, is it a plane? No its Superman!'
movie_Director2 = 'Michael Bay'
movie_Actors2 = 'Gary Oldman, Gary Coleman, Gary Newman'
movie_Image2 = '../static/img/superman.jpg'

movie_Id3 = 3
movie_Name3 = 'Frozen'
movie_Rating3 = 'U'
movie_Runtime3 = 7200
movie_Info3 = 'Princess with hypothermia estranges her family'
movie_Director3 = 'M. Night Shamalamalan'
movie_Actors3 = 'Beneictus Chrimblesnatch, Sting, Dimitri Popov'
movie_Image3 = '../static/img/frozen.jpg'

movie_Id4 = 4
movie_Name4 = 'The Great Escape'
movie_Rating4 = '12A'
movie_Runtime4 = 5400
movie_Info4 = 'Man who loves tunnels digs out of camp'
movie_Director4 = 'Alfred Hitchcock'
movie_Actors4 = 'Steve McQueen, Killian Reestein'
movie_Image4 = '../static/img/great_escape.jpg'

movie_Id5 = 5
movie_Name5 = 'Pirates of the Carribean: The Black Pearl'
movie_Rating5 = '12A'
movie_Runtime5 = 9000
movie_Info5 = 'Man with alcohol problem steals ships and pretends to be a captain'
movie_Director5 = 'Stephen Spielberg'
movie_Actors5 = 'Johnny Depp, Kiera Knightly, Legolas'
movie_Image5 = '../static/img/pirates_of_the_caribbean_one.jpg'

movie_Id6 = 6
movie_Name6 = 'Scary Movie III'
movie_Rating6 = '18+'
movie_Runtime6 = 7800
movie_Info6 = 'Spooky stuff occurs in this spooky movie'
movie_Director6 = 'Quentin Tarentino'
movie_Actors6 = 'Danny Dyer, Ray Winston'
movie_Image6 = '../static/img/scary_movie_3.jpg'


##Initial whats on movie information
#Information for movie 1 on one day
wo_Id = 1
wo_Movie = 1
wo_Screen = 1
#Time must be in format 'YYYY-MM-DD:HH:MM:SS'
wo_Time = "2018-04-01T11:55:00"

wo_Id2 = 2
wo_Movie2 = 1
wo_Screen2 = 1
wo_Time2 = "2018-04-01T14:00:00"

wo_Id3 = 3
wo_Movie3 = 1
wo_Screen3 = 1
wo_Time3 = "2018-04-01T16:30:00"
#Day 2
wo_Id4 = 4
wo_Movie4 = 1
wo_Screen4 = 1
#Time must be in format 'YYYY-MM-DD:HH:MM:SS'
wo_Time4 = "2018-04-02T11:55:00"

wo_Id5 = 5
wo_Movie5 = 1
wo_Screen5 = 1
wo_Time5 = "2018-04-02T14:00:00"

wo_Id6 = 6
wo_Movie6 = 1
wo_Screen6 = 1
wo_Time6 = "2018-04-02T16:30:00"
#Movie 2
#Information for movie 2 on one day
wo_Id7 = 7
wo_Movie7 = 2
wo_Screen7 = 3
#Time must be in format 'YYYY-MM-DD:HH:MM:SS'
wo_Time7 = "2018-04-01T09:00:00"

wo_Id8 = 8
wo_Movie8 = 2
wo_Screen8 = 3
wo_Time8 = "2018-04-01T12:00:00"

wo_Id9 =9
wo_Movie9 = 2
wo_Screen9 = 3
wo_Time9 = "2018-04-01T15:30:00"
#Day 2
wo_Id10 = 10
wo_Movie10 = 2
wo_Screen10 = 2
#Time must be in format 'YYYY-MM-DD:HH:MM:SS'
wo_Time10 = "2018-04-02T10:30:00"

wo_Id11 = 11
wo_Movie11 = 2
wo_Screen11 = 2
wo_Time11 = "2018-04-02T13:00:00"

wo_Id12 = 12
wo_Movie12 = 2
wo_Screen12 = 2
wo_Time12 = "2018-04-02T16:30:00"

#Movie 3
#Information for movie 3 on one day
wo_Id13 = 13
wo_Movie13 = 3
wo_Screen13 = 4
#Time must be in format 'YYYY-MM-DD:HH:MM:SS'
wo_Time13 = "2018-04-01T09:00:00"

wo_Id14 = 14
wo_Movie14 = 3
wo_Screen14 = 4
wo_Time14 = "2018-04-01T12:00:00"

wo_Id15 =15
wo_Movie15 = 3
wo_Screen15 = 4
wo_Time15 = "2018-04-01T15:30:00"
#Day 2
wo_Id16 = 16
wo_Movie16 = 3
wo_Screen16 = 5
#Time must be in format 'YYYY-MM-DD:HH:MM:SS'
wo_Time16 = "2018-04-02T10:30:00"

wo_Id17 = 17
wo_Movie17 = 3
wo_Screen17 = 4
wo_Time17 = "2018-04-02T13:15:00"

wo_Id18 = 18
wo_Movie18 = 3
wo_Screen18 = 4
wo_Time18 = "2018-04-02T17:45:00"

#Movie 4
#Information for movie 4 on one day
wo_Id19 = 19
wo_Movie19 = 4
wo_Screen19 = 6
#Time must be in format 'YYYY-MM-DD:HH:MM:SS'
wo_Time19 = "2018-04-01T10:00:00"

wo_Id20 = 20
wo_Movie20 = 4
wo_Screen20 = 6
wo_Time20 = "2018-04-01T12:30:00"

wo_Id21 = 21
wo_Movie21 = 4
wo_Screen21 = 6
wo_Time21 = "2018-04-01T16:30:00"
#Day 2
wo_Id22 = 22
wo_Movie22 = 4
wo_Screen22 = 6
#Time must be in format 'YYYY-MM-DD:HH:MM:SS'
wo_Time22 = "2018-04-02T8:30:00"

wo_Id23 = 23
wo_Movie23 = 4
wo_Screen23 = 6
wo_Time23 = "2018-04-02T11:15:00"

wo_Id24 = 24
wo_Movie24 = 4
wo_Screen24 = 6
wo_Time24 = "2018-04-02T17:45:00"

#Movie 5
#Information for movie 5 on one day
wo_Id25 = 25
wo_Movie25 = 5
wo_Screen25 = 7
#Time must be in format 'YYYY-MM-DD:HH:MM:SS'
wo_Time25 = "2018-04-01T09:00:00"

wo_Id26 = 26
wo_Movie26 = 5
wo_Screen26 = 7
wo_Time26 = "2018-04-01T12:00:00"

wo_Id27 = 27
wo_Movie27 = 5
wo_Screen27 = 7
wo_Time27 = "2018-04-01T17:30:00"
#Day 2
wo_Id28 = 28
wo_Movie28 = 5
wo_Screen28 = 7
#Time must be in format 'YYYY-MM-DD:HH:MM:SS'
wo_Time28 = "2018-04-02T10:30:00"

wo_Id29 = 29
wo_Movie29 = 5
wo_Screen29 = 7
wo_Time29 = "2018-04-02T15:15:00"

wo_Id30 = 30
wo_Movie30 = 5
wo_Screen30 = 7
wo_Time30 = "2018-04-02T20:45:00"

#Movie 6
#Information for movie 3 on one day
wo_Id31 = 31
wo_Movie31 = 6
wo_Screen31 = 8
#Time must be in format 'YYYY-MM-DD:HH:MM:SS'
wo_Time31 = "2018-04-01T09:15:00"

wo_Id32 = 32
wo_Movie32 = 6
wo_Screen32 = 8
wo_Time32 = "2018-04-01T13:00:00"

wo_Id33 = 33
wo_Movie33 = 6
wo_Screen33 = 8
wo_Time33 = "2018-04-01T18:30:00"

#Day 2
wo_Id34 = 34
wo_Movie34 = 6
wo_Screen34 = 8
#Time must be in format 'YYYY-MM-DD:HH:MM:SS'
wo_Time34 = "2018-04-02T10:15:00"

wo_Id35 = 35
wo_Movie35 = 6
wo_Screen35 = 8
wo_Time35 = "2018-04-02T14:15:00"

wo_Id36 = 36
wo_Movie36 = 6
wo_Screen36 = 8
wo_Time36 = "2018-04-02T19:45:00"

##Initial bookings information
b_Id = 1
b_Col = 1 #Bookings column
b_Row = 1 #Bookings row

b_Id2 = 1
b_Col2 = 3 #Bookings column
b_Row2 = 3 #Bookings row

b_Id3 = 1
b_Col3 = 5 #Bookings column
b_Row3 = 5 #Bookings row

#Entering values into cinema.db tables
cursor.execute('''INSERT INTO Users(User_ID,Username,Password)
                VALUES(?,?,?)''', (id1,username1,password1))

cursor.execute('''INSERT INTO Users(User_ID,Username,Password)
                VALUES(?,?,?)''', (id2,username2,password2))

cursor.execute('''INSERT INTO Movies(Movie_ID,Movie_Name,Movie_Rating,Movie_Runtime,
                                        Movie_Info, Movie_Director, Movie_Actors, Movie_Image)
                                    VALUES(?,?,?,?,?,?,?,?)''',(movie_Id1,movie_Name1,
                                    movie_Rating1,movie_Runtime1,movie_Info1,movie_Director1, movie_Actors1,movie_Image1))

cursor.execute('''INSERT INTO Movies(Movie_ID,Movie_Name,Movie_Rating,Movie_Runtime,
                                        Movie_Info, Movie_Director, Movie_Actors, Movie_Image)
                                    VALUES(?,?,?,?,?,?,?,?)''',(movie_Id2,movie_Name2,
                                    movie_Rating2,movie_Runtime2,movie_Info2,movie_Director2,movie_Actors2,movie_Image2))

cursor.execute('''INSERT INTO Movies(Movie_ID,Movie_Name,Movie_Rating,Movie_Runtime,
                                        Movie_Info, Movie_Director, Movie_Actors, Movie_Image)
                                    VALUES(?,?,?,?,?,?,?,?)''',(movie_Id3,movie_Name3,
                                    movie_Rating3,movie_Runtime3,movie_Info3,movie_Director3,movie_Actors3,movie_Image3))

cursor.execute('''INSERT INTO Movies(Movie_ID,Movie_Name,Movie_Rating,Movie_Runtime,
                                        Movie_Info, Movie_Director, Movie_Actors, Movie_Image)
                                    VALUES(?,?,?,?,?,?,?,?)''',(movie_Id4,movie_Name4,
                                    movie_Rating4,movie_Runtime4,movie_Info4,movie_Director4, movie_Actors4,movie_Image4))

cursor.execute('''INSERT INTO Movies(Movie_ID,Movie_Name,Movie_Rating,Movie_Runtime,
                                        Movie_Info, Movie_Director, Movie_Actors, Movie_Image)
                                    VALUES(?,?,?,?,?,?,?,?)''',(movie_Id5,movie_Name5,
                                    movie_Rating5,movie_Runtime5,movie_Info5,movie_Director5,movie_Actors5,movie_Image5))

cursor.execute('''INSERT INTO Movies(Movie_ID,Movie_Name,Movie_Rating,Movie_Runtime,
                                        Movie_Info, Movie_Director, Movie_Actors, Movie_Image)
                                    VALUES(?,?,?,?,?,?,?,?)''',(movie_Id6,movie_Name6,
                                    movie_Rating6,movie_Runtime6,movie_Info6,movie_Director6,movie_Actors6,movie_Image6))


cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id, wo_Movie, wo_Screen, wo_Time))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id2, wo_Movie2, wo_Screen2, wo_Time2))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id3, wo_Movie3, wo_Screen3, wo_Time3))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id4, wo_Movie4, wo_Screen4, wo_Time4))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id5, wo_Movie5, wo_Screen5, wo_Time5))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id6, wo_Movie6, wo_Screen6, wo_Time6))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id7, wo_Movie7, wo_Screen7, wo_Time7))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id8, wo_Movie8, wo_Screen8, wo_Time8))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id9, wo_Movie9, wo_Screen9, wo_Time9))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id10, wo_Movie10, wo_Screen10, wo_Time10))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id11, wo_Movie11, wo_Screen11, wo_Time11))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id12, wo_Movie12, wo_Screen12, wo_Time12))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id13, wo_Movie13, wo_Screen13, wo_Time13))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id14, wo_Movie14, wo_Screen14, wo_Time14))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id15, wo_Movie15, wo_Screen15, wo_Time15))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id16, wo_Movie16, wo_Screen16, wo_Time16))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id17, wo_Movie17, wo_Screen17, wo_Time17))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id18, wo_Movie18, wo_Screen18, wo_Time18))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id19, wo_Movie19, wo_Screen19, wo_Time19))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id20, wo_Movie20, wo_Screen20, wo_Time20))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id21, wo_Movie21, wo_Screen21, wo_Time21))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id22, wo_Movie22, wo_Screen22, wo_Time22))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id23, wo_Movie23, wo_Screen23, wo_Time23))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id24, wo_Movie24, wo_Screen24, wo_Time24))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id25, wo_Movie25, wo_Screen25, wo_Time25))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id26, wo_Movie26, wo_Screen26, wo_Time26))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id27, wo_Movie27, wo_Screen27, wo_Time27))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id28, wo_Movie28, wo_Screen28, wo_Time28))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id29, wo_Movie29, wo_Screen29, wo_Time29))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id30, wo_Movie30, wo_Screen30, wo_Time30))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id31, wo_Movie31, wo_Screen31, wo_Time31))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id32, wo_Movie32, wo_Screen32, wo_Time32))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id33, wo_Movie33, wo_Screen33, wo_Time33))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id34, wo_Movie34, wo_Screen34, wo_Time34))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id35, wo_Movie35, wo_Screen35, wo_Time35))

cursor.execute('''INSERT INTO Whats_On(Screening_ID, Movie_ID, Screen_ID, Start_Time)
                                    Values(?,?,?,?)''',(wo_Id36, wo_Movie36, wo_Screen36, wo_Time36))

cursor.execute('''INSERT INTO Bookings(Screening_ID, Row_Num, Column_Num)
                                    VALUES(?,?,?)''', (b_Id, b_Row, b_Col))

cursor.execute('''INSERT INTO Bookings(Screening_ID, Row_Num, Column_Num)
                                    VALUES(?,?,?)''', (b_Id2, b_Row2, b_Col2))

cursor.execute('''INSERT INTO Bookings(Screening_ID, Row_Num, Column_Num)
                                    VALUES(?,?,?)''', (b_Id3, b_Row3, b_Col3))

cursor.execute('''INSERT INTO Card_Details(User_ID, Card_Name, Card_Number, Card_SortCode, Card_SecurityCode)
                                    VALUES(?,?,?,?,?)''', (c_uid1, c_n1, c_num1, ce1, c_s1))

cursor.execute('''INSERT INTO Card_Details(User_ID, Card_Name, Card_Number, Card_SortCode, Card_SecurityCode)
                                    VALUES(?,?,?,?,?)''', (c_uid2, c_n2, c_num2, ce2, c_s2))

#Committing changes to cinema.db
db.commit()
db.close()
