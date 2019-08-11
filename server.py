from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submitUser():
    nameFromForm = request.form['name']
    locationFromForm = request.form['location']
    languageFromForm = request.form['lang']
    commentFromForm = request.form['comment']
    return render_template("result.html", nameOnTemplate=nameFromForm, locationOnTemplate=locationFromForm, languageFromTemplate=languageFromForm, commentFromTemplate=commentFromForm)


if __name__ == "__main__":
    app.run(debug=True)



