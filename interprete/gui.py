"""
Módulo de interfaz gráfica para el intérprete Gamer.
Incluye área de texto, botones de compilar/ejecutar y consola de resultados.
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
from interprete.interpreter import Interpreter, InterpreterError
from interprete.lexer import Lexer
from interprete.parser import Parser, ParserError
from interprete.keywords import KEYWORDS

EXAMPLE = (
    "crear a = 10\n"
    "crear b = 5\n"
    "curar a b\n"
    "golpear a b\n"
    "multiplicar a b\n"
    "dividir a b\n"
    "poder a b\n"
    "revivir a\n"
    "xp b\n"
    "jefe a b\n"
    "esbirro a b\n"
    "decir a\n"
)

def run_gui() -> None:
    """
    Inicia la interfaz gráfica del intérprete Gamer.
    """
    interpreter = Interpreter()
    lexer = Lexer()
    parser = Parser()

    def show_help():
        msg = (
            "Palabras clave disponibles:\n\n" +
            "\n".join(f"- {kw}" for kw in KEYWORDS) +
            "\n\nEjemplo de uso:\n\n" + EXAMPLE
        )
        messagebox.showinfo("Ayuda - Intérprete Gamer", msg)

    def insert_line(text, color=None):
        console_area.config(state=tk.NORMAL)
        if color:
            console_area.insert(tk.END, text + "\n", color)
        else:
            console_area.insert(tk.END, text + "\n")
        console_area.config(state=tk.DISABLED)

    def compile_only():
        console_area.config(state=tk.NORMAL)
        console_area.delete("1.0", tk.END)
        for idx, line in enumerate(text_area.get("1.0", tk.END).strip().split('\n'), start=1):
            line = line.strip()
            if not line:
                continue
            tokens = lexer.tokenize(line)
            insert_line(f"Línea {idx} - Tokens: {tokens}")
            try:
                parser.parse(tokens)
                insert_line(f"Línea {idx} - Sintaxis: válida")
            except ParserError as pe:
                insert_line(f"Línea {idx} - Error de sintaxis: {pe}", "error")
        console_area.config(state=tk.DISABLED)

    def compile_and_execute():
        console_area.config(state=tk.NORMAL)
        console_area.delete("1.0", tk.END)
        for idx, line in enumerate(text_area.get("1.0", tk.END).strip().split('\n'), start=1):
            line = line.strip()
            if not line:
                continue
            try:
                tokens = lexer.tokenize(line)
                insert_line(f"Línea {idx} - Tokens: {tokens}")
                try:
                    parser.parse(tokens)
                    insert_line(f"Línea {idx} - Sintaxis: válida")
                except ParserError as pe:
                    insert_line(f"Línea {idx} - Error de sintaxis: {pe}", "error")
                    continue
                result = interpreter.eval_instruction(line)
                insert_line(f"Línea {idx} - Compilado correctamente.")
                insert_line(f"Línea {idx} - {result}")
            except InterpreterError as e:
                insert_line(f"Línea {idx} - Error: {e}", "error")
            except Exception as e:
                insert_line(f"Línea {idx} - Error inesperado: {e}", "error")
        console_area.config(state=tk.DISABLED)

    def clear_console():
        console_area.config(state=tk.NORMAL)
        console_area.delete("1.0", tk.END)
        console_area.config(state=tk.DISABLED)

    root = tk.Tk()
    root.title("Intérprete Gamer")
    root.configure(bg="#222831")

    # Área de instrucciones
    instr_frame = tk.LabelFrame(root, text="Área de instrucciones", bg="#393E46", fg="white", font=("Arial", 11, "bold"))
    instr_frame.pack(fill="both", padx=12, pady=8)
    text_area = scrolledtext.ScrolledText(instr_frame, width=60, height=10, font=("Courier New", 11), bg="#EEEEEE")
    text_area.pack(padx=8, pady=8)

    # Botones
    button_frame = tk.Frame(root, bg="#222831")
    button_frame.pack(pady=8)
    compile_btn = tk.Button(button_frame, text="Compilar", command=compile_only, bg="#00ADB5", fg="white", font=("Arial", 10, "bold"), width=15)
    compile_btn.pack(side=tk.LEFT, padx=8)
    run_btn = tk.Button(button_frame, text="Compilar y Ejecutar", command=compile_and_execute, bg="#00FF00", fg="black", font=("Arial", 10, "bold"), width=18)
    run_btn.pack(side=tk.LEFT, padx=8)
    clear_btn = tk.Button(button_frame, text="Limpiar consola", command=clear_console, bg="#393E46", fg="white", font=("Arial", 10, "bold"), width=15)
    clear_btn.pack(side=tk.LEFT, padx=8)
    help_btn = tk.Button(button_frame, text="Ayuda", command=show_help, bg="#222831", fg="#00ADB5", font=("Arial", 10, "bold"), width=10)
    help_btn.pack(side=tk.LEFT, padx=8)

    # Consola de resultados
    console_frame = tk.LabelFrame(root, text="Consola de resultados", bg="#393E46", fg="white", font=("Arial", 11, "bold"))
    console_frame.pack(fill="both", padx=12, pady=8)
    console_area = scrolledtext.ScrolledText(console_frame, width=60, height=15, font=("Courier New", 11), bg="black", fg="lime", state=tk.DISABLED)
    console_area.pack(padx=8, pady=8)
    console_area.tag_config("error", foreground="red", font=("Courier New", 11, "bold"))

    root.mainloop()