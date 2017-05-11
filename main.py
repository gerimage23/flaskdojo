from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


COUNTS = 0


@app.route("/")
def root():
    global COUNTS
    return render_template('root.html', counts=COUNTS)


@app.route("/request-counter", methods=["POST", "GET"])
def request_counter():
    global COUNTS
    if request.method == "POST":
        COUNTS += 1
        return redirect(url_for('root'))
    COUNTS += 1
    return redirect(url_for('root'))


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
