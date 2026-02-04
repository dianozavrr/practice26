from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
DATA_FILE = "users.json"

def read_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def write_users(users):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

def get_next_id(users):
    return max([u["id"] for u in users], default=0) + 1

@app.route('/users', methods=['GET','POST'])
def handle_users():
    users = read_users()
    if request.method == 'GET':
        return jsonify({"status":"success","data":users,"message":"Список користувачів"})
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"status":"error","data":None,"message":"Вкажіть name та email"}),400
    user = {"id": get_next_id(users), "name": data['name'], "email": data['email']}
    users.append(user)
    write_users(users)
    return jsonify({"status":"success","data":user,"message":"Користувача створено"}),201

@app.route('/users/<int:user_id>', methods=['GET','PUT','DELETE'])
def handle_user(user_id):
    users = read_users()
    user = next((u for u in users if u["id"]==user_id),None)
    if not user:
        return jsonify({"status":"error","data":None,"message":f"id={user_id} не знайдено"}),404
    if request.method == 'GET':
        return jsonify({"status":"success","data":user,"message":"Користувача отримано"})
    if request.method == 'PUT':
        data = request.json
        user['name']=data.get('name',user['name'])
        user['email']=data.get('email',user['email'])
        write_users(users)
        return jsonify({"status":"success","data":user,"message":"Користувача оновлено"})
    users.remove(user)
    write_users(users)
    return jsonify({"status":"success","data":None,"message":"Користувача видалено"})

if __name__=="__main__":
    app.run(debug=True)
