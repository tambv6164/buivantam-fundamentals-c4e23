from flask import Flask, render_template
 
app = Flask(__name__)

@app.route("/user/<username>")
def infor(username):
    users = {
        "huy": {"Tên": "Nguyễn Quang Huy", "Giới tính": "Nam", "Tuổi": 35},
        "linh": {"Tên": "Lê Thùy Linh", "Giới tính": "Nữ", "Tuổi": 46},
        "huyenanh": {"Tên": "Phùng Huyền Anh", "Giới tính": "Nữ", "Tuổi": 19},
        "nam": {"Tên": "Đỗ Văn Nam", "Giới tính": "Nam", "Tuổi": 25}
    }
    for k in users.keys():
        if username == k:
            return render_template("users.html", k=users[k])
    else:
        return "User not found"


if __name__ == "__main__":
    app.run(debug=True) 