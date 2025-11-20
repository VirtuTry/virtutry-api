from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "message": "VirtuTry API v1 ativa"
    })

@app.route("/process", methods=["POST"])
def process_image():
    if "image" not in request.files:
        return jsonify({"error": "Nenhuma imagem enviada"}), 400

    image = request.files["image"]

    # Por enquanto só retornamos o nome — depois entraremos com a IA real
    return jsonify({
        "status": "success",
        "filename": image.filename,
        "message": "Imagem recebida com sucesso (IA ainda não aplicada)"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
