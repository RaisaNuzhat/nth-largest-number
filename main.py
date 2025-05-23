from flask import Flask, render_template, request

app = Flask(__name__)

def get_ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        try:
            numbers = request.form['numbers']
            n = int(request.form['n'])

            num_list = [int(x.strip()) for x in numbers.split(',')]
            num_list = list(set(num_list))  # remove duplicates

            if n > len(num_list):
                result = f"There are only {len(num_list)} unique numbers."
            else:
                num_list.sort(reverse=True)
                nth_largest = num_list[n - 1]
                ordinal = get_ordinal(n)
                result = f"The {ordinal} largest number is: {nth_largest}"
        except ValueError:
            result = "Please enter valid input (comma-separated numbers and a valid integer for n)."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)  # Required for Render
