from flask import Flask, render_template, request
from new_bike import New_bike
import mlab

mlab.connect()
app = Flask(__name__)

@app.route("/new_bike", methods=['GET', 'POST'])
def new_bike():
    if request.method == 'GET':
        return render_template("new_bike.html")
    elif request.method == 'POST':
        form = request.form
        model = form['model']
        dailyfee = form['dailyfee']
        image = form['image']
        year = form['year']
        nb = New_bike(model=model, dailyfee=dailyfee, image=image, year=year)
        
        model_check = New_bike.objects(model=model).first()
        image_check = New_bike.objects(image=image).first()
        if model_check != None:
            return "Model đã tồn tại!!!"
        elif image_check != None:
            return "Ảnh đã được sử dụng ở model khác!!!"
        else:
            nb.save()
            return "Xin cảm ơn!"

if __name__ == "__main__":
    app.run(debug=True)