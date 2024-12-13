import os
from flask import Flask, request
app = Flask(__name__)
@app.route('/', methods=['POST'])
def alert():
data = request.json
if data:
# Log incoming alerts for debugging
with open("/home/raul/webhook.log", "a") as log_file:
log_file.write(str(data) + "\n")
# Change directory and execute commands
os.chdir("/home/raul/Portfolio")
os.system("npm run build && nohup npm start &")
return "Alert received and commands executed", 200
return "No data received", 400
if __name__ == '__main__':
app.run(host='0.0.0.0', port=5001)
