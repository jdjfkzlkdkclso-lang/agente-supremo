export async function executeTool(toolName, params) {
  console.log(`[HADES] Ejecutando: ${toolName}`, params);
  return { status: "ok", tool: toolName };
}
