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

2. Crie e ative um ambiente virtual:
- Windows: python -m venv venv e depois venv\Scripts\activate
- Linux/Mac: python3 -m venv venv e depois source venv/bin/activate
Instale as dependências do projeto:

3. Instale as dependências do projeto:
   pip install -r requirements.txt

## Banco de Dados
O projeto utiliza o SQLite para facilitar a avaliação. Não é necessário instalar nenhum banco de dados externo. As migrations e a criação das tabelas (incluindo as regras de negócio de multicanalidade) são executadas automaticamente pela API no momento da inicialização.

## Como iniciar a API
Com o ambiente virtual ativado, rode o servidor com o comando:
uvicorn main:app --reload
A API estará disponível e rodando em: http://127.0.0.1:8000

## Documentação (Swagger / OpenAPI)

A documentação interativa da API, gerada automaticamente pelo FastAPI, reflete os contratos exatos dos endpoints implementados. 
Com o servidor rodando, acesse no seu navegador: http://127.0.0.1:8000/docs.
Lá é possível testar a autenticação JWT inserindo o token no botão "Authorize".

## Testes

Para evidenciar a integridade das regras de negócio, a validação de estoque e o tratamento padronizado de exceções, os cenários de testes exigidos encontram-se na raiz deste repositório no arquivo Raizes_do_Nordeste_Postman.json.
   1. Abra o Postman (ou Insomnia).
   2. Clique em Import e selecione o arquivo .json deste repositório.
   3. A coleção abrirá com pastas contendo os cenários positivos e negativos.
   - Importante: Rode primeiro o teste de Cadastrar Cliente e Login Válido para gerar o Bearer Token. Copie este token e adicione-o na aba Authorization dos testes subsequentes (como Pedidos e Pagamentos) para validar as rotas protegidas.
