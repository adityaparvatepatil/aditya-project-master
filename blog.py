from flask import *
import sqlite3


app = Flask(__name__)
conn = sqlite3.connect('database.db',check_same_thread=False,isolation_level=None)
cur = conn.cursor()

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/article',methods=['GET','POST'])
def article1():
    cur.execute('select name,comment from comments where post like "article";')
    res = cur.fetchall()
    comment = list(res) # [0][0])
    #return render_template('post1.html',data=comment)
    return render_template('article.html',data=comment,length=len(comment))
'''
def blog():
    cur.execute('select name,comment from comments where post like "post1";')
    res = cur.fetchall()
    comment = list(res) # [0][0])
    output_string = ""
    #for i in range(len(comment)):
    # 	output_string = 
    #return comment
    return render_template('post1.html',data=comment)
'''

@app.route('/article2',methods=['GET','POST'])
def article2():
    cur.execute('select name,comment from comments where post like "article2";')
    res = cur.fetchall()
    comment = list(res) # [0][0])
    #return render_template('post1.html',data=comment)
    return render_template('article2.html',data=comment,length=len(comment))



@app.route('/article3',methods=['GET','POST'])
def article3():
    cur.execute('select name,comment from comments where post like "article3";')
    res = cur.fetchall()
    comment = list(res) # [0][0])
    #return render_template('post1.html',data=comment)
    return render_template('article3.html',data=comment,length=len(comment))

@app.route('/article4',methods=['GET','POST'])
def article4():
    cur.execute('select name,comment from comments where post like "article4";')
    res = cur.fetchall()
    comment = list(res) # [0][0])
    #return render_template('post1.html',data=comment)
    return render_template('article4.html',data=comment,length=len(comment))


@app.route('/article5',methods=['GET','POST'])
def article5():
    cur.execute('select name,comment from comments where post like "article5";')
    res = cur.fetchall()
    comment = list(res) # [0][0])
    #return render_template('post1.html',data=comment)
    return render_template('article5.html',data=comment,length=len(comment))


@app.route('/article6',methods=['GET','POST'])
def article6():
    cur.execute('select name,comment from comments where post like "article6";')
    res = cur.fetchall()
    comment = list(res) # [0][0])
    #return render_template('post1.html',data=comment)
    return render_template('article6.html',data=comment,length=len(comment))

@app.route('/enter-comment',methods=['POST'])
def enter_comment():
    data = request.form #This is in json
    comment = str(data['comment'])
    postnum = str(data['postnum'])
    name = str(data['name'])
    query_string = "insert into comments values('"+comment+"','"+postnum+"','"+name+"');"
    cur.execute(query_string)
    query_string2 = 'select name,comment from comments where post like "'+postnum+'";'
    cur.execute(query_string2)
    res = cur.fetchall()
    comments = list(res)
    page_name = postnum + '.html'
    return render_template(page_name,data=comments,length=len(comments)) 
    
@app.route('/about-us',methods=['GET','POST'])
def about_us():
    return render_template('about_us.html')
	


