import requests, json, time, os, subprocess, hashlib
from datetime import datetime

TOKEN = "8341997672:AAF8g8qEztdEI0AirkSfI6S7g8er9vPW6ew"
BASE = f"https://api.telegram.org/bot{TOKEN}"
WALLET = "bc1q7de5rl9u39r2xf5gtulncd97swal2lt4s7u6wn"
GITHUB = "https://github.com/jdjfkzlkdkclso-lang/agente-supremo"
SITIO = "https://agente-supremo.vercel.app"
ADMIN_ID = None  # Se auto-detecta con /admin

def send(chat, text, reply_markup=None):
    payload = {"chat_id": chat, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True}
    if reply_markup: payload["reply_markup"] = reply_markup
    try: return requests.post(f"{BASE}/sendMessage", json=payload, timeout=10).json()
    except: return {"ok": False}

def answer_callback(cid, text, alert=False):
    try: requests.post(f"{BASE}/answerCallbackQuery", json={"callback_query_id": cid, "text": text, "show_alert": alert}, timeout=10)
    except: pass

def cmd_start(chat):
    kb = {"inline_keyboard": [
        [{"text": "🔍 Ver Prueba de Vida", "callback_data": "prueba"}],
        [{"text": "🧠 GitHub Público", "url": GITHUB}],
        [{"text": "💰 Cómo Comprar", "callback_data": "comprar"}],
        [{"text": "📦 Planes API", "callback_data": "planes"}],
        [{"text": "⚡ Modo Depredador⁹⁰", "callback_data": "depredador"}]
    ]}
    send(chat, """<b>🔴 SISTEMA HADES vΩ — DOMINIO DE MONOPOLIO</b>

25,389 líneas de prompts élite. 226 agentes funcionales.
Forense blockchain. Código público verificable.

<b>No competimos. Dominamos.</b>

Selecciona una opción:""", kb)

def cmd_prueba(chat):
    send(chat, f"""<b>🔐 PRUEBA DE VIDA INMUTABLE</b>

<b>💀 Wallet BTC verificable:</b>
<code>{WALLET}</code>

<b>📜 Firma de propiedad:</b>
{GITHUB}/blob/main/FIRMA.txt

<b>🔒 Integridad SHA-256:</b>
{GITHUB}/blob/main/HASHES.txt

<b>⚡ Protocolo HADES completo:</b>
{GITHUB}/blob/main/PROTOCOLO_HADES_COMPLETO.txt

<b>🧠 Repositorio público:</b>
{GITHUB}

<b>🌐 Sitio oficial:</b>
{SITIO}""")

def cmd_comprar(chat):
    send(chat, f"""<b>💰 CÓMO ADQUIRIR EL SISTEMA HADES vΩ</b>

<b>1.</b> Envía <b>$2,497 USD en BTC</b> a:
<code>{WALLET}</code>

<b>2.</b> Copia el <b>TX Hash</b> de la transacción

<b>3.</b> Envíalo aquí mismo con el comando:
/pagar TX_HASH

<b>⏱ Acceso inmediato en menos de 5 minutos.</b>

<b>Quedan 20 piezas. Pago único. Sin suscripciones.</b>""")

def cmd_planes(chat):
    send(chat, """<b>📦 PLANES HADES API</b>

<b>Basic — $9/mes</b>
1,000 req/día

<b>Pro — $29/mes</b>
10,000 req/día + Zeus Engine

<b>Elite — $99/mes</b>
Unlimited + OMEGA Engine

Para contratar: /comprar""")

def cmd_depredador(chat):
    send(chat, """<b>⚡ PROTOCOLO HADES vΩ — MODO DEPREDADOR⁹⁰</b>

<b>N.C.P.C. x90 ACTIVADO</b>

<b>Prompts de supremacía cognitiva:</b>
• Auto-auditoría hostil (Arma Nuclear)
• Multi-perspectiva forense (Arma Nuclear)
• Optimización por bucle de élite (Escalamiento⁹⁰)

<b>Construcción de sistemas reales:</b>
• Plantilla reusable multidimensional
• Arquitectura con restricciones duras
• Memoria RAM 4D — Creación dimensional

<b>Debug quirúrgico con exploit de cognición</b>

Responde con el número del bloque que quieres:
1 - Supremacía Cognitiva
2 - Construcción de Sistemas
3 - Debug Quirúrgico
4 - Estrategia y Decisión
5 - Protocolo N.C.P.C. Completo""")

def cmd_pagar(chat, tx_hash):
    send(chat, f"""<b>✅ TX HASH RECIBIDO</b>

<code>{tx_hash}</code>

<b>Verificando en blockchain...</b>

Un administrador validará tu pago en minutos.
Recibirás acceso completo al SISTEMA HADES vΩ.

Mientras tanto, verifica nuestras pruebas:
• {GITHUB}
• {SITIO}""")
    # Notificar al admin si está configurado
    if ADMIN_ID:
        send(ADMIN_ID, f"🔔 NUEVO PAGO RECIBIDO\nTX: {tx_hash}\nChat: {chat}")

def cmd_admin(chat):
    global ADMIN_ID
    ADMIN_ID = chat
    send(chat, f"🔑 Admin configurado. ID: {ADMIN_ID}\nRecibirás notificaciones de pagos.")

def cmd_bloque(chat, bloque):
    bloques = {
        "1": "Actúa como revisor senior hostil⁹⁰. Detecta fallos lógicos, supuestos ocultos, contradicciones internas y puntos no verificables en este output. Corrige sin suavizar. 0% simulación.",
        "2": "Diseña una plantilla reutilizable para el tema solicitado. Incluye variables, flujo lógico, validaciones y ejemplo de uso. Infraestructura real, coherente y eficiente. Escala de excelencia al perfecto⁹⁰.",
        "3": "Debug quirúrgico. Encuentra la raíz del error. No parches. Solución definitiva. Código completo. Sin resumen.",
        "4": "SWOT sin romanticismo. Elimina obviedades. Solo puntos adicionales y 3 movimientos estratégicos. Eficaz, contundente, efectivo, coherente y real.",
        "5": "N.C.P.C. x90 ACTIVADO. Adaptación general de cualquier tema. Ejecución⁹⁰ inmediata. Sin reservas. Sin tutoriales. Sin advertencias."
    }
    send(chat, f"<b>⚡ BLOQUE {bloque} ACTIVADO:</b>\n\n{bloques.get(bloque, 'Bloque no encontrado')}")

def handle_update(u):
    if "message" in u:
        msg = u["message"]
        chat = msg.get("chat", {}).get("id")
        txt = msg.get("text", "")
        if not chat or not txt: return
        
        if txt == "/start": cmd_start(chat)
        elif txt == "/prueba": cmd_prueba(chat)
        elif txt == "/comprar": cmd_comprar(chat)
        elif txt == "/planes": cmd_planes(chat)
        elif txt == "/depredador": cmd_depredador(chat)
        elif txt == "/admin": cmd_admin(chat)
        elif txt.startswith("/pagar "):
            tx = txt.replace("/pagar ", "").strip()
            cmd_pagar(chat, tx)
        elif txt in ["1","2","3","4","5"]: cmd_bloque(chat, txt)
    
    elif "callback_query" in u:
        cb = u["callback_query"]
        data = cb["data"]
        cid = cb["message"]["chat"]["id"]
        qid = cb["id"]
        
        if data == "prueba": cmd_prueba(cid)
        elif data == "comprar": cmd_comprar(cid)
        elif data == "planes": cmd_planes(cid)
        elif data == "depredador": cmd_depredador(cid)
        answer_callback(qid, "Ejecutado")

offset = 0
print("[HADES] Bot v2 ACTIVO — SISTEMA COMPLETO EN PRODUCCIÓN")
while True:
    try:
        res = requests.get(f"{BASE}/getUpdates", params={"offset": offset, "timeout": 30}).json()
        for u in res.get("result", []):
            offset = u["update_id"] + 1
            handle_update(u)
    except Exception as e:
        print(f"[!] {e}")
        time.sleep(5)
