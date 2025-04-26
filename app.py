from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Jenkins CI/CD!"

if __name__ == '__main__':
    app.run(host='13.233.113.188', port=5000)

