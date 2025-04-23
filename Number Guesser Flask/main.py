from flask import Flask

app = Flask(__name__)

def makebold(func):
    def wrap ():
        return f"<b>{func()}</b>"
    return wrap

@app.route("/bye")
@makebold
def yasin():
    return "bye"

@app.route("/")
def show_number ():
    return ("<h1 style='text-align:center'>Hello Yasin</h2>"
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGEwdHFqc2Nnb201cGsxYmxlMTdiYjMwd3Jqa2tzMWRjN2gyejc2MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/a1AjSMw4glOi8Ow2yy/giphy.gif'  style='display:block; margin:auto'  alt='america_image'/>")

@app.route("/username/<path:name>/<int:age>")
def greet (name,age):
    return f"Hello {name } , Your age is {age}"

if __name__ == "__main__":
    app.run(debug=True)