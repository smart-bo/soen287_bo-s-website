from flask import Flask,Response,render_template,request, session, redirect, url_for
import json


app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    if not session.get('username'):
        return render_template('home.html')
    else:
        return render_template('home.html',message="welcome "+session.get('username'))

@app.route("/about")
def about():
    return render_template("about.html")   

@app.route("/mylife")
def mylife():
    return render_template("mylife.html")

@app.route("/history")
def education():
    return render_template("history.html")

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method.lower() == 'get':
        return render_template("login.html")
    elif request.method.lower() == 'post':

        _user=request.form['username']
        _pass=request.form['password']

        file_data=open(r'C:\Users\maybe\Desktop\287\version4.1\data\user.json','r').read()
        user_data=json.loads(file_data)




        for item in user_data:
            if item['username']==_user and item['password']==_pass:
                session['username']=_user
                break
      
        
        if session.get('username'):
            return redirect(url_for('home'))
        else :
            return render_template('login.html',message="user/pass combination not right!")

        #if request.form['username'] == _user and request.form['password'] == _pass:
        #   session['username'] = _user
        #   return redirect(url_for('home'))
        #else:
        #   return render_template('login.html',message="user/pass combination not right!")

@app.route('/logout')
def logout():
    session.clear()

    return redirect(url_for('home'))    



@app.route("/contact",methods=['post','get'])
def contact():
    if request.method.lower()=='get':
        return render_template('contact.html')
    elif request.method.lower()=='post':

        _ID=request.form['ID']
        _comment=request.form['comment'] 

        file_data=open(r'C:\Users\maybe\Desktop\287\version4.1\data\message.json','r').read()
        users_message=json.loads(file_data)      

        users_message.append(
            {
                "ID":_ID,
                "comment":_comment
            }
        )  

        out_file=open(r'C:\Users\maybe\Desktop\287\version4.1\data\message.json','w')
        json.dump(users_message,out_file,indent=4)

        return render_template('contact.html',message="comment send")



@app.route("/register",methods=['post','get'])
def register():
    if request.method.lower()=='get':
        return render_template('register.html')
    elif request.method.lower()=='post':

        _username=request.form['username']
        _password1=request.form['password1'] 
        _password2=request.form['password2']

        file_data=open(r'C:\Users\maybe\Desktop\287\version4.1\data\user.json','r').read()
        users_data=json.loads(file_data)

        

        if len(_username)<4:
            return render_template('register.html',message="username should have more than 4 characters!")
        elif _password1 != _password2:
            return render_template('register.html',message="passwords don't match")
        for item in users_data:
            if item['username']==_username:
                return render_template('register.html',message="username exitst! try another one")
        users_data.append(
            {
                "username":_username,
                "password":_password1

            }
        )

        out_file=open(r'C:\Users\maybe\Desktop\287\version4.1\data\user.json','w')
        json.dump(users_data,out_file,indent=4)

        return render_template('register.html',message="user registered")


@app.route("/userlist")
def users():

    #Reading the file content
    file_data = open(r'C:\Users\maybe\Desktop\287\version4.1\data\user.json','r').read()
    data = json.loads(file_data)

    #Sending the file content to the HTML template
    return render_template ('userlist.html', users = data)




if __name__=="__main__":
    app.secret_key = "287"
    app.run(debug=True)

 
