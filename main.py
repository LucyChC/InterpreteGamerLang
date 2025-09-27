"""
Punto de entrada.
Ejecuta la interfaz gráfica y gestiona errores globales.
"""

from interprete.gui import run_gui  

def main() -> None:
    """
    Función principal que inicia la interfaz gráfica del intérprete.
    Maneja errores globales y muestra mensajes claros.
    """
    try:
        run_gui()
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()