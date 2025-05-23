from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    error = None

    if request.method == 'POST':
        numbers = request.form['numbers']
        n = request.form['n']

        try:
            number_list = list(map(int, numbers.split(',')))
            n = int(n)
            if n > len(number_list) or n < 1:
                error = "Invalid value of n."
            else:
                number_list.sort(reverse=True)
                result = number_list[n - 1]
        except:
            error = "Please enter valid integers separated by commas and a valid n."

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
