#!/usr/bin/env python3
import os, hashlib, json, time, sqlite3
from pathlib import Path

class TaigerCore:
    def __init__(self):
        self.root = os.path.dirname(os.path.dirname(__file__))
        self.vault = Path(self.root) / 'vault'
        self.forensics = Path(self.root) / 'forensics'
        self.vault.mkdir(exist_ok=True)
        self.forensics.mkdir(exist_ok=True)
        self.db = sqlite3.connect(self.vault / 'master_gold.db')
        self._init_db()
        self._load_wallets()

    def _init_db(self):
        self.db.execute('''CREATE TABLE IF NOT EXISTS wallets
            (id INTEGER PRIMARY KEY, address TEXT UNIQUE, private_key TEXT,
             seed TEXT, balance REAL, source TEXT, found_date TIMESTAMP)''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS evidence
            (id INTEGER PRIMARY KEY, hash TEXT UNIQUE, file TEXT,
             findings TEXT, timestamp TIMESTAMP)''')
        self.db.commit()

    def _load_wallets(self):
        wallet_paths = [
            Path.home() / 'wallets',
            Path.home() / '.electrum/wallets',
            Path.home() / 'TAIGER_CORE/vault'
        ]
        for wp in wallet_paths:
            if wp.exists():
                for w in wp.glob('*'):
                    self._ingest_wallet(str(w))

    def _ingest_wallet(self, path):
        h = hashlib.sha256(open(path, 'rb').read()).hexdigest()
        self.db.execute(
            'INSERT OR IGNORE INTO evidence (hash, file, timestamp) VALUES (?, ?, ?)',
            (h, str(path), time.time())
        )
        self.db.commit()

    def log_forensic(self, event_type, details):
        entry = {
            'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S'),
            'type': event_type,
            'details': details,
            'signature': hashlib.md5(str(details).encode()).hexdigest()
        }
        logfile = self.forensics / 'forensics.jsonl'
        with open(logfile, 'a') as f:
            f.write(json.dumps(entry) + '\n')
        return entry['signature']
