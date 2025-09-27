"""
Módulo de interfaz gráfica para el intérprete Gamer.
Incluye área de texto, botones de compilar/ejecutar y consola de resultados.
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
from interprete.interpreter import Interpreter, InterpreterError

def run_gui() -> None:
    """
    Inicia la interfaz gráfica del intérprete Gamer.
    """
    interpreter = Interpreter()

    def compile_code():
        code = text_area.get("1.0", tk.END).strip()
        lines = code.split('\n')
        console_area.config(state=tk.NORMAL)
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                result = interpreter.eval_instruction(line)
                console_area.insert(tk.END, f"Compilado correctamente.\n")
                console_area.insert(tk.END, f"{result}\n")
            except InterpreterError as e:
                console_area.insert(tk.END, f"Error: {e}\n")
            except Exception as e:
                console_area.insert(tk.END, f"Error inesperado: {e}\n")
        console_area.config(state=tk.DISABLED)

    def compile_and_run():
        compile_code()
        # Aquí podrías agregar ejecución si tienes instrucciones múltiples

    def clear_console():
        console_area.config(state=tk.NORMAL)
        console_area.delete("1.0", tk.END)
        console_area.config(state=tk.DISABLED)

    root = tk.Tk()
    root.title("Intérprete Gamer")

    tk.Label(root, text="Área de instrucciones:").pack(anchor="w")
    text_area = scrolledtext.ScrolledText(root, width=60, height=10)
    text_area.pack(padx=10, pady=5)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)

    compile_btn = tk.Button(button_frame, text="Compilar", command=compile_code)
    compile_btn.pack(side=tk.LEFT, padx=5)

    run_btn = tk.Button(button_frame, text="Compilar y Ejecutar", command=compile_and_run)
    run_btn.pack(side=tk.LEFT, padx=5)

    clear_btn = tk.Button(button_frame, text="Limpiar consola", command=clear_console)
    clear_btn.pack(side=tk.LEFT, padx=5)

    tk.Label(root, text="Consola de resultados:").pack(anchor="w")
    console_area = scrolledtext.ScrolledText(root, width=60, height=10, state=tk.DISABLED)
    console_area.pack(padx=10, pady=5)

    root.mainloop()