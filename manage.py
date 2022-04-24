# coding=utf-8
from flask import Flask, render_template
import pymysql
from flask import request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template("index.html")


# 添加数据
@app.route('/submit_insert', methods=['GET', 'POST'])
def submit_insert():
    return render_template("sql_insert.html")


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        # 从数据库获取信息
        name1 = request.values.get('name')
        age1 = request.values.get('age')
    elif request.method == 'POST':
        # 添加数据
        try:
            # 从网页表单获取数据
            name1 = request.form['name']
            age1 = request.form['age']
        except KeyError:
            ret = {'code': 10001, 'message': '参数不能为空！'}
            return json.dumps(ret, ensure_ascii=False)
    # 数据非空
    if name1 and age1:
        # 打开数据库连接
        db = pymysql.connect(host="localhost", port=3309, user="root", password="123456", database="test",
                             charset="utf8")
        # 使用cursor（）方法创建一个游标对象cursor
        cursor = db.cursor()
        # sql插入语句 拼接注意字符串要加引号
        sql = "insert into test(name,age) values ('" + name1 + "' ," + age1 + ")"
        try:
            cursor.execute(sql)
            # 提交
            db.commit()
            ret = {'code': 200, 'message': '添加成功！'}
            return json.dumps(ret)
        except Exception as e:
            # 错误回滚
            db.rollback()
            ret = {'code': 10002, 'message': '添加失败！'}
            return json.dumps(ret)
        finally:
            db.close()


# 删除数据
@app.route('/submit_delete')
def submit_delete():
    return render_template("sql_delete.html")


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'GET':
        id1 = request.values.get('id')
    elif request.method == 'POST':
        try:
            # 从网页表单获取id
            id1 = request.form['id']
        except KeyError:
            ret = {'code': 10001, 'message': '参数不能为空！'}
            return json.dumps(ret, ensure_ascii=False)
    if id1:
        # 打开数据库连接
        db = pymysql.connect(host="localhost", port=3309, user="root", password="123456", database="test")
        # 使用cursor（）方法创建一个游标对象cursor
        cursor = db.cursor()
        # sql删除语句
        sql = "delete from test where id =" + id1
        sql1 = "alter table test drop id"
        sql2 = "alter table test add id int not null first"
        sql3 = "alter table test modify column id int not null auto_increment,add primary key(id)"
        try:
            cursor.execute(sql)
            cursor.execute(sql1)
            cursor.execute(sql2)
            cursor.execute(sql3)
            # 提交
            db.commit()
            ret = {'code': 200, 'message': '删除成功！'}
            return json.dumps(ret)
        except Exception as e:
            # 错误回滚
            db.rollback()
            ret = {'code': 10003, 'message': '删除失败！'}
            return json.dumps(ret)
        finally:
            db.close()


# 修改数据
@app.route('/submit_update')
def submit_update():
    return render_template("sql_update.html")


@app.route('/update', methods=['GET', 'POST'])
def modify():
    if request.method == 'GET':
        id1 = request.values.get('id')
        name1 = request.values.get('name')
        age1 = request.values.get('age')
    elif request.method == 'POST':
        try:
            id1 = request.form['id']
            name1 = request.values.get('name')
            age1 = request.values.get('age')
        except KeyError:
            ret = {'code': 10001, 'message': '参数不能为空！'}
            return json.dumps(ret, ensure_ascii=False)
    if name1 and age1:
        # 打开数据库连接
        db = pymysql.connect(host="localhost", port=3309, user="root", password="123456", database="test")
        # 使用cursor（）方法创建一个游标对象cursor
        cursor = db.cursor()
        # sql修改语句
        sql = "update test set age =" + age1 + ", name = '" + name1 + "'where id = " + id1
        sql1 = "select count(1) from test"
        try:
            cursor.execute(sql)
            # 提交
            db.commit()
            ret = {'code': 200, 'message': '修改成功！'}
            return json.dumps(ret)
        except Exception as e:
            # 错误回滚
            db.rollback()
            ret = {'code': 10004, 'message': '修改失败！'}
            return json.dumps(ret)
        finally:
            db.close()


# 根据id查询数据
@app.route('/submit_select', methods=['GET', 'POST'])
def submit_select():
    return render_template("sql_select.html")


@app.route('/query', methods=['GET', 'POST'])
def query():
    if request.method == 'GET':
        id1 = request.values.get('id')
    elif request.method == 'POST':
        try:
            id1 = request.form['id']
        except KeyError:
            ret = {'code': 10001, 'message': '参数不能为空！'}
            return json.dumps(ret, ensure_ascii=False)
    if id1:
        # 打开数据库连接
        db = pymysql.connect(host="localhost", port=3309, user="root", password="123456", database="test")
        # 使用cursor（）方法创建一个游标对象cursor
        cursor = db.cursor()
        # sql查询语句
        sql = "select * from test where id = " + id1
        try:
            cursor.execute(sql)
            # 提交
            db.commit()
            results = cursor.fetchall()
            # 遍历结果
            for rows in results:
                id1 = rows[0]
                name1 = rows[1]
                age1 = rows[2]

            if name1 and age1:
                ret = {'code': 200, 'message': '查询成功！'}
                return json.dumps(ret)
            else:
                ret = {'code': 10005, 'message': '查询失败！'}
                # print("id=%s,name=%s,age=%s" % (id1, name1, age1))
                return json.dumps(ret)
        except Exception as e:
            # 错误回滚
            db.rollback()
            ret = {'code': 10005, 'message': '查询失败！'}
            return json.dumps(ret)
        finally:
            db.close()
    else:
        ret = {'code': 10001, 'message': '参数不能为空！'}
        return json.dumps(ret, ensure_ascii=False)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 指定端口和ip
    app.run(debug=True, host='127.0.0.1', port=5000)
