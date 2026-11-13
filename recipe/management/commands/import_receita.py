# 1. Ferramentas do Django e do Python
from recipe.models import Receita
from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):
    help = 'Testando conexao API' #help é pra quando alguem quer saber o que a API faz

    def handle(self, *args, **options): #É o método principal (a função) que o Django executa automaticamente assim que você roda o comando no terminal.
        url = "https://www.themealdb.com/api/json/v1/1/search.php?s=" #URL da API
        
        # Exibe mensagem amarela no terminal avisando o início da operação por causa do WARNING
        self.stdout.write(self.style.WARNING("Iniciando conexao com a API..."))
        

        resposta = requests.get(url)
        
        # Checagem de segurança HTTP: 200 significa "Sucesso"
        if resposta.status_code == 200:

            dados = resposta.json()

            # Pega a lista de receitas dentro da chave 'meals' do JSON. Se não existir, retorna uma lista vazia []
            receitas = dados.get('meals', [])
            
            # Avisa no terminal que a requisição funcionou
            self.stdout.write(self.style.SUCCESS(f"Conexao estabelecida com sucesso! Código HTTP: {resposta.status_code}"))
            
            #  verifica se as receitas vieram em uma lista (verificamos 'receitas', pois 'dados' é o dicionário completo)
            if isinstance(receitas, list):
                total = len(receitas)
                self.stdout.write(f"Total de receitas encontradas na API: {total}") 
                
                # Se houver receitas na lista, mostra o primeiro item como exemplo para inspeção
                if total > 0:
                    self.stdout.write("\n--- Exemplo da primeira receita que veio do JSON ---")
                    self.stdout.write(str(receitas[0]))
                    self.stdout.write("---------------------------------------------------\n")

                    # Novo bloco: Percorre a lista e salva cada receita no banco de dados (model Receita)
                    self.stdout.write(self.style.WARNING("Salvando receitas no banco de dados..."))
                    for item in receitas:
                        Receita.objects.create(
                            name=item.get('strMeal'),
                            preparationmethod=item.get('strInstructions'),
                            fotos=item.get('strMealThumb')
                        )
                    self.stdout.write(self.style.SUCCESS("Receitas salvas com sucesso no banco de dados!"))

            else:
                # Se a API não respondeu uma lista, exibe o conteúdo bruto recebido
                self.stdout.write("Os dados nao vieram no formato de lista. Retorno recebido:")
                self.stdout.write(str(dados))
                
        else:
            # Se a API falhou (código diferente de 200), exibe o erro em vermelho
            self.stdout.write(
                self.style.ERROR(f"Falha ao conectar na API. Código de erro HTTP: {resposta.status_code}")
            )