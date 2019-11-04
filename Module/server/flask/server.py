from flask import Flask,render_template,url_for
import pymysql
import json

app = Flask(__name__)
@app.route('/index/')
def my_tem():
    #在浏览器上渲染my_templaces.html模板
    return render_template('index.html')
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
    sql='SELECT ID,CU FROM clouds_clog WHERE CID=1' #sql语句
    cur.execute(sql) #execute(query, args):执行单条sql语句。
    data=cur.fetchall() #使结果全部可看
    #创建json数据

    jsonData={}
    xid=[]
    ycu=[]

    for data in data:
        xid.append(data[0])
        ycu.append(data[1])

    jsonData['xid']=xid
    jsonData['ycu']=ycu

    #将json格式转成str，因为如果直接将dict类型的数据写入json会发生报错，因此将数据写入时需要用到该函数。
    j = json.dumps(jsonData)
    cur.close()
    connection.close()
    #渲染html模板
    return (j)

if __name__ == "__main__":
    app.run(debug = True) #整个项目的运行
