from flask import Flask, redirect, url_for, render_template, request, session, abort, flash
import json

with open('db/products.json', 'r+') as p:
    data_p = json.load(p)
    products = data_p["products"]

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')
app.secret_key = "PASSWORD"


@app.route('/', methods=['GET', 'POST'])
def home():
    return redirect(url_for("login"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session:
        return redirect(url_for("shop"))
    if request.method == "POST":
        try:
            session.clear()
            username = request.form["username"]
            session["username"] = username
            password = request.form["password"]
            session["password"] = password
            if username == '' or password == '': 
                flash("Enter all the required fields!")
                return render_template("login.html")
            with open('db/users.json', 'r+') as u:
                data_u = json.load(u)
                users = data_u["users"]
                for user in users:
                    if user["username"] == session["username"] and user["password"] == session["password"]:
                        return redirect(url_for("shop"))
                u.close()
            flash("Invalid Credentials")
            return render_template("login.html")
        finally:
            pass
    else:
        return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if session:
        return redirect(url_for("shop"))
    if request.method == "POST":
        try:
            session.clear()
            username = request.form["username"]
            session["username"] = username
            password = request.form["password"]
            session["password"] = password
            password_conf = request.form["password-conf"]
            if password != password_conf:
                flash("Enter the same password!")
                return render_template("register.html")
            if username == '' or password == '' or password_conf == '': 
                flash("Enter all the required fields!")
                return render_template("register.html")
            with open('db/users.json') as u_read:
                data_u = json.load(u_read)
                users = data_u["users"]
                for user in users:
                    if user["username"] == session["username"]:
                        flash("User already exists!")
                        return render_template("register.html")
                new_user = {"username": session["username"],
                            "password": session["password"],
                            "cart": []
                            }
                users.append(new_user)
            with open('db/users.json', 'w') as u_write:
                json.dump(data_u, u_write, indent=4)
                u_write.close()
                u_read.close()
            return redirect(url_for("login"))
        finally:
            pass
    else:
        return render_template("register.html")


@app.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route('/shop', methods=['GET', 'POST'])
def shop():
    if not session:
        return redirect(url_for("login"))
    try:
        item = request.args.get('addtocart')
        if item:
            with open('db/users.json') as u_read:
                data_u = json.load(u_read)
                users = data_u["users"]
                for user in users:
                    if user["username"] == session["username"]:
                        if not user["cart"]:
                            user["cart"] = []
                        user["cart"].append(item)
                        break
            with open('db/users.json', 'w') as u_write:
                json.dump(data_u, u_write, indent=4)
                u_write.close()
                u_read.close()
    finally:
        return render_template("shop.html", products=products)


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if not session:
        return redirect(url_for("login"))
    try:
        rem = request.args.get('delfromcart')
        if rem:
            with open('db/users.json') as u_read:
                data_u = json.load(u_read)
                users = data_u["users"]
                for user in users:
                    if user["username"] == session["username"]:
                        if not user["cart"]:
                            user["cart"] = []
                        if rem in user["cart"]:
                            user["cart"].remove(rem)
                        break
            with open('db/users.json', 'w') as u_write:
                json.dump(data_u, u_write, indent=4)
                u_write.close()
                u_read.close()
    finally:
        pass
    with open('db/users.json') as u_read:
        data_u = json.load(u_read)
        users = data_u["users"]
        for user in users:
            if user["username"] == session["username"]:
                if not user["cart"]:
                    cart = []
                else:
                    cart = user["cart"]
        u_read.close()
    cart_items = []
    total = 0
    for item in cart:
        for product in products:
            if item == product["name"]:
                cart_items.append(product)
                total += float(product["price"][1:])
    return render_template("cart.html", cart=cart_items, total=total)

if __name__ == "__main__":
    app.run(host="localhost", port=5050)
