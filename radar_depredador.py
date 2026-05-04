#!/usr/bin/env python3
import subprocess, os, json
from pathlib import Path

class RadarDepredador:
    def __init__(self):
        self.electrum_path = Path.home() / '.electrum'
        self.headers = self.electrum_path / 'blockchain_headers'

    def daemon_status(self):
        try:
            r = subprocess.run(['electrum', 'daemon', 'status'],
                               capture_output=True, text=True, timeout=5)
            return json.loads(r.stdout) if r.returncode == 0 else {}
        except:
            return {}

    def start_daemon(self):
        subprocess.run(['electrum', 'daemon', '-d'], stderr=subprocess.DEVNULL)

    def get_block_height(self):
        try:
            r = subprocess.run(['electrum', 'getinfo'],
                               capture_output=True, text=True, timeout=5)
            info = json.loads(r.stdout)
            return info.get('blockchain_height', 0)
        except:
            return 0

    def get_headers_size(self):
        if self.headers.exists():
            return self.headers.stat().st_size
        return 0
