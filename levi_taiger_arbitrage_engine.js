#!/data/data/com.termux/files/usr/bin/node

/**
 * TAIGER ARBITRAGE ENGINE v1
 * Motor de análisis de liquidez y oportunidades de arbitraje
 * HADES CORE COMPATIBLE
 */

const fs = require('fs');
const path = require('path');
const os = require('os');

// Configuración de rutas
const HOME = process.env.HOME || os.homedir();
const VAULT_PATH = path.join(HOME, 'storage', 'shared', 'TAIGER_VAULT');
const INPUT_FILE = path.join(VAULT_PATH, 'liquidity_realtime.jsonl');
const OUTPUT_FILE = path.join(VAULT_PATH, 'arbitrage_opportunities.jsonl');

// Asegurar que el directorio existe
    fs.mkdirSync(VAULT_PATH, { recursive: true });
}

console.log('\x1b[36m[⚡] TAIGER ARBITRAGE ENGINE INITIALIZED\x1b[0m');
console.log(
