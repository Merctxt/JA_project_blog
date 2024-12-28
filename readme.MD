# *James Arthur Fan Blog*

*Este projeto é um blog dedicado ao artista James Arthur, criado usando Django. O objetivo é oferecer um espaço onde os fãs possam acessar informações, como posts sobre o artista, agenda de shows, galeria de fotos e uma página de contato.*

## *Estrutura do Projeto*

*O projeto foi desenvolvido com apenas um app, chamado **`blog`**, e inclui as seguintes funcionalidades:*

### ***Funcionalidades Gerais***

- ***Usuários****:*
  - *Login/Logout.*
  - *Controle de acesso para criação e edição de posts (apenas para administradores).*
- ***Posts****:*
  - *Exibição de posts na página inicial.*
  - *Detalhamento de cada post com opção de comentar (se configurado).*
- ***Extras****:*
  - *Agenda de shows.*
  - *Galeria de fotos.*
  - *Formulário de contato para visitantes.*

## ***Tecnologias Utilizadas***

- ***Backend****:*
  - *Django (Framework principal).*
  - *SQLite (Banco de dados padrão para desenvolvimento).*
- ***Frontend****:*
  - *HTML e CSS simples (templating do Django).*

## *\*\*Estrutura do App \*\*\`\`*

### ***Models***

- ***Post****: Representa os posts do blog, com campos como título, conteúdo, data de publicação e autor.*
- ***Comentário****: Vinculado a posts, permitindo interações dos usuários.*
- ***Evento****: Representa a agenda de shows do artista.*
- ***Contato****: Armazena mensagens enviadas através do formulário de contato.*

### ***Views***

- ***Posts****:*
  - *Lista de posts na página inicial.*
  - *Detalhamento de cada post.*
- ***Agenda****:*
  - *Listagem dos eventos planejados.*
- ***Contato****:*
  - *Formulário para visitantes enviarem mensagens.*

### ***Templates***

- ***Base Template****: Layout padrão para herança em todas as páginas.*
- ***Páginas Específicas****:*
  - *Lista de posts.*
  - *Detalhes do post.*
  - *Agenda de shows.*
  - *Página de contato.*

## *Como Rodar o Projeto Localmente*

1. ***Clone o repositório****:*

   ```bash
   git clone https://github.com/seu-usuario/james_arthur_blog.git
   cd james_arthur_blog
   ```

2. ***Crie e ative um ambiente virtual****:*

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. ***Instale as dependências****:*

   ```bash
   pip install -r requirements.txt
   ```

4. ***Aplique as migrações****:*

   ```bash
   python manage.py migrate
   ```

5. ***Rode o servidor****:*

   ```bash
   python manage.py runserver
   ```

6. ***Acesse o site****: Abra seu navegador e acesse **`http://127.0.0.1:8000/`**.*

## *Melhorias Futuras*

- *Implementar upload de imagens para a galeria.*
- *Melhorar o design do site usando frameworks como Bootstrap.*
- *Adicionar sistema de busca para posts e eventos.*

## *Contribuições*

*Contribuições são bem-vindas! Por favor, envie um pull request ou abra uma issue com sugestões.*

---

***Criado por:**** Giovanni*

