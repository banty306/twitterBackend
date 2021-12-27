# twitterBackend



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


### Functionality 
~~login~~
~~add tweet~~
~~follow~~
retweet 
edit details
timeline: this is also a table in db which need to be implemented so that we can improve the speed of the system.

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
  
**On \*nix:**  
  
```  
./task.sh  
```  
## Run Automated Tests  
  
### 1. Install Node.js  
  
You need to have npm installed in your computer for this problem. It comes with Node.js and you can get it by installing Node from https://nodejs.org/en/  
  
### 2. Install dependencies  
  
Run `npm install` to install all dependencies.  
  
### 3. Create Create symbolic link to the executable file  
  
#### On Windows  
  
To create a symbolic link on Windows, you'll need to run either the Windows Command Prompt, or Windows Powershell **with administrator privileges**. To do so, right-click on the icon for Command Prompt, or Powershell, and choose the _"Run as Administrator"_ option.  
  
**Command Prompt:**  
  
```  
> mklink task task.bat  
```  
  
**Powershell:**  
  
```  
> cmd /c mklink task task.bat  
```  
  
#### On \*nix:  
  
Run the following command in your shell:  
  
```  
$ ln -s task.sh task  
```  
  
### 4. Try running tests.  
  
Now run `npm test` and you will see all the tests failing. As you fill in each functionality, you can re-run the tests to see them passing one by one.  
  
## A Note about `/` for Windows Users  
  
In the following sections, you'll see many commands prefixed with `./`, or paths containing the `/` (forward-slash) character.  
  
If you're using the Windows _Command Prompt_, then you'll need to replace `/` with `\` (back-slash) for these commands and paths to work as expected.  
  
On Windows _Powershell_, these substitutions are not required.  
  
## Known Issues  
  
A few notes to help you avoid any hiccups while implementing the programming challenge:  
  
1. If you are on Windows, you might have difficulty getting the tests to pass because of newline UTF encoding issues. If you get stuck, please [refer to the thread here](https://github.com/nseadlc-2020/package-todo-cli-task/issues/12).  
  
2. In Windows machines, the `make` command might not exist and can prevent you from running the tests. This can be fixed [by using WSL, or installing MinGW, among other options](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows).  
  
## Specification  
  
1. The app can be run in the console with `./task`.  
  
2. The app should read from and write to a task.txt text file. Each task occupies a single line in this file. Each line in the file should be in this format :  
  
```  
p task  
```  
  
where `p` is the priority ( priority will be a number) and `task` is the task description.  
  
> Priority denotes how important a task is, if it is a high priority task, it should be completed earlier. Priority is denoted using an integer, the lower the number, the higher the priority.  
  
Here is an example file that has 2 items.  
  
```  
1 Buy milk  
2 Complete the project  
```  
  
3. Completed task are writted to a completed.txt file. Each task occupies a single line in this file. Each line in the file should be in this format :  
  
```  
task  
```  
  
where task is the task description.  
  
Here is an example file that has 2 items.  
  
```  
Buy milk  
Complete the project  
```  
  
4. Priority can be any integer _greater than_ or _equal to_ 0. 0 being the highest priority  
  
5. If two task have the same priority, the task that was added first should be displayed first.  
  
The application must open the files task.txt and completed.txt from where the app is run, and not where the app is located. For example, if we invoke the app like this:  
  
6. The files should always be sorted in order of the priority, ie, the task with the highest priority should be first item in the file.  
  
```  
$ cd /path/to/plans  
  
$ /path/to/apps/task ls  
```  
  
The application should look for the text files in `/path/to/plans`, since that is the userâ€™s current directory.  
  
> Please note that the programming task could be completed without the use of any additional packages  
  
## Usage  
  
### 1. Help  
  
Executing the command without any arguments, or with a single argument help prints the CLI usage.  
  
```  
$ ./task help  
Usage :-  
$ ./task add 2 hello world  # Add a new item with priority 2 and text "hello world" to the list  
$ ./task ls  # Show incomplete priority list items sorted by priority in ascending order  
$ ./task del INDEX  # Delete the incomplete item with the given index  
$ ./task done INDEX  # Mark the incomplete item with the given index as complete  
$ ./task help  # Show usage  
$ ./task report  # Statistics  
```  
  
### 2. List all pending items  
  
Use the ls command to see all the items that are not yet complete, in ascending order of priority.  
  
Every item should be printed on a new line. with the following format  
  
```  
[index] [task] [priority]  
```  
  
Example:  
  
```  
$ ./task ls  
1. change light bulb [2]  
2. water the plants [5]  
```  
  
index starts from 1, this is used to identify a particular task to complete or delete it.  
  
### 3. Add a new item  
  
Use the add command. The text of the task should be enclosed within double quotes (otherwise only the first word is considered as the item text, and the remaining words are treated as different arguments).  
  
```  
$ ./task add 5 "the thing i need to do"  
Added task: "the thing i need to do" with priority 5  
```  
  
### 4. Delete an item  
  
Use the del command to remove an item by its index.  
  
```  
$ ./task del 3  
Deleted item with index 3  
```  
  
Attempting to delete a non-existent item should display an error message.  
  
```  
$ ./task del 5  
Error: item with index 5 does not exist. Nothing deleted.  
```  
  
### 5. Mark a task as completed  
  
Use the done command to mark an item as completed by its index.  
  
```  
$ ./task done 1  
Marked item as done.  
```  
  
Attempting to mark a non-existed item as completed will display an error message.  
  
```  
$ ./task done 5  
Error: no incomplete item with index 5 exists.  
```  
  
### 6. Generate a report  
  
Show the number of complete and incomplete items in the list. and the complete and incomplete items grouped together.  
  
```  
$ ./task report  
Pending : 2  
1. this is a pending task [1]  
2. this is a pending task with priority [4]  
  
Completed : 3  
1. completed task  
2. another completed task  
3. yet another completed task  
```
