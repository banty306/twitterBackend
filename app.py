from flask import Flask, request, abort, jsonify
from flask_cors import CORS

import os, json, jwt
import psycopg2, psycopg2.extras

app = Flask(__name__)
cors = CORS(app)
secret_key = 'marinirinfantri'

#create Connection to database in postgreSQL
con = psycopg2.connect(database=os.getenv('DATABASE'),user=os.getenv('USER'),password=os.getenv('PASSWORD'),host=os.getenv('HOSTDB'),port=os.getenv('PORTDB'))

@app.route('/signUp', methods=['POST'])
def signUp():
    #retrieve data from user input in main
    username = request.json['username']
    fullname = request.json['fullname']
    email = request.json['email']
    password = request.json['password']
    bio = request.json['bio']
    photoprofile = request.json['photoprofile']

    cursorSignUp = con.cursor()
    cursorSignUp.execute("Insert into person (username,fullname,email,password,bio, photoprofile) values(%s,%s,%s,%s,%s,%s)",(username, fullname, email, password, bio, photoprofile))
    con.commit()

    return "SignUp success", 201

@app.route('/login', methods=['POST'])
def login():

    username = request.json['username']
    password = request.json['password']

    cursorLogin = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursorLogin.execute("Select * from person where username = %s and password = %s",(username,password))
    jml = cursorLogin.rowcount

    # return str(cursorLogin.fetchall())
    
    dataUser = []
    for row in cursorLogin.fetchall():
        encode = jwt.encode({'id':row[0]},secret_key,algorithm='HS256').decode('utf-8')
        # print(encode)
        dataUser.append(dict(row))

    con.commit()
    #merge json
    dataUser[0].update({'token':str(encode)})
    if jml > 0:
        return jsonify(dataUser), 200
    else:
        "Fail", 400   

@app.route('/dashboard', methods=['GET'])
def read_tweet():
   
    curTweet = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    curTweet.execute("select person.id as id, person.username as username, person.fullname as fullname, person.email as email, person.password as password, person.bio as bio, person.photoprofile as photoprofile, tweets.id as idtweet, tweets.content as content, tweets.date as date from tweets inner join person on tweets.person_id=person.id") # To display tweet data from db

    dataTweet = []
    data_TokenID = []
    for row in curTweet.fetchall():
        encode = jwt.encode({'id':row[0]},secret_key,algorithm='HS256').decode('utf-8')
        
        data_TokenID.append(encode)
        dataTweet.append(dict(row))

    for index, tokenID in enumerate(data_TokenID):
        dataTweet[int(index)].update({"token":str(tokenID)})

    con.commit()
    return jsonify(dataTweet), 200  

@app.route('/addtweet', methods=['POST'])
def add_tweet():

    if request.method == 'POST':
        token = request.json['id']
        decode = jwt.decode(token, secret_key, algorithms=['HS256'])
        id = (decode['id'])
        tweet = request.json['content']

        curInsertTweet = con.cursor()
        curInsertTweet.execute("Insert into tweets (content, date, person_id) values (%s,now(),%s)",(tweet, id))
        
        con.commit()
        return "Tweet success", 201
    else:
        return "Method not allowed", 400


#Displays the user to be followed
@app.route('/getfollowlist', methods=['POST'])
def get_following_list():

    token = request.json['id']
    decode = jwt.decode(token, secret_key, algorithms=['HS256'])
    id = (decode['id'])

    #retrieve data from database
    cursorgetfollow = con.cursor(cursor_factory = psycopg2.extras.DictCursor)
    cursorgetfollow.execute("select * from person where id not in (select following from follow where id_person=%s) and id != %s",(id,id))

    dataFollowlist = []
    for row in cursorgetfollow.fetchall():
        dataFollowlist.append(dict(row))

    con.commit()

    return jsonify(dataFollowlist), 201

# read personal tweet in profile page
@app.route('/readPersonaltweet', methods=['POST'])
def read_personal_tweet():

    token = request.json['id']
    decode = jwt.decode(token, secret_key, algorithms=['HS256'])
    id = (decode['id'])

    #retrieve data from database
    cursorLogin = con.cursor(cursor_factory = psycopg2.extras.DictCursor) #key in dictionary
    cursorLogin.execute("select * from person inner join tweets on person.id = tweets.person_id and person.id=%s",(id,))

    dataTweetPersonal = []
    for row in cursorLogin.fetchall():
        dataTweetPersonal.append(dict(row))

    con.commit()

    return jsonify(dataTweetPersonal), 201



@app.route('/getprofileHome', methods=['POST'])
def get_Userprofile():

    token = request.json['id']
    decode = jwt.decode(token, secret_key, algorithms=['HS256'])
    id = (decode['id'])

    cursorProfilhome = con.cursor(cursor_factory = psycopg2.extras.DictCursor)
    cursorProfilhome.execute("select * from person where id = %s",(id,))

    dataprofilHome = []
    for row in cursorProfilhome.fetchall():
        dataprofilHome.append(dict(row))

    con.commit()

    return jsonify(dataprofilHome), 201

@app.route('/getfollowing', methods=['POST','GET'])
def addfollow():
    if request.method == 'POST':

        token = request.json['id']
        decode = jwt.decode(token, secret_key, algorithms=['HS256'])
        id = (decode['id'])

        idfollowing = request.json['id_following']

        curInsertFollow = con.cursor()
        curInsertFollow.execute("Insert into follow(id_person,following) values (%s,%s)",(id,idfollowing))
        con.commit()

        return "Followed", 201
    else:
        return "Method Not Allowed", 400 

@app.route('/deletetweet', methods=['POST'])
def deletetweet():
    if request.method == 'POST' :

        id = request.json['id']

        curdeltweet = con.cursor()
        curdeltweet.execute("DELETE from tweets where id=%s", (id,))
        con.commit()

        return "Tweet has been deleted", 201
    else:
        return "",400


if __name__ == '__main__' :
     app.run(debug=True, host=os.getenv('HOST'),port =os.getenv('PORT')) 
