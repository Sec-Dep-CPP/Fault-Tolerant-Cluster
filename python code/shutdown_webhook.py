import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def alert():
    data = request.json
    if data:
        # Log the alert
        with open("/home/raul/shutdown.log", "a") as log_file:
            log_file.write(str(data) + "\n")

        # Shut down the VM
        os.system("sudo shutdown now")
        return "Shutting down VM1 due to high CPU usage", 200
    return "No data received", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
