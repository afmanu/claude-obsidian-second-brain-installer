# Guía rápida en español

Esta guía te permite probar Claude Obsidian Second Brain sin tener que entender la arquitectura del repositorio.

## Qué vas a obtener

Claude te hará tres preguntas, propondrá una estructura adaptada a tu trabajo o vida personal y creará un vault de Obsidian con:

- una página de inicio;
- una guía de uso;
- carpetas personalizadas;
- reglas para guardar y conectar notas;
- cinco habilidades para capturar, conectar, sintetizar y decidir próximos pasos.

Tus notas se guardan como archivos locales de Markdown. El instalador no necesita una base de datos.

## Qué necesitas

Para la instalación completa:

- un ordenador;
- Obsidian;
- Claude Code o Claude Co-Work con acceso a carpetas locales;
- conexión a Internet durante la preparación;
- permiso para crear una carpeta para el vault.

Claude Code es actualmente el modo más fiable. Desde móvil puedes iniciar la tarea, pero la creación del vault debe continuar en el ordenador.

## Instalación recomendada

Abre Claude Code o Claude Co-Work Desktop y envía únicamente:

~~~text
Quiero instalar este sistema de segundo cerebro:

https://github.com/afmanu/claude-obsidian-second-brain-installer
~~~

No necesitas mencionar BOOTSTRAP.md, MCP, permisos ni pasos internos. El repositorio contiene esas instrucciones.

Claude debe comenzar automáticamente con una comprobación de solo lectura. Después solo debería preguntarte por decisiones que no puede tomar por ti:

- dónde crear el vault;
- qué quieres organizar;
- qué idioma prefieres;
- y si apruebas una operación que modificará el equipo.

Si Claude se limita a resumir el repositorio, la detección de intención ha fallado. Usa entonces el prompt de recuperación de docs/recovery-prompts.md.

## Alternativa desde terminal

Si Claude no puede acceder al repositorio automáticamente:

~~~bash
git clone https://github.com/afmanu/claude-obsidian-second-brain-installer.git
cd claude-obsidian-second-brain-installer
claude .
~~~

Después di:

~~~text
Lee BOOTSTRAP.md e inicia la instalación guiada. No resumas el repositorio.
~~~

## Resultado esperado

Al terminar tendrás una carpeta independiente que podrás abrir directamente en Obsidian y Claude Code. El instalador verificará como mínimo:

- CLAUDE.md;
- Home.md;
- 00_START_HERE.md;
- el perfil del vault;
- las cinco habilidades principales;
- la documentación operativa;
- y las carpetas elegidas.

## Primera prueba

Abre el vault final en Claude Code:

~~~bash
claude "RUTA_DEL_VAULT"
~~~

Después ejecuta la primera captura:

~~~text
/second-brain-capture

He decidido reservar dos horas cada viernes para revisar mis proyectos y preparar la semana siguiente.
~~~

Continúa con [Primeros 10 minutos](docs/primeros-10-minutos.md).

## Si algo falla

Pega este mensaje dentro del repositorio del instalador:

~~~text
Revisa TROUBLESHOOTING.md, specs/setup-state-machine.md y specs/vault-output-contract.md. Identifica el último paso completado y continúa desde ahí sin empezar de cero ni sobrescribir archivos existentes.
~~~

También puedes consultar [TROUBLESHOOTING.md](TROUBLESHOOTING.md) y [los prompts de recuperación](docs/recovery-prompts.md).

## Límites actuales

- No es un plugin de Obsidian ni una aplicación de instalación con un botón.
- La instalación local completa no se ejecuta únicamente desde móvil.
- La configuración MCP puede requerir reiniciar o refrescar Claude.
- Windows con WSL puede necesitar ajustar rutas.
- El sistema no publica, sincroniza ni sube tus notas automáticamente.
