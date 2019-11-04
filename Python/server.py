import os
import psutil
import pymysql
from threading import Timer


def fuck():
    print('fuck')


def infodbcreatetable():
    db = pymysql.connect("s.antistudy.cn", "666", "antistudy", "666")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # 使用预处理语句创建表
    sql = """CREATE TABLE SERVER (
         id  int(20) NOT NULL,
         location  CHAR(20),
         cloud CHAR(20),  
         cpu CHAR(20),
         memory CHAR(20),
         disk CHAR(20) )"""

    cursor.execute(sql)

    # 关闭数据库连接
    db.close()


def dbselect():
    db = pymysql.connect("s.antistudy.cn", "666", "antistudy", "666")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM CLIENTINFO "
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            ip = row[1]
            location = row[2]
            cloud = row[3]
            cpucore = row[4]
            memory = row[5]
            disk = row[6]
            # 打印结果
            print("id:%s\nip:%s\nlocation=%s\ncloud=%s\ncpucore=%s\nmemory=%s\ndisk=%s" % \
                  (id, ip, location, cloud, cpucore, memory, disk))
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    db.close()
    # 打开数据库连接


def dbupdate():
    db = pymysql.connect("s.antistudy.cn", "666", "antistudy", "666")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()


def dbinsert():
    db = pymysql.connect("s.antistudy.cn", "666", "antistudy", "666")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = f"INSERT INTO client( \
       loadavg, cpupercent, memoryper, storage, iow, ior,netin,netout,nettraffic) \
       VALUES ('{psutil.getloadavg()[0]}', '{psutil.cpu_percent(interval=None, percpu=False)}',  '{psutil.virtual_memory()[2]}',  '{psutil.cpu_count(logical=True)}',  '4', '{'5'}','{'6'}','{'7'}','{'8'}')"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()
    Timer(10.0, dbinsert).start()

def dbdel():
    db = pymysql.connect("s.antistudy.cn", "666", "antistudy", "666")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 删除语句
    sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (19)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭连接
    db.close()


psutil.cpu_times(percpu=False)  # cost of time
psutil.cpu_percent(interval=None, percpu=False)  # use percent of cpu
psutil.cpu_count(logical=True)  # cpu_count
psutil.cpu_stats()  # cpu information
psutil.getloadavg()  # ava fuzai
psutil.virtual_memory()  # memory information
psutil.disk_io_counters(perdisk=False, nowrap=True)  # I/O
psutil.net_io_counters(pernic=False, nowrap=True)  # net I/O
psutil.boot_time()  # start time
psutil.users()

print(psutil.disk_io_counters(perdisk=False, nowrap=True))

dbinsert()