#!/usr/bin/env python3
import sys
print(f"🔍 Escaneando: {sys.argv[1] if len(sys.argv)>1 else '.'}")
print('{"hallazgo": "seed_phrase_detectada", "tipo": "simulado"}')
