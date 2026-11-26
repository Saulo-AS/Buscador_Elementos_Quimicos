from banco import elementos_quimicos, mapa_acentos, alfabeto

def limpar_acentos(texto):
  novo_elemento_input = ""
  for A in texto:
    if A in alfabeto:
        if A in mapa_acentos:
            A = mapa_acentos[A]
            novo_elemento_input += A
        
        else:
            novo_elemento_input += A
    else:
       print(f"ERRO a palavra contém caracteres que não estão no alfabeto pt-BR. Caractere: {A}")
    return novo_elemento_input


def buscar_elemento(novo_elemento_input):
  if novo_elemento_input in elementos_quimicos:
    print(elementos_quimicos[novo_elemento_input])
  else:
    print("Elemento não encontrado.")


# Loop principal do programa
while True:
  print("=====DETECTOR DE ELEMENTOS QUÍMICOS=====")
  elemento_input = input("Digite qual elemento deseja procurar: ").lower().strip()

  # Chama a função de limpeza que você construiu
  novo_elemento_input = limpar_acentos(elemento_input)

  # Chama a função de busca
  buscar_elemento(novo_elemento_input)