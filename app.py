from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.append(note)
    return render_template("home.html", notes=notes)

@app.route('/delete/<note>', methods=["GET"])
def delete(note):
    if note in notes:
        notes.remove(note)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
