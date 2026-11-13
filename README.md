# Receitas

Aplicação web em Django para cadastro, busca e visualização de receitas culinárias. Usuários autenticados podem cadastrar receitas, consultar ingredientes e modo de preparo, enviar fotos e interagir com as receitas.

## Tecnologias

- Python
- Django 5.2.4
- SQLite
- Pillow, para upload e processamento de imagens
- Django Templates
- Django Admin

## Pré-requisitos

Antes de começar, instale:

- Python 3.11 ou superior;
- Git, caso o projeto seja obtido por um repositório Git.

O SQLite já vem incluído na instalação padrão do Python. Não é necessário instalar um servidor de banco de dados separado.

Confira as versões instaladas:

```powershell
python --version
git --version
```

## Instalação no Windows

Execute os comandos a partir da pasta que contém o arquivo `manage.py`.

### 1. Obter o projeto

```powershell
git clone <URL_DO_REPOSITORIO>
cd receitas
```

Se o projeto já estiver disponível localmente, apenas entre na pasta dele:

```powershell
cd C:\caminho\para\receitas
```

### 2. Criar o ambiente virtual

```powershell
python -m venv venv
```

O ambiente virtual fica na pasta `venv/` e não deve ser versionado.

### 3. Ativar o ambiente virtual

```powershell
.\venv\Scripts\Activate.ps1
```

Quando a ativação funcionar, o terminal normalmente exibirá `(venv)` no início da linha.

Se o PowerShell bloquear a execução de scripts, libere apenas para a sessão atual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

As versões principais estão fixadas em `requirements.txt` para que todos trabalhem com o mesmo ambiente.

## Banco de dados

Este projeto usa SQLite. O arquivo `db.sqlite3` é local e é criado automaticamente pelo Django quando as migrações são aplicadas.

```powershell
python manage.py migrate
```

Esse comando cria as tabelas padrão do Django e as tabelas da aplicação de receitas. O banco local não deve ser enviado para o repositório.

Para criar um usuário administrador:

```powershell
python manage.py createsuperuser
```

O usuário criado poderá acessar o painel em `/admin/`.

## Configuração por ambiente

O arquivo `.env.example` documenta as variáveis usadas pela aplicação. Ele não deve ser renomeado ou enviado como `.env` com segredos reais para o Git.

Variáveis disponíveis:

```text
DJANGO_SECRET_KEY=chave-secreta-do-ambiente
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

No desenvolvimento local, a aplicação possui valores padrão seguros apenas para uso local. Em produção, defina uma chave secreta própria, desative o debug e informe os hosts permitidos.

Exemplo no PowerShell:

```powershell
$env:DJANGO_SECRET_KEY = "uma-chave-longa-e-secreta"
$env:DJANGO_DEBUG = "False"
$env:DJANGO_ALLOWED_HOSTS = "exemplo.com,www.exemplo.com"
```

## Executar o projeto

Com o ambiente virtual ativado:

```powershell
python manage.py runserver
```

Abra no navegador:

- Aplicação: <http://127.0.0.1:8000/>
- Login: <http://127.0.0.1:8000/accounts/login/>
- Cadastro: <http://127.0.0.1:8000/accounts/register/>
- Administração: <http://127.0.0.1:8000/admin/>

Para escolher outra porta:

```powershell
python manage.py runserver 8080
```

Pressione `Ctrl+C` para parar o servidor.

## Comandos úteis do Django

```powershell
# Verificar configurações do projeto
python manage.py check

# Criar novas migrações depois de alterar models.py
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Executar testes
python manage.py test

# Abrir um terminal interativo com o Django carregado
python manage.py shell

# Coletar arquivos estáticos para produção
python manage.py collectstatic
```

Depois de alterar modelos, o fluxo esperado é:

```powershell
python manage.py makemigrations
python manage.py migrate
```

As migrações geradas devem ser versionadas no Git. O banco `db.sqlite3` não deve ser versionado.

## Uploads e arquivos estáticos

- `recipe/static/recipe/css/`: CSS pertencente à aplicação de receitas;
- `media/`: imagens enviadas pelos usuários;
- `templates/`: templates compartilhados e templates de autenticação;
- `recipe/templates/recipe/`: templates específicos de receitas.

Em desenvolvimento, o Django serve os arquivos de `media/` quando `DEBUG=True`. Em produção, o servidor web deve ser configurado para servir os arquivos estáticos e a mídia.

## Estrutura do projeto

```text
manage.py
config/
├── settings.py       # Configurações globais
├── urls.py           # URLs principais
├── asgi.py           # Entrada ASGI
└── wsgi.py           # Entrada WSGI
accounts/             # Cadastro e autenticação
recipe/               # Domínio de receitas
├── models.py         # Modelo Receita
├── forms.py          # Formulários
├── views.py          # Regras de requisição e resposta
├── urls.py           # URLs da aplicação
├── admin.py          # Configuração do Django Admin
├── migrations/       # Histórico do banco
├── templates/        # Templates da aplicação
└── static/           # Estáticos da aplicação
templates/            # Templates compartilhados
media/                # Uploads locais
requirements.txt      # Dependências Python
```

As aplicações ficam diretamente na raiz, seguindo o layout tradicional do Django. `config/` contém apenas configuração global; regras de negócio devem ficar dentro das aplicações.

## Fluxo de trabalho para colaboradores

```powershell
git pull
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py check
python manage.py test
```

Antes de enviar alterações:

```powershell
git status
git diff
python manage.py check
python manage.py test
```

Não envie para o repositório:

- `venv/`;
- `db.sqlite3`;
- `.env`;
- `__pycache__/` e arquivos `.pyc`;
- arquivos temporários de execução.

Esses itens já estão protegidos pelo `.gitignore`.

## Solução de problemas

### `python` não é reconhecido

Instale o Python e marque a opção para adicioná-lo ao `PATH`. Depois, feche e abra o PowerShell novamente.

### O ambiente virtual não ativa

Execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

Se o ambiente estiver apontando para uma instalação antiga do Python, recrie-o:

```powershell
Remove-Item -Recurse -Force venv
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### `No module named django`

Ative o ambiente virtual e reinstale as dependências:

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Alterações no banco não aparecem

Gere e aplique as migrações:

```powershell
python manage.py makemigrations
python manage.py migrate
```

### Erro ao fazer upload de imagem

Confirme que o Pillow está instalado:

```powershell
pip install -r requirements.txt
```

Também verifique se a pasta `media/` existe e se o formulário foi enviado com `enctype="multipart/form-data"`.
