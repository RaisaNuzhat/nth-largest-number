from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            numbers = list(map(int, request.form["numbers"].split(",")))
            n = int(request.form["n"])
            numbers.sort(reverse=True)
            result = f"{n}th largest number is: {numbers[n-1]}"
        except Exception as e:
            result = f"Error: {e}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
