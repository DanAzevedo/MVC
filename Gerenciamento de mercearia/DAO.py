from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria: Categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        print(cls.categoria)

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))

        return cat    
class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendidos.nome + "|" 
                           + venda.itensVendidos.preco + "|" 
                           + venda.itensVendidos.categoria + "|" 
                           + venda.vendedor + "|" 
                           + venda.cliente + "|" 
                           + venda.formaPagamento + "|" 
                           + venda.valorTotal + "|" 
                           + venda.desconto + "|" 
                           + venda.valorFinal + "|" 
                           + str(venda.quantidadeVendida) + "|" 
                           + venda.data)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()        

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        vendas = []
        for i in cls.venda:
            vendas.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]))
        return vendas    
class DaoEstoque:
    @classmethod     
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + "|" 
                           + produto.preco + "|" 
                           + produto.categoria + "|" 
                           + str(quantidade))
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))
        return est
class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoa.txt', 'a') as arq:
            arq.writelines(pessoa.nome + "|" 
                           + pessoa.telefone + "|" 
                           + pessoa.cpf + "|" 
                           + pessoa.email + "|" 
                           + pessoa.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            cls.clientes = arq.readlines()

        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))
        clientes = []
        for i in cls.clientes:
            clientes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return clientes    
class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionario.txt', 'a') as arq:
            arq.writelines(funcionario.nome + "|" 
                           + funcionario.telefone + "|" 
                           + funcionario.cpf + "|" 
                           + funcionario.email + "|" 
                           + funcionario.endereco + "|" 
                           + funcionario.clt)
            arq.writelines('\n')    

    @classmethod
    def ler(cls):
        with open('funcionario.txt', 'r') as arq:
            cls.funcionario = arq.readlines()

        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
        cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))
        funcionarios = []
        for i in cls.funcionario:
            funcionarios.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
        return funcionarios        
class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + "|" 
                           + fornecedor.cnpj + "|" 
                           + fornecedor.telefone + "|" 
                           + fornecedor.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedor.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()

        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))
        fornecedores = []
        for i in cls.fornecedor:
            fornecedores.append(Fornecedor(i[0], i[1], i[2], i[3]))
        return fornecedores


x = DaoVenda.ler()
print(x[0].itensVendidos.nome)
