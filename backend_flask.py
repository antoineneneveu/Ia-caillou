from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Autorise les requêtes depuis ton site web

# Remplace par ta clé API OpenAI
openai.api_key = "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"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"reply": "Je suis un caillou, mais même moi j'attends une question..."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Utilise GPT-4o pour de meilleures réponses
            messages=[
                {"role": "system", "content": "Tu es un caillou philosophe, patient et sage. Tes réponses sont profondes mais parfois absurdes."},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Erreur : {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
