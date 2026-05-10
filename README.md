# Projeto Multidisciplinar: API Raízes do Nordeste (Back-end)

Esta é a API RESTful desenvolvida para a rede "Raízes do Nordeste", contemplando os requisitos do MVP escolhido, que foi o Fluxo A.

## Tecnologias e Requisitos
- **Linguagem:** Python 3.10+
- **Framework:** FastAPI
- **Banco de Dados:** SQLite
- **ORM:** SQLAlchemy
- **Autenticação:** JWT

## Como instalar e configurar

1. Clone o repositório para a sua máquina:

   git clone https://github.com/omatheusanjos/api-raizes-do-nordeste.git
   cd raizes-do-nordeste-api

Crie e ative um ambiente virtual:
- Windows: python -m venv venv e depois venv\Scripts\activate
- Linux/Mac: python3 -m venv venv e depois source venv/bin/activate
Instale as dependências do projeto:

## Banco de Dados
O projeto utiliza o SQLite para facilitar a avaliação. Não é necessário instalar nenhum banco de dados externo. As migrations e a criação das tabelas (incluindo as regras de negócio de multicanalidade) são executadas automaticamente pela API no momento da inicialização.

## Como iniciar a API
Com o ambiente virtual ativado, rode o servidor com o comando:
uvicorn main:app --reload

## Documentação (Swagger / OpenAPI)
Com o servidor rodando, a documentação interativa da API poderá ser acessada no seu navegador através do link: http://127.0.0.1:8000/docs

## Testes
O arquivo de coleção contendo os cenários de testes exigidos encontra-se na raiz deste repositório com o nome Raizes_do_Nordeste_Postman.json. Importe este arquivo no Postman ou Insomnia para validar os fluxos positivos e de exceção.
