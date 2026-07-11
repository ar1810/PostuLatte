# install.py
import subprocess
import sys

def run_pip(args):
    """Ejecuta un comando pip usando el ejecutable de Python actual."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip"] + args)
    except subprocess.CalledProcessError:
        print(f"❌ Error al ejecutar pip con los argumentos: {args}")
        sys.exit(1)

def main():
    print("=" * 60)
    print("   ☕ ¡Bienvenido al asistente de instalación de PostuLatte!   ")
    print("=" * 60)
    print("¿Qué tipo de entorno deseás configurar para la IA?\n")
    print("  [1] Local (Instala dependencias base + Ollama para Llama 3)")
    print("  [2] Cloud / Base (Instala solo dependencias esenciales)")
    print("-" * 60)
    
    opcion = input("Seleccioná una opción (1 o 2) y presioná Enter: ").strip()
    
    print("\n📦 Instalando dependencias base esenciales (PyYAML y Pydantic)...")
    # Instalamos las dependencias base usando el requirements.txt que ya tenés
    run_pip(["install", "-r", "requirements.txt"])
    
    if opcion == "1":
        print("\n🦙 Instalando soporte para IA Local (Librería de Ollama)...")
        run_pip(["install", "ollama>=0.2.1"])
        print("\n✅ ¡Entorno LOCAL configurado con éxito!")
        print("💡 Recordá tener la aplicación de Ollama corriendo con el modelo 'llama3'.")
    elif opcion == "2":
        print("\n☁️ Configurando entorno BASE/CLOUD.")
        print("✅ ¡Entorno base configurado con éxito! (Preparado para futuras APIs en la nube).")
    else:
        print("\n⚠️ Opción no reconocida. Solo se instalaron las dependencias base.")
    
    print("-" * 60)
    print("🚀 Todo listo. Ya podés ejecutar el sistema con: python -m src.main")
    print("=" * 60)

if __name__ == "__main__":
    main()