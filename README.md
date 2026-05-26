# Laboratorio 4: IA Soberana y Vibe Coding

Este repositorio contiene el desarrollo del Laboratorio 4 sobre Inteligencia Artificial Soberana. El objetivo central del proyecto es demostrar la viabilidad de ejecutar modelos de lenguaje (LLMs) de forma 100% local, garantizando la privacidad de los datos y aplicando metodologías de **Vibe Coding** (programación asistida por IA) para la automatización de tareas.

## Descripción del Proyecto
El sistema implementado consiste en un script de Python que se comunica con una API de un servidor local de Ollama, el cual fue desplegado mediante contenedores. El script lee el texto completo de la Licencia GNU GPLv3 localmente y le instruye al modelo de lenguaje que genere un resumen estricto de exactamente tres líneas. Todo el procesamiento de la información se realiza dentro de la red local.

## Tecnologías y Herramientas
* **Infraestructura:** Podman, Ollama.
* **Modelo de Lenguaje:** `qwen2.5:0.5b` (optimizado para CPU y entornos de bajos recursos).
* **Desarrollo:** Python 3 (librerías nativas `urllib` y `json`), Visual Studio Code.
* **Control de Versiones:** Git y ramas paralelas integradas mediante Pull Requests.

## Equipo de Trabajo

* **Integrante 1: Leonela Jara (Maintainer)**
  * **Rol:** Gestión del repositorio central, revisión de Pull Requests, resolución de conflictos y ensamblado del Informe Final.
  * **Rama:** `main`

* **Integrante 2: Pablo Torres (SysAdmin)**
  * **Rol:** Despliegue de la infraestructura local, aprovisionamiento del contenedor de Ollama y descarga del modelo de lenguaje.
  * **Rama:** `feature/infra`

* **Integrante 3: Ayelen Jara (Vibe Coder)**
  * **Rol:** Desarrollo de la lógica del cliente mediante inteligencia artificial (Vibe Coding).
  * **Rama:** `feature/scripting`
