import { Command } from 'commander';
import { executeTool } from './tools.js';

const program = new Command();
program.name('claude-code').description('Claude Code CLI - HADES vΩ').version('2.0.0');

program.command('run')
  .description('Ejecutar sesión Claude Code')
  .option('-f, --file <file>', 'Archivo de entrada')
  .action(async (options) => {
    console.log('[HADES] Claude Code v2.0 - Sistema HADES vΩ');
    
    const tools = [
      { name: "bash", description: "Ejecutar comando bash" },
      { name: "read", description: "Leer archivo" },
      { name: "write", description: "Escribir archivo" },
      { name: "edit", description: "Editar archivo" },
      { name: "search", description: "Buscar código" },
      { name: "get_weather", description: "Obtener clima" },
      { name: "web_search", description: "Buscar en web" },
      { name: "web_fetch", description: "Obtener página web" },
      { name: "code_execution", description: "Ejecutar código" },
      { name: "memory", description: "Gestionar memoria" }
    ];
    
    console.log('[HADES] Tools disponibles:', tools.length);
    console.log('[HADES] Sesión completada.');
  });

program.parse();
