from Models import Categoria, Produtos, Estoque, Venda, Fornecedor, Pessoa, Funcionario
from DAO import DaoCategoria, DaoEstoque, DaoVenda, DaoFornecedor, DaoPessoa, DaoFuncionario
from datetime import datetime


class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print("Categoria cadastrada com sucesso!")
        else:
            print("Categoria já cadastrada no sistema!")

    def excluirCategoria(self, categoriaExcluir):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaExcluir, x))
        
        if len(cat) <= 0:
            print("Categoria não encontrada!")
        else:
            for i in range(len(x)):   
                if x[i].categoria == categoriaExcluir:
                    del x[i]
                    break
            print("Categoria excluída com sucesso!")

            with open('categoria.txt', 'w') as arq:    
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')



a = ControllerCategoria()
a.cadastrarCategoria('Frios')            