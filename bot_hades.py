import requests
import json
import time

TOKEN = "8341997672:AAF8g8qEztdEI0AirkSfI6S7g8er9vPW6ew"
BASE = f"https://api.telegram.org/bot{TOKEN}"

def send(chat, text, reply_markup=None):
    return requests.post(f"{BASE}/sendMessage", json={
        "chat_id": chat, "text": text, "reply_markup": reply_markup,
        "parse_mode": "HTML", "disable_web_page_preview": False
    }).json()

def handle_update(u):
    msg = u.get("message", {})
    chat = msg.get("chat", {}).get("id")
    txt = msg.get("text", "")
    if not chat: return
    
    if txt == "/start":
        kb = {"inline_keyboard": [
            [{"text": "🔍 Ver Prueba de Vida", "callback_data": "prueba"}],
            [{"text": "🧠 Ir a Github", "url": "https://github.com/jdjfkzlkdkclso-lang/agente-supremo"}],
            [{"text": "💰 Cómo Comprar", "callback_data": "comprar"}]
        ]}
        send(chat, "<b>AGENTE SUPREMO vΩ</b>\nVerifica tú mismo. Sin letras pequeñas.", kb)
    
    elif txt == "/prueba":
        send(chat, """<b>🔐 PRUEBA DE VIDA</b>

<b>Wallet verificada:</b> <code>bc1q7de5rl9u39r2xf5gtulncd97swal2lt4s7u6wn</code>

<b>Firma de propiedad:</b> <a href='https://github.com/jdjfkzlkdkclso-lang/agente-supremo/blob/main/FIRMA.txt'>FIRMA.txt</a>

<b>Integridad SHA-256:</b> <a href='https://github.com/jdjfkzlkdkclso-lang/agente-supremo/blob/main/HASHES.txt'>HASHES.txt</a>

<b>Repositorio completo:</b> <a href='https://github.com/jdjfkzlkdkclso-lang/agente-supremo'>github.com/jdjfkzlkdkclso-lang/agente-supremo</a>""")
    
    elif txt == "/comprar":
        send(chat, """<b>💰 CÓMO COMPRAR</b>

1. Envía <b>$2,497 USD en BTC</b> a:
<code>bc1q7de5rl9u39r2xf5gtulncd97swal2lt4s7u6wn</code>

2. Copia el <b>TX Hash</b>

3. Envíalo aquí

⏱ Acceso en menos de 5 minutos.""")
    
    elif txt == "/plan":
        send(chat, """<b>📦 PLANES HADES API</b>

<b>Basic — $9/mes</b> | 1,000 req/día
<b>Pro — $29/mes</b> | 10,000 req/día + Zeus
<b>Elite — $99/mes</b> | Unlimited + OMEGA""")
    
    elif "callback_query" in u:
        data = u["callback_query"]["data"]
        cid = u["callback_query"]["message"]["chat"]["id"]
        if data == "prueba":
            send(cid, """<b>🔐 PRUEBA DE VIDA</b>
<b>Wallet:</b> <code>bc1q7de5rl9u39r2xf5gtulncd97swal2lt4s7u6wn</code>
<b>Firma:</b> <a href='https://github.com/jdjfkzlkdkclso-lang/agente-supremo/blob/main/FIRMA.txt'>FIRMA.txt</a>
<b>Hashes:</b> <a href='https://github.com/jdjfkzlkdkclso-lang/agente-supremo/blob/main/HASHES.txt'>HASHES.txt</a>""")
        elif data == "comprar":
            send(cid, """<b>💰 CÓMO COMPRAR</b>
1. Envía <b>$2,497 USD en BTC</b> a <code>bc1q7de5rl9u39r2xf5gtulncd97swal2lt4s7u6wn</code>
2. Copia el <b>TX Hash</b> y envíalo aquí""")

offset = 0
print("[HADES] Bot activo. Ctrl+C para detener.")
while True:
    try:
        res = requests.get(f"{BASE}/getUpdates", params={"offset": offset, "timeout": 30}).json()
        for u in res.get("result", []):
            offset = u["update_id"] + 1
            handle_update(u)
    except Exception as e:
        print(f"[!] {e}")
        time.sleep(5)
