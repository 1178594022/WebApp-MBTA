from flask import Flask, render_template, request

from mbta_finder import find_stop_near


app = Flask(__name__)




@app.route("/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        a = str(request.form["a"])
        roots = find_stop_near(a)

        if roots:
            return render_template(
                "stop_result.html",
                a=a,
                root_1=roots[0],
                root_2=roots[1],
            )
        else:
            return render_template("stop_form.html", error=True)
    return render_template("stop_form.html", error=None)




if __name__ == "__main__":
    app.run(debug=True)