import socket
import random as r
import time as t
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Character pools for password generation
number = "1234567890"
symbol = "!@#$%^&*()_+-={}[]|\\:;\"\'<>?"
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()

# HTML template
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Password Generator</title>
</head>
<body>
	<h1>Password Generator</h1>
    <form action="/" method="POST">
        <label for="j">Enter number of Passwords you need: </label>
        <input type="number" id="j" name="j" required><br><br>
    
        <label for="pass_len">Enter the password length: </label>
        <input type="number" id="pass_len" name="pass_len" required><br><br>
    
        <input type="submit" value="Generate">
    </form>

    {% if outputs %}
    <h2>Generated Passwords</h2>
    <ul>
        {% for output in outputs %}
            <li>{{ output }}</li>
        {% endfor %}
    </ul>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def main():
    outputs = []
    if request.method == 'POST':
        try:
            j = int(request.form['j'])
            pass_len = int(request.form['pass_len'])
            for _ in range(j):
                password = "".join(r.sample(number + symbol + lower + upper, pass_len))
                outputs.append(password)
                #t.sleep(0.12)
        except ValueError as msg:
            outputs.append(f"Error: {msg}")

    return render_template_string(html_content, outputs=outputs)

if __name__ == '__main__':
    # Dynamically get the system's IP address
    hostname = socket.gethostname()
    system_ip = socket.gethostbyname(hostname)
    print(f"Server running on http://{system_ip}:5000")
    app.run(host=system_ip, port=5000, debug=True)
