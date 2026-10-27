from flask import Flask, request, jsonify
from flask_cors import CORS
from detector import rule_based_detect

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    page_text = data.get("text", "")
    page_url  = data.get("url", "")

    if not page_text:
        return jsonify({"error": "No text provided"}), 400

    results = rule_based_detect(page_text, page_url)

    severity_counts = {"high": 0, "medium": 0, "low": 0}
    for r in results:
        severity_counts[r.get("severity", "low")] += 1

    return jsonify({
        "url": page_url,
        "total": len(results),
        "severity_counts": severity_counts,
        "patterns": results,
        "llm_used": False
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)