from flask import Flask
from flask import Flask, request, render_template, url_for
from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import hashlib
import uuid

# def hash_password(password):
#     # uuid используется для генерации случайного числа
#     salt = uuid.uuid4().hex
#     return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
# def check_password(hashed_password, user_password):
#     password, salt = hashed_password.split(':')
#     return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 
# new_pass = input('Введите пароль: ')
# hashed_password = hash_password(new_pass)
# print('Строка для хранения в базе данных: ' + hashed_password)
# old_pass = input('Введите пароль еще раз для проверки: ')
 
# if check_password(hashed_password, old_pass):
#     print('Вы ввели правильный пароль')
# else:
#     print('Извините, но пароль не подходит')

app = Flask(__name__)


@app.route('/login/', methods =["GET", "POST"])
def login():
    hashpass = "21232f297a57a5a743894a0e4a801fc3"
    if request.method == "POST":
        name = request.form.get("fname") 
        password = request.form.get("lname")
        hash_object = hashlib.md5(password.encode())
        passr = hash_object.hexdigest()
        print(passr, hashpass)
        if name == "admin" and passr == hashpass:
            if request.cookies.get('foo'):
                return redirect("http://127.0.0.1:5000/Products/", code=302)
            if not request.cookies.get('foo'):
                res = make_response("Всё правильно, обнови страницу, чтобы продолжить")
                res.set_cookie('foo', 'lolo', max_age=60*60*24*1)
                return res
            else:
                return redirect("http://127.0.0.1:5000/Products/", code=302)
        else:
            return "Ошибка в пароле или логине, попробуй снова"
    else:
        return render_template("login.html")

@app.route('/Products/', methods =["GET", "POST"])
def service():
    if not request.cookies.get('foo'):
        return render_template("login.html")
    else:
        return render_template("Products.html")

@app.route('/form_staf/', methods =["GET", "POST"])
def form_staf():
    return render_template("form.html")

if __name__ == "__main__":
    app.run()