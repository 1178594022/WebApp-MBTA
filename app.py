from flask import Flask, render_template, request

from mbta_finder import find_stop_near


app = Flask(__name__)



"""Define a route of the webside to the default route"""
@app.route("/", methods=["GET", "POST"])
#define the function calculate to find the tupple of the closest station information
def calculate():
    if request.method == "POST":    #use the request method post
        a = str(request.form["a"])  #set veriable a as the input from the user
        roots = find_stop_near(a)   #set root as the veriable records result returned from find_stop_near 

        if roots:
            return render_template(
                "stop_result.html", #use the templet of HTML code in the templet folder named stop_form
                a=a,
                root_1=roots[0],   # root_1 record the station name
                root_2=roots[1],    # root_2 record the accessability
            )
        else:
            return render_template("stop_form.html", error=True) 
    return render_template("stop_form.html", error=None) # the result returns by the format of stop_form.html


if __name__ == "__main__":
    app.run(debug=True)