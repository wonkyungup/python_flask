from flask import Flask, request, redirect, url_for,render_template,session  # @UnresolvedImport
import sqlite3
from matplotlib.pyplot import title
from gi.overrides.Gdk import name
#from Onboard.OnboardGtk import app




app = Flask(__name__)
app.secret_key="any random string"

'''conn = sqlite3.connect('KFC_DB.db')
conn.execute('CREATE TABLE MEMBER (id TEXT, password TEXT)')
conn.close()'''

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/logout')
def logout():
    session.clear()
    return render_template("index.html")

@app.route('/mypage')
def mypage():
    return render_template("Mypasge/mypage.html")

@app.route('/member_detail')
def mypage_member_detail():
    id=session['id']
    password = "text"
    name = "wonkyungup"
    
    con=sqlite3.connect("KFC_DB.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor();
    cur.execute("select password,name from MEMBER where id='"+id+"';")
    rows = cur.fetchall();
    cur.close()
    con.close()
    
    for row in rows:
        password= row[0]
        name = row[1]
    
    retVal={'id':id,'password':password,'name':name}
    return render_template("Mypasge/member_detail.html",member=retVal)

@app.route('/PWupdate_action',methods = ['POST'])
def PWupdate_action():
    if request.method == 'POST':
        #id=request.form['id']
        #password=request.form['password']
        id=session['id']
        password=request.form['password'];
    
        con=sqlite3.connect("KFC_DB.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor();
        cur.execute("update MEMBER set password='"+password+"' where id='"+id+"';")
        rows = cur.fetchall();
        con.commit();
        cur.close()
        con.close()

    return render_template("Mypasge/mypage.html")

@app.route('/schedule')
def schedule():
    return render_template("Mypasge/schedule.html")

@app.route('/body_state_information')
def body_state():
    return render_template("Mypasge/body_state_information.html")

@app.route('/login')
def login():
    retVal={'id':'','password':'','result':True}
    return render_template("member/login.html",result=retVal)

@app.route('/login_action',methods = ['POST'])
def login_action():
    if request.method == 'POST':
        id=request.form['id']
        password=request.form['password']
        value='';
        name='';
        
        con=sqlite3.connect("KFC_DB.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor();
        cur.execute("select password,name from MEMBER where id='"+id+"';")
        rows = cur.fetchall();
        cur.close()
        con.close()
        
        if len(rows)==0:
            retVal={'id':id,'password':password,'result':False}
            return render_template("member/login.html",result=retVal) #아이디가 없습니다
        
        else:
            for row in rows:
                value = row[0]
                name = row[1]
        
        if value==password:
            session['name']=name;
            session['id']=id;
            session['logged_in'] = True
            return render_template("index.html",result = name)
        else:
            retVal={'id':id,'password':password,'result':False}
            return render_template("member/login.html",result=retVal) #비밀번호가 일치하지 않습니다

@app.route('/join')
def join():
    return render_template("member/join.html")

@app.route('/join_action',methods = ['POST'])
def join_action():
    if request.method == 'POST':
        try:
            id=request.form['id']
            password=request.form['password']
            name=request.form['name']
            with sqlite3.connect("KFC_DB.db") as con:
                cur = con.cursor()
                cur.execute("insert into MEMBER (id,password,name) values ('"+id+"','"+password+"','"+name+"');")
                con.commit();
        except: con.rollback();
        finally:
            cur.close()
            con.close()
            retVal={'id':'','password':'','result':True}
            return render_template("member/login.html",result=retVal)

 #<--------------------------------------------------PT & gT

@app.route('/PT')
def PT():
    return render_template("training/PT.html")

@app.route('/GT')
def GT():
    return render_template("training/GT.html")


@app.route('/PT_detail')
def PT_detail():
    return render_template("training/PT_detail.html")

@app.route('/person')
def person():
    return render_template("training/person.html")

@app.route('/person_detail')
def person_detail():
    return render_template("training/person_detail.html")

#@app.route('/PT_detail_action',methods = ['POST'])
#def PT_detail_action():
    

@app.route('/PT_GT')
def PT_GT():
    return render_template("training/PT_GT.html")

 #<--------------------------------------------------PT & GT

@app.route('/idcheck',methods = ['POST'])
def idcheck():
    id=request.form['id']
    
    con=sqlite3.connect("KFC_DB.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor();
    cur.execute("select name from MEMBER where id='"+id+"';")
    rows = cur.fetchall();
    cur.close()
    con.close()
    
    if len(rows)==0:
        return 'T'
        
    else:
        return 'F'
   #<--------------------------------------------------신청하기
@app.route('/buy')
def buy():
    id=session['id']
    password = "text"
    name = "wonkyungup"
    
    con=sqlite3.connect("KFC_DB.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor();
    cur.execute("select password,name from MEMBER where id='"+id+"';")
    rows = cur.fetchall();
    cur.close()
    con.close()
    
    for row in rows:
        password= row[0]
        name = row[1]
    
    retVal={'id':id,'password':password,'name':name}
    
    return render_template("buy.html",member=retVal)

@app.route('/finish')
def finish():
    id=session['id']
    password = "text"
    name = "wonkyungup"
    
    con=sqlite3.connect("KFC_DB.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor();
    cur.execute("select password,name from MEMBER where id='"+id+"';")
    rows = cur.fetchall();
    cur.close()
    con.close()
    
    for row in rows:
        password= row[0]
        name = row[1]
    
    retVal={'id':id,'password':password,'name':name}
    
    return render_template("finish.html",member=retVal)

@app.route('/buy_action',methods = ['POST'])
def buy_action():

        return finish()

   #<--------------------------------------------------신청하기
   
   #<--------------------------------------------------게시판
@app.route('/qna')
def qna():
    id=session['id']
    title = "text"
    content = "text"
    no = 0
    
    con=sqlite3.connect("KFC_DB.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor();
    cur.execute("select no,title,content,id from QA;")
    rows = cur.fetchall();
    cur.close()
    con.close()
    
    for row in rows:
        no = row[0]
        title = row[1]
        content = row[2]
        id = row[3]
    
    retVal={'id':id,'no':no,'title':title,'content':content}
    return render_template("qna.html",qna=rows)

@app.route('/qna_action',methods = ['POST'])
def qna_action():
   if request.method == 'POST':
        try:
            title=request.form['title']
            writer=request.form['writer']
            content=request.form['content']
            with sqlite3.connect("KFC_DB.db") as con:
                cur = con.cursor()
                cur.execute("insert into QA (title,ID,content) values ('"+title+"','"+writer+"','"+content+"');")
                con.commit();
        except: con.rollback();
        finally:
            cur.close()
            con.close()
            return qna()
        
@app.route('/wq')
def wq():
    return render_template("wq.html")

@app.route('/wq_detail',methods = ['GET'])
def wq_detail():
    
    no=request.args.get('no')
    title=""
    content=""
    id=""
    
    con=sqlite3.connect("KFC_DB.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor();
    cur.execute("select title,content,id from QA where no="+no+";")
    rows = cur.fetchall();
    cur.close()
    con.close()
    
    for row in rows:
        title = row[0]
        content = row[1]
        id = row[2]
    
    retVal={'id':id,'title':title,'content':content,'no':no}
    
    return render_template("wq_detail.html",result=retVal)

@app.route('/wq_detail_action',methods = ['POST'])
def wq_detail_action():
    if request.method == 'POST':
        no=request.form['no']
        
        con=sqlite3.connect("KFC_DB.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor();
        cur.execute("delete from QA where no='"+no+"';")
        con.commit();
        cur.close()
        con.close()
        
        return qna()
    
    #<--------------------------------------------------게시판
    
    #<--------------------------------------------------페이지링
    
    

    #<--------------------------------------------------페이지링

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
    
    
    
    
    

'''

@app.route('/wq_detail_delete_action',methods = ['POST'])
def wq_detail_delete_action():
        no=request.form['no']
        
        con=sqlite3.connect("KFC_DB.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor();
        cur.execute("delete from QA where no='"+no+"';")
        con.commit();
        cur.close()
        con.close()
        
        return qna()
    
@app.route('/httpmethod_success/<myname>')
def httpmethod_success(myname):
    return 'welcome ' + myname

@app.route('/httpmethod', methods=['POST', 'GET'])
def httpmethod():
    if request.method == 'POST':
        user = request.form['myname']
    else:
        user = request.args.get('myname')
    return redirect(url_for('httpmethod_success', myname=user))

@app.route('/template_base/<user>')
def hello_name(user):
    return render_template('template_base.html',myname=user)'''
