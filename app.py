from flask import Flask, request

app = Flask(__name__)

@app.route('/check_palindrome')
def check_palindrome():
    number = int(request.args.get('num1'))
    temp = number
    rev = 0
    while (number > 0):
        dig = number % 10
        rev = rev * 10 + dig
        number = number // 10
    if (temp == rev):
        return "The number is a palindrome!"
    else:
        return "The number isn't a palindrome!"

if __name__ == '_main_':
    app.run(debug=True)