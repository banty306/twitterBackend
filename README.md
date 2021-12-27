

# Backend API Design of Twitter   
  
### Problem Statement
Design API to support basic CRUD functionality for a twitter like system. 

### API Endpoints

 1. /signUp
 2. /login
 3. /addtweet
 4. /dashboard
 5. /readPersonaltweet
 6. /getfollowlist
 7. /getprofileHome
 8. /getfollowing
 9. /deletetweet

#### Functions of each endpoints

 - signUp: This is a post method and accepts username,fullname,email,password,bio, photoprofile as input and make a new entry wrt new email.
 ```
 request format
 {
	 username:"expname"
	 fullname:"banty manjhi",
	 email:"gggg@email.com",
	 password:"hashed value",
	 bio:"about you", 
	 photoprofile:"picture-file"
 }
 ```
 - login: This is a post method which takes in username and password and returns the data of the particular user.
 ```
 request format
 {
	 username:"expname"
	 password:""
 }
 ```
 - addtweet: This is a post method and used to write a tweet. It pushes the tweet based on the id of the logged in user 
 ```
 request format
 {
	 id:"id"
	 tweet:"hello this day is awesome!"
 }
 ```
 - dashboard: This is get method and serves as the base page for our service which shows the tweets so far done by the users.
 - readPersonaltweet: This is post method and returns all the tweets that you have done so far.
```
 request format
 {
	 id:"id"
 }
 ```
 
 - get_following_list: This is post method which returns a lit of users current not followed by the user.
```
 request format
 {
	 id:"id"
 }
 ``` 
 
 - getprofileHome: This is a post method and used to get all the details for a user it also just take id as input.
```
 request format
 {
	 id:"id"
 }
 ``` 
 
 - getfollowing: This serves a get and post for in different scenario if the both id is valid and the user is not already following the user it will return followed or error. 
```
 request format
 {
	 id:"id",
	 idfollowing:"id_following"
 }
 ```
 
 - deletetweet: This act a post method and used to delete an already existing tweet with id same as the id of the current logged user.
```
 request format
 {
	 id:"tweet_id",
 }
 ``` 

### Database table design

 imgggggg

  ### Tech stack used
  

 - Flask (Python)
 - PostgreSQL
 - 
### Functionality 
 - [x] login
 - [x] add tweet
 - [x] follow
 - [ ] retweet
 - [ ] edit details
 - [ ] timeline : this is also a table in db which need to be implemented so that we can improve the speed of the system.

## Further Improvement 
### Another approach for the dashboard or main page  
```  
	@app.route('/dashboard',methods=['GET','POST'])
	def dashboard():
	user_tweet = createTweet()
	if user_tweet.validate_on_submit():
	x = datetime.datetime.now()
	currentTime = str(x.strftime("%d")) +" "+ str(x.strftime("%B")) +"'"+ str(x.strftime("%y")) + " "+ str(x.strftime("%I")) +":"+ str(x.strftime("%M")) +" "+ str(x.strftime("%p"))
	post = Tweets(tweet=user_tweet.tweet.data, stamp=currentTime, author=current_user)
	else:
	post = Tweets(tweet=user_tweet.tweet.data, stamp=currentTime, author=current_user)
	db.session.add(post)
	db.session.commit()
	to_timeline = Timeline(post_id=post.id)
	db.session.add(to_timeline)
	db.session.commit()
	flash('The Tweet was added to your timeline!','success')
	return redirect(url_for('dashboard'))
	page = request.args.get('page',1,type=int)
	timeline = Timeline.query\
	.order_by(desc(Timeline.id))\
	.paginate(page=page,per_page=5)
	return render_template('dashboard.html',name = current_user.username,tweet = user_tweet, timeline=timeline) 
```  
  




