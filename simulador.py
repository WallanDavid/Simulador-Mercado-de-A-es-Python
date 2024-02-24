import tkinter as tk
from tkinter import ttk, messagebox
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SimulacaoMercadoAcoes:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulação de Mercado de Ações")

        self.valor_inicial = 100  # Valor inicial de cada ação
        self.dias_simulacao = tk.IntVar(value=30)
        self.preco_acao = [self.valor_inicial]

        self.criar_interface()

    def criar_interface(self):
        self.frame_controles = ttk.Frame(self.root, padding="10")
        self.frame_controles.pack()

        ttk.Label(self.frame_controles, text="Dias de Simulação:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(self.frame_controles, textvariable=self.dias_simulacao, width=5).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.frame_controles, text="Simular", command=self.simular_mercado_acoes).grid(row=0, column=2, padx=5, pady=5)

        self.fig, self.ax = plt.subplots(figsize=(5, 3), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

    def simular_mercado_acoes(self):
        try:
            dias_simulacao = self.dias_simulacao.get()
            if dias_simulacao <= 0:
                raise ValueError("Insira um número positivo de dias.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            return

        self.preco_acao = [self.valor_inicial]

        for dia in range(1, dias_simulacao):
            variacao = random.uniform(-5, 5)
            novo_preco = self.preco_acao[-1] + variacao
            self.preco_acao.append(max(0, novo_preco))

        self.plotar_grafico()
        self.exibir_resultado_final()

    def plotar_grafico(self):
        self.ax.clear()
        self.ax.plot(range(1, len(self.preco_acao) + 1), self.preco_acao, label='Preço da Ação', color='blue')
        self.ax.set_ylabel('Preço', color='blue')
        self.ax.set_xlabel('Dias')
        self.ax.legend(loc='upper left')
        self.canvas.draw()

    def exibir_resultado_final(self):
        resultado_final = f"Preço final da ação: {self.preco_acao[-1]:.2f} USD"
        messagebox.showinfo("Resultado da Simulação", resultado_final)

class App:
    def __init__(self, root):
        self.root = root
        self.simulacao = SimulacaoMercadoAcoes(root)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
