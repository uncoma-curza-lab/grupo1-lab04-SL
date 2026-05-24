# Documentación de Infraestructura: Despliegue Local de IA

**Rol:** Integrante 2 - Operador de Infraestructura (SysAdmin)
**Rama de trabajo:** `feature/infra`

---

## 1. Despliegue del Contenedor Base
Para levantar el entorno local, se creó un contenedor persistente utilizando el motor de Podman:

```bash
podman run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama docker.io/ollama/ollama 
```

**Explicación de los parámetros:**
* `-d`: Ejecuta el contenedor en segundo plano para no bloquear la terminal.
* `-v`: Crea un volumen persistente para no perder los datos si se apaga la máquina.
* `-p`: Mapea el puerto del contenedor con el de la máquina virtual.
* `--name`: Le asigna el nombre "ollama" para que sea más fácil de administrar.

## 2. Descarga y Ejecución del Modelo
Con el contenedor base activo, se ejecutó un comando para ingresar al mismo de forma interactiva, descargar y levantar el modelo de lenguaje requerido:

```bash
podman exec -it ollama ollama run qwen2.5:0.5b
```

**Explicación de los parámetros:**
* `exec`: Instrucción para ejecutar un comando dentro de un contenedor que ya está en funcionamiento (en este caso, el contenedor "ollama").
* `-it`: Habilita el modo interactivo con la terminal. Es indispensable para que el contenedor nos devuelva la consola de chat y podamos probar la IA.
* `ollama run qwen2.5:0.5b`: Comando interno del motor que descarga los archivos del modelo desde internet y lo carga en la memoria para su uso.

## 3. Comprobación de la API Local
Para verificar que el servicio se encuentra activo, enrutado correctamente y respondiendo peticiones, se realizó una prueba de conexión local mediante la herramienta `curl`:

```bash
curl http://localhost:11434/
```
**Respuesta del servidor (Output obtenido):**
```text
Ollama is running
```

## 4. Gestión del Contenedor (Operaciones Diarias)
Para la correcta administración del servicio y la optimización de recursos, se documentan los comandos operativos básicos:

**Salir de la consola interactiva de la IA:**
```text
/bye
```

**Detener el contenedor (Apagar el servicio):**
```bash
podman stop ollama
```

**Volver iniciar el contenedor (Apagar el servicio):**
```bash
podman start ollama
```
