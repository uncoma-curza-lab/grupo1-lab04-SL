#!/usr/bin/env python3
import argparse
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

# Modelo exacto a usar en Ollama
MODEL = "qwen2.5:0.5b"

OLLAMA_URL = "http://192.168.1.29:11434/api/generate"


def read_input_file(path: Path) -> str:
	if path.exists():
		return path.read_text(encoding="utf-8")
	# Try current working directory fallback
	cwd_path = Path.cwd() / path.name
	if cwd_path.exists():
		return cwd_path.read_text(encoding="utf-8")
	raise FileNotFoundError(f"No se encontró el archivo: {path}")


def call_ollama(model: str, prompt: str, timeout: int = 600) -> str:
	payload = {"model": model, "prompt": prompt, "stream": False}
	data = json.dumps(payload).encode("utf-8")
	req = urllib.request.Request(OLLAMA_URL, data=data, headers={"Content-Type": "application/json"})
	try:
		with urllib.request.urlopen(req, timeout=timeout) as resp:
			raw = resp.read().decode("utf-8")
	except urllib.error.URLError as e:
		raise RuntimeError(f"Error al conectar con Ollama: {e}")

	# Parsear JSON
	try:
		j = json.loads(raw)
	except Exception:
		return raw.strip()

	if isinstance(j, dict):
		if "response" in j and isinstance(j["response"], str):
			return j["response"].strip()

		if "results" in j and isinstance(j["results"], list) and j["results"]:
			first = j["results"][0]
			if isinstance(first, dict):
				content = first.get("content")
				if isinstance(content, dict) and "text" in content and isinstance(content["text"], str):
					return content["text"].strip()
				if isinstance(content, str):
					return content.strip()
				if isinstance(content, list):
					texts = [item["text"].strip() for item in content if isinstance(item, dict) and item.get("type") == "output_text" and isinstance(item.get("text"), str)]
					if texts:
						return "\n".join(texts).strip()

	# Fallback: stringify JSON si no existe "response"
	return json.dumps(j, ensure_ascii=False)


def main():
	parser = argparse.ArgumentParser(description="Enviar archivo a Ollama para resumen de 3 líneas.")
	parser.add_argument("-f", "--file", default="archivo_prueba.txt", help="Ruta al archivo de texto to leer")
	parser.add_argument("-m", "--model", default=MODEL, help="Modelo Ollama (por defecto: qwen2.5:0.5b)")
	args = parser.parse_args()

	file_path = Path(args.file)
	try:
		content = read_input_file(file_path)
	except FileNotFoundError as e:
		print(e, file=sys.stderr)
		sys.exit(2)

	prompt = f"{content}\n\nEscribe un breve resumen del texto anterior de un (1) solo párrafo en ESPAÑOL. Máximo 3 oraciones en total. No uses viñetas, listas, introducciones ni conclusiones"

	try:
		result = call_ollama(args.model, prompt)
	except Exception as e:
		print(f"Error: {e}", file=sys.stderr)
		sys.exit(1)

	sentences = [s.strip() for s in result.split('.') if s.strip()]
	trimmed = '. '.join(sentences[:3]).strip()
	if trimmed and not trimmed.endswith('.'):
		trimmed += '.'

	print(trimmed)


if __name__ == "__main__":
	main()
