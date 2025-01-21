from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Eingehende JSON-Daten (z. B. SMS-Inhalt)
    data = request.get_json()
    print(f"Eingehende SMS: {data}")
    return "SMS erhalten", 200

if __name__ == '__main__':
    app.run(port=5000)
