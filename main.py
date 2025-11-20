from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({
        "status": "ok",
        "service": "VirtuTry API",
        "version": "v1",
        "message": "Bem-vindo à API da VirtuTry 👗✨"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/try-on", methods=["POST"])
def try_on():
    """
    Endpoint de teste por enquanto.
    No futuro: receber imagem, roupa, etc.
    """
    data = request.json or {}
    return jsonify({
        "status": "ok",
        "message": "Endpoint /try-on funcionando. Modelo de IA vem na próxima etapa 😉",
        "received": data
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
