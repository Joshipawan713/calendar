from flask import Flask, render_template, request
import calendar
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    year = now.year
    month = now.month

    if request.args.get('year'):
        year = int(request.args.get('year'))
    if request.args.get('month'):
        month = int(request.args.get('month'))

    cal = calendar.monthcalendar(year, month)
    
    return render_template('index.html', calendar=cal, year=year, month=month)

if __name__ == "__main__":
    app.run(debug=True)