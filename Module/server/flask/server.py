from flask import Flask, render_template, url_for, request
import pymysql
import json

app = Flask(__name__)

def func(sql,m='r'):
    py = pymysql.connect ('s.antistudy.cn','666','antistudy','666',charset="utf8",cursorclass=pymysql.cursors.DictCursor)
    cursor = py.cursor ()
    try:
        cursor.execute (sql)
        if m == 'r':
            data = cursor.fetchall ()
        elif m == 'w':
            py.commit ()
            data = cursor.rowcount
    except:
        data = False
        py.rollback ()
    py.close ()
    return data


@app.route('/')
def my_tem():
    #在浏览器上渲染my_templaces.html模板
    return render_template('home.html')
@app.route('/test',methods=['POST'])
def my_test():
	#创建连接数据库
    connection = pymysql.connect(host='s.antistudy.cn',
                                 user='666',
                                 passwd='antistudy',
                                 db='666',
                                 port=3306,
                                 charset='utf8'
                                 )
    cur=connection.cursor() #游标（指针）cursor的方式操作数据
    sql='SELECT ID,CU,MU,LOAVG,DI,DO,NI,NO FROM clouds_clog WHERE CID=1' #sql语句
    cur.execute(sql) #execute(query, args):执行单条sql语句。
    data=cur.fetchall() #使结果全部可看
    #创建json数据

    jsonData={}
    id=[]
    cu=[]
    mu=[]
    loavg=[]
    di=[]
    do=[]
    ni=[]
    no=[]


    for data in data:
        id.append(data[0])
        cu.append(data[1])
        mu.append(data[2])
        loavg.append(data[3])
        di.append(data[4])
        do.append(data[5])
        ni.append(data[6])
        no.append(data[7])


    jsonData['id'] = id
    jsonData['cu'] = cu
    jsonData['mu'] = mu
    jsonData['loavg'] = loavg
    jsonData['di'] = di
    jsonData['do'] = do
    jsonData['ni'] = ni
    jsonData['no'] = no

    #将json格式转成str，因为如果直接将dict类型的数据写入json会发生报错，因此将数据写入时需要用到该函数。
    j = json.dumps(jsonData)
    cur.close()
    connection.close()
    #渲染html模板
    return (j)


# 首页,将mysql中表的值读出并传到网页----查
@app.route ('/sql')
def index():
    cmd = func ('select * from cmdrun')
    return render_template ('sqldata.html',cmdlist=cmd)


# 返回到添加操作的界面
@app.route ("/add/")
def ad():
    return render_template ('add.html')


# 接受添加的数据,写入数据库----增
@app.route ("/adds/",methods=["POST"])  # 注意post大写,因为post是通过form.data传数据所以下面用request.form
def updatee():
    # 使用cursor()方法获取操作游标
    data = dict(request.form)
    CID = data['CID']
    CMD = data['CMD']
    # SQL 插入语句
    sql = f"INSERT INTO cmdrun (CID, CMD) VALUES ('{CID}', '{CMD}')"
    res = func (sql ,m='w')
    if res:
        return '<script>alert("添加成功");location.href="/sql";</script>'
    else:
       return '<script>alert("添加失败");location.href="/sql";</script>'

# 返回到更改界面
@app.route ('/cha')
def ch():
    idd = request.args.get ('CID')
    data = func (f'select * from cmdrun where CID={idd}')
    return render_template ('cha.html',cmdlist=data)


# 检察更改的数据并更新数据库----改
@app.route ('/chas',methods=["POST"])
def chas():
    data = dict (request.form)
    res = func ("update cmdrun set CID='{CID}',CMD='{CMD}' where CID={CID}".format (**data),m='w')
    if res:
        return '<script>alert("更新成功");location.href="/sql";</script>'
    else:
        return '<script>alert("未更新");location.href="/sql";</script>'


# 删除数据----删
@app.route ('/del')
def de():
    LOGID = request.args.get ('LOGID')
    res = func (f'delete from cmdrun where LOGID={LOGID}',m='w')
    if res:
        return '<script>alert("删除成功");location.href="/sql";</script>'
    else:
        return '<script>alert("删除失败");location.href="/sql";</script>'



if __name__ == "__main__":
    app.run(debug = True) #整个项目的运行
