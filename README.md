# SGEN – Sistema de Gestão de Equipamentos de Notebook

O SGEN é um sistema web para gestão de empréstimo de notebooks de uma instituição de ensino.  
O objetivo é controlar patrimônio, registrar empréstimos e devoluções, e oferecer uma visão organizada do uso dos equipamentos ao longo do tempo. [file:1]

## Tecnologias utilizadas

- Backend / Web: Python / Django
- Banco de Dados: SQLite
- ORM: Django ORM
- Controle de versão: Git / GitHub

## Uso de Inteligência Artificial

Neste projeto **não foi utilizada IA no backend**.  
Todas as regras de negócio, modelagem de entidades e implementação das views, models e regras de validação foram desenvolvidas manualmente, com base em conceitos de engenharia de software e boas práticas de desenvolvimento web. 

Houve apenas apoio pontual de IA **no frontend** (quando aplicável), para auxiliar em:

- Ideias de interface;
- Ajustes de layout e componentes;
- Sugestões de textos e melhorias visuais.

As decisões de modelagem de dados, regras de negócio e arquitetura do backend em Django foram tomadas pelo desenvolvedor ao longo do desenvolvimento do projeto.

## Decisões de banco de dados e aprendizados

As principais decisões sobre o modelo de banco de dados (models do Django, relacionamentos e restrições) foram tomadas **durante** o desenvolvimento, e não completamente definidas antes do início da implementação.

Isso trouxe alguns impactos importantes:

- Necessidade de **refatorar models e relacionamentos** no meio do projeto;
- Criação e ajuste frequente de migrations;
- Readequação de views, forms e templates por causa de mudanças de modelo;
- Aumento de retrabalho e dificuldade para manter o código limpo e coerente.

Esse processo gerou um aprendizado relevante:

> Definir o modelo conceitual (MER) e o esquema de banco de dados com mais cuidado **antes** de implementar reduz bastante retrabalho, evita inconsistências e facilita a evolução do sistema. 

Como lição, projetos futuros devem:

- Investir mais tempo em modelagem conceitual e validação de regras de negócio antes de criar os models;
- Validar regras com o “cliente” (professor/usuário) antes de consolidar o modelo de dados;
- Manter a documentação de requisitos e do banco de dados sempre alinhada com o código. 

## Escopo do sistema

O sistema foi desenvolvido com base em uma especificação de requisitos, contendo funcionalidades para:

- Cadastro e autenticação de usuários (alunos, professores, administradores);
- Cadastro e controle de notebooks (patrimônio, status, histórico de uso);
- Regras de empréstimo e devolução dentro de janelas de horário específicas;
- Controle de acessório (carregador);
- Geração de comprovante digital de empréstimo;
- Painel administrativo e histórico de empréstimos;
- Controle de perfis de usuário e cadastro de turmas;
- Funcionalidades administrativas de consulta de usuários e turmas. 


## Como executar o projeto

> Ajuste nomes conforme seu projeto real (nome do app, do módulo de settings etc.).

1. Clonar o repositório:
   ```bash
   git clone https://github.com/michaeldouglasx/SGEN-Sistema-de-Gestao-de-Equipamentos-de-Notebook.git
   ```

2. Criar e ativar um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # ou
   venv\Scripts\activate     # Windows
   ```

3. Instalar as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplicar as migrations:
   ```bash
   python manage.py migrate
   ```

5. Criar um superusuário (opcional, para acessar o admin do Django):
   ```bash
   python manage.py createsuperuser
   ```

6. Rodar o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

7. Acessar o sistema no navegador:
   - Aplicação: `http://127.0.0.1:8000/`
   - Admin Django: `http://127.0.0.1:8000/admin/`

## Estado atual do projeto

Este projeto foi desenvolvido como parte de atividade acadêmica, com foco em:

- Aplicar conceitos de desenvolvimento web com Django;
- Praticar modelagem de banco de dados e relacionamento entre models;
- Exercitar boas práticas de organização de apps, views, templates e urls. 

Ainda há espaço para evolução em pontos como:

- Melhorar a modelagem inicial do banco de dados;
- Refinar as regras de negócio;
- Otimizar a experiência do usuário no frontend;
- Ampliar testes automatizados (unitários e de integração). 

## Autor

- Michael Douglas – Brasília/DF – Desenvolvedor backend (Python-Django/Java-Spring-boot) e estudante de Análise e Desenvolvimento de Sistemas.
