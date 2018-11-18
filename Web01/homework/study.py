from flask import Flask, redirect

app = Flask(__name__)

@app.route("/about-me")
def about_me():
    return "Tên tôi là Bùi Văn Tâm. Năm nay tôi 25 tuổi. Tôi mang giới tính Nam. Cảm ơn đã đọc."


@app.route("/school")
def school():
    return redirect("http://www.techkids.vn")


if __name__ == "__main__":
    app.run(debug=True) 