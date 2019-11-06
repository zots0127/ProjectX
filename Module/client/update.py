import pymysql
import psutil
import subprocess
import datetime
import os
from threading import Timer

#配置部分：数据库信息以及本机CID
db = pymysql.connect("s.antistudy.cn", "666", "antistudy", "666")

CID: int = 1
#clientID
def updateresult(CMD,LOGID):
#暂时没用
    updateresult =db.cursor()

    sqlupdate = f"update cmdrun SET STATU = '1' WHERE cmdrun.LOGID =%s" % LOGID

    rres = os.popen(CMD).readlines()

    #resultupdate =f"update cmdrun SET RESULT = %s WHERE cmdrun.LOGIN  =%s" %rres %LOGID

    updateresult.execute(sqlupdate)

    #updateresult.execute(resultupdate)

def checkcmd():

    youbiao = db.cursor()

    sqlc = f"select LOGID,CMD from cmdrun where CID = %s and STATU = '0' " %(CID)
    #获取当CID为本机CID时需要执行的命令以及该命令编号
    #sqlupdate = f"update cmdrun SET STATU = '1' WHERE LOGID = %s " %LOGID

    print('2')

    try:
        youbiao.execute(sqlc)
        #执行查询命令
        print('3')
        emptytuple = ()
        cresult = youbiao.fetchall()
        #获取查询到的所有数据
        if cresult is emptytuple:
            #判断是否有新命令（判断元组是否为空）
            print('no command')

        else:

            for row in cresult:

                LOGID = row[0]

                CMD = row[1]
            print(type(cresult))
            print('have command')

        print('4')

        fanhuizhi = 'fakeresult'
        print('4')

        #os.popen(CMD).readlines()[0]
        print('4')

        #print(os.popen(CMD)[0])

        resultupdate = f"update cmdrun SET RESULT = '%s' WHERE LOGID = '%s' " %(fanhuizhi,LOGID)

        #执行完命令之后更新返回结果到数据库

        print('5')

        #youbiao.execute(sqlupdate)
        #更新命令执行状态
        #测试环境不真实执行

        print('111111')

        youbiao.execute(resultupdate)
        #更新执行结果到数据库
        print("update success2")

        db.commit()
        #提交到数据库
    except:

        db.rollback()

def update():

    cursor = db.cursor()

    sqlc = f"select LOGID,CMD from cmdrun where CID ='%s' and STATU = '0' " %CID

    sql = f"INSERT INTO clouds_clog( \
       CID, CU, MU,LOAVG, DI, DO,NI,NO) \
       VALUES ('{CID}', '{psutil.cpu_percent(interval=None, percpu=False)}',  '{psutil.virtual_memory()[2]}','{psutil.getloadavg()[0]}',  '{psutil.disk_io_counters(perdisk=False, nowrap=True)[3]}',  '{psutil.disk_io_counters(perdisk=False, nowrap=True)[2]}', '{psutil.net_io_counters(pernic=False, nowrap=True)[0]}','{psutil.net_io_counters(pernic=False, nowrap=True)[1]}')"
    #statusupdata = f"update cmdrun SET STATUS = '1' WHERE LOGID = '1' " #测试update功能 每次执行完命令之后更新状态为1

    try:
        # 执行sql语句
        cursor.execute(sqlc)

        checkvalue = cursor.fetchall()

        for row in checkvalue:

            LOGID = row[0]

            CMD = row[1]

        cursor.execute(sql)

        #cursor.execute(sqlupdate)

        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接

    Timer(30.0, update).start()

checkcmd()