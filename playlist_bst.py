class No:
    def __init__(self, nome, autor, duracao):
        self.nome = nome
        self.autor = autor
        self.duracao = duracao
        self.esq = None
        self.dir = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, nome, autor, duracao):
        novo_no = No(nome, autor, duracao)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)
        print(f"Música '{nome}' inserida com sucesso!")

    def _inserir_recursivo(self, atual, novo_no):
        # Organização alfabética (case-insensitive para evitar erros)
        if novo_no.nome.lower() < atual.nome.lower():
            if atual.esq is None:
                atual.esq = novo_no
            else:
                self._inserir_recursivo(atual.esq, novo_no)
        else:
            if atual.dir is None:
                atual.dir = novo_no
            else:
                self._inserir_recursivo(atual.dir, novo_no)

    def buscar(self, nome_busca):
        caminho = ["raiz"]
        return self._buscar_recursivo(self.raiz, nome_busca.lower(), caminho, 0)

    def _buscar_recursivo(self, atual, nome_busca, caminho, nivel):
        if atual is None:
            return None, None, None

        if atual.nome.lower() == nome_busca:
            return atual, caminho, nivel

        if nome_busca < atual.nome.lower():
            caminho.append("esquerda")
            return self._buscar_recursivo(atual.esq, nome_busca, caminho, nivel + 1)
        else:
            caminho.append("direita")
            return self._buscar_recursivo(atual.dir, nome_busca, caminho, nivel + 1)

def executar_playlist():
    bst = ArvoreBinariaBusca()
    
    # Lista fixa de 10 músicas para facilitar o teste
    musicas = [
        ("Diaba", "Urias", 186),
        ("AmarElo", "Emicida", 320),
        ("Inertia", "AJR", 220),
        ("Zombified", "Falling in Reverse", 218),
        ("Bones", "Imagine Dragons", 165),
        ("Hype", "Dizzee Rascal", 213),
        ("Levitating", "Dua Lipa", 203),
        ("Numb", "Linkin Park", 185),
        ("Overpass Graffiti", "Ed Sheeran", 236),
        ("X1", "MC IG", 145)
    ]

    for m in musicas:
        bst.inserir(m[0], m[1], m[2])

    print("\n" + "="*30)
    busca = input("Digite o nome da música para buscar: ")
    print("="*30)

    no_encontrado, caminho, nivel = bst.buscar(busca)

    if no_encontrado:
        print("\nMúsica encontrada")
        print(f"Nome: {no_encontrado.nome}")
        print(f"Autor: {no_encontrado.autor}")
        print(f"Duração: {no_encontrado.duracao} segundos")
        print("\nCaminho percorrido:")
        print(" → ".join(caminho))
        print(f"\nNível na árvore: {nivel}")
    else:
        print("\nMúsica não encontrada.")

if __name__ == "__main__":
    executar_playlist()