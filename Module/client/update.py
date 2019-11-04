import pymysql
import psutil
import subprocess
import os
from threading import Timer
db = pymysql.connect("s.antistudy.cn", "666", "antistudy", "666")
CID = 1
def updateresult(CMD,LOGID):
    updateresult =db.cursor()

    sqlupdate = f"update cmdrun SET STATU = '1' WHERE cmdrun.LOGID =%s" % LOGID
    rres = os.popen(CMD).readlines()
    print("123123")
    #resultupdate =f"update cmdrun SET RESULT = %s WHERE cmdrun.LOGIN  =%s" %rres %LOGID
    updateresult.execute(sqlupdate)
    #updateresult.execute(resultupdate)
    print("update success1")
def checkcmd():
    youbiao = db.cursor()
    print('1')
    sqlc = f"select LOGID,CMD from cmdrun where LOGID ='1' and STATU = '0' "
    sqlupdate = f"update cmdrun SET STATU = '1' WHERE LOGID = '1' "

    print('2')

    try:
        youbiao.execute(sqlc)
        print('3')

        chaxunjieguo = youbiao.fetchall()
        for row in chaxunjieguo:
            LOGID = row[0]
            CMD = row[1]
        print('4')

        fanhuizhi = os.popen(CMD).readlines()[0]
        #print(os.popen(CMD)[0])
        resultupdate = f"update cmdrun SET RESULT = '%s' WHERE LOGID = '1' " %(fanhuizhi)
        print('5')
        youbiao.execute(sqlupdate)
        print('111111')
        youbiao.execute(resultupdate)
        print("update success2")
        db.commit()
    except:
        db.rollback()
def dbins():
    print()
def dbsel():
    print()
def update():
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = f"INSERT INTO clouds_clog( \
       CID, CU, MU, DI, DO,NI,NO,UPT) \
       VALUES ('{CID}', '{psutil.cpu_percent(interval=None, percpu=False)}',  '{psutil.virtual_memory()[2]}',  '{psutil.disk_io_counters(perdisk=False, nowrap=True)[1]}',  '{psutil.disk_io_counters(perdisk=False, nowrap=True)[0]}', '{psutil.net_io_counters(pernic=False, nowrap=True)[0]}','{psutil.net_io_counters(pernic=False, nowrap=True)[1]}','{psutil.boot_time()}')"
    #sqlupdate = f"update cmdrun SET STATU = '1' WHERE LOGID = '1' " #测试update功能

    try:
        # 执行sql语句
        cursor.execute(sql)
        #cursor.execute(sqlupdate)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接

    Timer(5.0, update).start()

checkcmd()
