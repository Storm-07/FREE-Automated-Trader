from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Parse the incoming webhook payload
    payload = request.json

    # Extract the plain_text_body parameter from the payload
    email_body = payload.get('plain_text_body')

    # Determine which Python script to execute based on the email body
    script_path = '[PATH TO BuyActivator.py]/BuyActivator.py' if 'buy' in email_body else '[PATH TO SellActivator]/SellActivator.py'

    # Execute the Python script with the email body as an argument
    subprocess.Popen(['python', script_path, email_body])

    return 'OK'

if __name__ == '__main__':
    app.run()
