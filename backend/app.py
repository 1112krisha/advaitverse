from flask import Flask, request, jsonify
import os
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'data'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "✅ AdvaitVerse Backend Running"

@app.route("/upload", methods=["POST"])
def upload_data():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(save_path)

    try:
        df = pd.read_csv(save_path)
        return jsonify({
            "message": "File uploaded successfully",
            "rows": len(df),
            "columns": list(df.columns)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
