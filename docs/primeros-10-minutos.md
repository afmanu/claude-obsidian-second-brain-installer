# Primeros 10 minutos

Usa esta secuencia después de completar la instalación. El objetivo es comprobar que el vault funciona con información real antes de empezar a importar muchas notas.

## Minuto 1: abre el vault correcto

Abre en Obsidian la carpeta final creada por el instalador. Después abre esa misma carpeta en Claude Code:

~~~bash
claude "RUTA_DEL_VAULT"
~~~

No continúes trabajando desde el repositorio del instalador.

## Minutos 2 y 3: revisa el mapa

Abre:

- Home.md;
- 00_START_HERE.md;
- .claude/vault-profile.md.

Comprueba que el perfil, el idioma y las carpetas coinciden con lo que aprobaste.

## Minutos 4 y 5: captura una decisión real

Ejecuta:

~~~text
/second-brain-capture

He decidido [decisión]. La tomé porque [motivo]. Afecta a [proyecto o área].
~~~

Antes de crear la nota, Claude debe mostrar el título, el tipo, la carpeta y las conexiones propuestas.

## Minutos 6 y 7: captura un aprendizaje

Ejecuta de nuevo:

~~~text
/second-brain-capture

Hoy aprendí que [aprendizaje]. Esto puede ser útil para [proyecto, persona o área].
~~~

Abre las dos notas en Obsidian y confirma que aparecen sus enlaces.

## Minuto 8: busca conexiones

Ejecuta:

~~~text
/link-finder
~~~

Revisa las conexiones sugeridas. No aceptes enlaces que no sean realmente útiles.

## Minuto 9: pide próximos pasos

Ejecuta:

~~~text
/next-steps-ai
~~~

Comprueba que las recomendaciones utilizan información existente en el vault y distinguen hechos de inferencias.

## Minuto 10: valida el sistema

La primera sesión está completa si:

- el perfil y el idioma son correctos;
- las cinco habilidades aparecen en .claude/commands;
- Claude propone antes de escribir;
- las notas se guardan en carpetas coherentes;
- los enlaces son útiles;
- y el vault puede reabrirse sin usar el instalador.

Si algo falta, usa el prompt de reparación de [recovery-prompts.md](recovery-prompts.md) en vez de reinstalar desde cero.
