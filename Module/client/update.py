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
    #sqlupdate = f"update cmdrun SET STATU = '1' WHERE LOGID = %s " %LOGID

    print('准备执行数据库查询命令')

    try:
        youbiao.execute(sqlc)
        #执行查询命令
        print('执行命令成功，判断获取结果是否为空')
        emptytuple = ()
        cresult = youbiao.fetchall()
        #获取查询到的所有数据
        if cresult is emptytuple:
            #判断是否有新命令（判断元组是否为空）
            print('没有收到新的命令')

        else:

            for row in cresult:

                LOGID = row[0]

                CMD = row[1]
            print(type(cresult))
            print('收到新的命令，准备执行')

            print('获取执行结果中')

            fanhuizhi = 'fakeresult'
            print('结果获取成功')

            #os.popen(CMD).readlines()[0]
            print('准备上传结果到数据库')

            #print(os.popen(CMD)[0])

            resultupdate = f"update cmdrun SET RESULT = '%s' WHERE LOGID = '%s' " %(fanhuizhi,LOGID)

            #执行完命令之后更新返回结果到数据库

            print('上传中')

            #youbiao.execute(sqlupdate)
            #更新命令执行状态
            #测试环境不真实执行

            print('任务完成')

            youbiao.execute(resultupdate)
            #更新执行结果到数据库
            print("结束命令")

            db.commit()
            #提交到数据库
    except:

        db.rollback()
#检查新命令
def update():
    checkcmd()
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
    print(time.asctime( time.localtime(time.time()) ))
    print('已更新服务器状态到数据库\n\n\n')
    Timer(30.0, update).start()
#更新监控数据
update()