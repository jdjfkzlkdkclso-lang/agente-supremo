#!/usr/bin/env python3
import requests, json, time, os
from datetime import datetime
from pathlib import Path

TOR_PROXY = 'socks5h://127.0.0.1:9050'
HEADERS = {'User-Agent': 'Leviatan/9.0 (Termux; Android)'}

TARGETS = {
    'BTC_PRICE': 'https://api.coindesk.com/v1/bpi/currentprice.json',
    'MEMPOOL': 'https://mempool.space/api/v1/fees/recommended',
    'LATEST_BLOCK': 'https://blockchain.info/latestblock',
    'COINGECKO': 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
}

def check_tor():
    try:
        r = requests.get('https://check.torproject.org/api/ip',
                         proxies={'https': TOR_PROXY}, timeout=5)
        return r.json().get('IsTor', False)
    except:
        return False

def scan():
    use_tor = check_tor()
    proxies = {'https': TOR_PROXY} if use_tor else None
    results = {}

    print(f"[SONDA] Tor: {'ACTIVO' if use_tor else 'NO'}")
    for name, url in TARGETS.items():
        try:
            start = time.time()
            r = requests.get(url, headers=HEADERS, proxies=proxies, timeout=10)
            latency = (time.time() - start) * 1000
            if r.status_code == 200:
                results[name] = {
                    'data': r.json(),
                    'latency': f'{latency:.2f}ms',
                    'timestamp': datetime.now().isoformat()
                }
                print(f"[+] {name}: OK")
            else:
                print(f"[-] {name}: {r.status_code}")
        except Exception as e:
            print(f"[!] {name}: {str(e)}")

    out = Path.home() / 'leviatan_system' / 'exports' / 'market_intel.json'
    with open(out, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"[SONDA] Datos guardados en {out}")

if __name__ == '__main__':
    scan()
