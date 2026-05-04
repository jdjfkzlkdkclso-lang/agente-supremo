#!/usr/bin/env python3
from flask import Flask, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/scan/<path:repo>')
def scan_repo(repo):
    """Escanea un repositorio en busca de vulnerabilidades"""
    result = subprocess.run(
        ['python', '~/TAIGER_CORE/modules/jalisco_letal.py', repo],
        capture_output=True, text=True
    )
    return jsonify({
        "repo": repo,
        "vulnerabilidades": result.stdout,
        "status": "completado"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
