# Aplicação de Agendamento de Automações com Django e Celery

Esta é uma aplicação desenvolvida em Python utilizando o framework Django e as bibliotecas Celery e Celery Beat para implementar mensageria e agendamento de tarefas. A aplicação tem como objetivo permitir o agendamento de automações, onde é possível definir a execução de robôs de webscrapping em intervalos de tempo pré-determinados.

## Tecnologias Utilizadas

A aplicação foi desenvolvida utilizando as seguintes tecnologias:

- Python: Linguagem de programação utilizada para desenvolver a aplicação.
- Django: Framework web de alto nível que fornece uma arquitetura MVC para desenvolver aplicativos web.
- Celery: Biblioteca que permite a execução de tarefas assíncronas e distribuídas.
- Celery Beat: Extensão do Celery que permite o agendamento de tarefas.
- Docker: Plataforma de código aberto que facilita a criação, o empacotamento e o fornecimento de aplicativos em contêineres.

## Como Executar a Aplicação

Para executar a aplicação localmente, é necessário ter o Docker instalado em sua máquina. Siga os passos abaixo:

1. Clone o repositório para sua máquina local: `git clone https://github.com/seu-usuario/nome-do-repositorio.git`

2. Navegue para o diretório do projeto:

```bash
cd nome-do-repositorio
```
Inicie a aplicação usando o Docker Compose:
```bash
docker-compose up
```

O Docker Compose se encarregará de construir e iniciar os contêineres necessários para a aplicação funcionar corretamente. Após a execução do comando acima, a aplicação estará disponível em http://localhost:1337/.

Funcionalidades Principais
A aplicação possui as seguintes funcionalidades principais:

Cadastro de Robôs de Webscrapping: Permite cadastrar informações sobre robôs de webscrapping, incluindo nome, descrição e parâmetros de configuração.

Agendamento de Automações: Permite criar agendamentos para execução dos robôs de webscrapping em horários específicos.

Execução dos Robôs: Os robôs de webscrapping são executados automaticamente de acordo com os horários agendados, realizando a coleta de dados dos sites ou APIs configurados.

Filtros e Pesquisa: A API permite filtrar os agendamentos com base em critérios como status code de resposta, data de agendamento, tipo de método HTTP, entre outros.

Configuração do Ambiente de Desenvolvimento
Caso queira contribuir para o desenvolvimento da aplicação, siga os passos abaixo para configurar o ambiente de desenvolvimento:

Clone o repositório para sua máquina local: git clone https://github.com/williamkleber1/django-web-scraping-scheduler-api

Navegue para o diretório do projeto:


```	bash
cd nome-do-repositorio
```	

Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```
Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```	
A aplicação estará disponível em http://localhost:8000/.