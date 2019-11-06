import pymysql
import psutil
import subprocess
import time
import os
from threading import Timer

#配置部分：数据库信息以及本机CID
db = pymysql.connect("s.antistudy.cn", "666", "antistudy", "666")
#数据库地址以及用户名密码等
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
#暂不使用
def checkcmd():

    youbiao = db.cursor()

    sqlc = f"select LOGID,CMD from cmdrun where CID = %s and STATU = '0' " %(CID)
    #获取当CID为本机CID时需要执行的命令以及该命令编号


    print('Check new commad')

    try:
        youbiao.execute(sqlc)
        #执行查询命令
        print('Check New Command from Main Server')
        emptytuple = ()
        cresult = youbiao.fetchall()
        #获取查询到的所有数据
        if cresult is emptytuple:
            #判断是否有新命令（判断元组是否为空）
            print('No New Command')

        else:

            for row in cresult:

                LOGID = row[0]

                CMD = row[1]

            print(type(cresult))
            statusdate = f"update cmdrun SET STATU = '1' WHERE LOGID = %s " % LOGID
            youbiao.execute(statusdate)
            print('Command Status Update')
            db.commit()
            print('New Command Received.Running')

            print('Getting Result')

            cmdresult = os.popen(CMD)



            fanhuizhi = cmdresult.read()
            print(type(fanhuizhi))
            print('Get Result')

            #os.popen(CMD).readlines()[0]






            resultupdate = f"update cmdrun SET RESULT = '%s' WHERE LOGID = '%s' " %(fanhuizhi,LOGID)

            #执行完命令之后更新返回结果到数据库


            #youbiao.execute(sqlupdate)
            #更新命令执行状态
            #测试环境不真实执行

            print('Command run complete.')

            youbiao.execute(resultupdate)
            #更新执行结果到数据库
            print("Update command result")

            db.commit()
            #提交到数据库
    except:

        db.rollback()
#检查新命令
def update():

    checkcmd()
    #检查新命令
    cursor = db.cursor()

    sql = f"INSERT INTO clouds_clog( CID, CU, MU,LOAVG, DI, DO,NI,NO) VALUES ('{CID}', '{psutil.cpu_percent(interval=None, percpu=False)}',  '{psutil.virtual_memory()[2]}','{psutil.getloadavg()[0]}',  '{psutil.disk_io_counters(perdisk=False, nowrap=True)[3]}',  '{psutil.disk_io_counters(perdisk=False, nowrap=True)[2]}', '{psutil.net_io_counters(pernic=False, nowrap=True)[0]}','{psutil.net_io_counters(pernic=False, nowrap=True)[1]}')"


    try:
        # 执行sql语句
        cursor.execute(sql)


        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    print('Print IS Only For Test')
    print(time.asctime( time.localtime(time.time()) ))
    print('Server Status info Send Success!\n\n\n')
    Timer(5.0, update).start()
#更新监控数据
update()