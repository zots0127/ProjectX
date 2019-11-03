import pymysql
import psutil
from threading import Timer
db = pymysql.connect("s.antistudy.cn", "666", "antistudy", "666")
def update():


    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = f"INSERT INTO clouds_clog( \
       CID, CU, MU, DI, DO,NI,NO,UPT) \
       VALUES ('1', '{psutil.cpu_percent(interval=None, percpu=False)}',  '{psutil.virtual_memory()[2]}',  '{psutil.disk_io_counters(perdisk=False, nowrap=True)[1]}',  '{psutil.disk_io_counters(perdisk=False, nowrap=True)[0]}', '{psutil.net_io_counters(pernic=False, nowrap=True)[0]}','{psutil.net_io_counters(pernic=False, nowrap=True)[1]}','{psutil.boot_time()}')"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接

    Timer(10.0, update).start()

update()
