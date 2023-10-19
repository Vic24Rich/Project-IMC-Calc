import tkinter as tk


def imc():
  peso = float(peso_entry.get())
  altura = float(altura_entry.get())
  imc = peso / (altura * altura)
  imc_label.config(text=f'IMC: {imc:.2f}')

  if imc < 18.5:
    status_label.config(text='Abaixo do peso')
  elif imc < 25:
    status_label.config(text='Peso ideal')
  elif imc < 30:
    status_label.config(text='Sobrepeso')
  elif imc < 35:
    status_label.config(text='Obesidade grau I')
  elif imc < 40:
    status_label.config(text='Obesidade grau II')
  else:
    status_label.config(text='Obesidade Morbida')


root = tk.Tk()
root.title('Calculadora de IMC')
root.geometry('500x300')
root.configure(background='#e5ead4')

peso_label = tk.Label(root,
                      text='Peso (kg):',
                      font=('Comics San', 11, 'bold'),
                      fg='#1f0a1d',
                      bg='#e5ead4')
peso_label.grid(row=1, column=1)
peso_entry = tk.Entry(root,
                      font=('Comics San', 11, 'bold'),
                      fg='#e5ead4',
                      bg='#1f0a1d')
peso_entry.grid(row=1, column=2)

altura_label = tk.Label(root,
                        text='Altura (m):',
                        font=('Comics San', 11, 'bold'),
                        fg='#1f0a1d',
                        bg='#e5ead4')
altura_label.grid(row=2, column=1)
altura_entry = tk.Entry(root,
                        font=('Comics San', 11, 'bold'),
                        fg='#e5ead4',
                        bg='#1f0a1d')
altura_entry.grid(row=2, column=2)

imc_label = tk.Label(root,
                     text='IMC:',
                     font=('Comics San', 11, 'bold'),
                     fg='#1f0a1d',
                     bg='#e5ead4')
imc_label.grid(row=4, column=1)

status_label = tk.Label(root,
                        text='Status:',
                        font=('Comics San', 11, 'bold'),
                        fg='#1f0a1d',
                        bg='#e5ead4')
status_label.grid(row=5, column=1)

imc_button = tk.Button(root,
                       text='Calcular',
                       command=imc,
                       font=('Comics San', 11, 'bold'),
                       fg='#1f0a1d',
                       bg='#9acc77')
imc_button.grid(row=3, column=2)

root.mainloop()
