from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_interest(principal, yearly_interest, num_of_years):
    total_deposit = principal * (1 + yearly_interest / 100) ** num_of_years
    total_profit = total_deposit - principal
    return total_deposit, total_profit

@app.route('/', methods=['GET', 'POST'])
def compound_interest():
    if request.method == 'POST':
        principal = float(request.form['principal'])
        yearly_interest = float(request.form['yearly_interest'])
        num_of_years = int(request.form['num_of_years'])

        total_deposit, total_profit = calculate_interest(principal, yearly_interest, num_of_years)

        return render_template('result.html', total_deposit=total_deposit, total_profit=total_profit)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)