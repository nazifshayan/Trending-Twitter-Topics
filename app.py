from flask import Flask, render_template
import threading
import main

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/run_script')
def run_script():
    threading.Thread(target=main.main_script()).start()
    return {"status": "Script is running"}


if __name__ == "__main__":
    app.run(debug=True)