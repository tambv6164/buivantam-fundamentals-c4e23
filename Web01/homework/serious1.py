from flask import Flask, render_template
 
app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    height_m = height/100
    BMI = weight/(height_m**2)
    if BMI < 16:
        return "BMI = " + str(BMI) + " SEVERELY UNDERWEIGHT"
    elif BMI < 18.5:
        return "BMI = " + str(BMI) + " UNDERWEIGHT"
    elif BMI < 25:
        return "BMI = " + str(BMI) + " NORMAL"
    elif BMI < 30:
        return "BMI = " + str(BMI) + " OVERWEIGHT"
    else:
        return "BMI = " + str(BMI) + " OBESE"


@app.route("/bmi2/<int:weight>/<int:height>")
def bmi2(weight, height):
    height_m = height/100
    BMI = weight/(height_m**2)
    return render_template("bmi.html", BMI=BMI)


if __name__ == "__main__":
    app.run(debug=True) 