from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return render_template('index1.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)