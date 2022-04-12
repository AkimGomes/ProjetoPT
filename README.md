# ProjetoPT
Projeto voltado para o cadastro, login, logout, exclusão e edição de dados do usuário. Ao se cadastrarem serão redirecionados e poderão realizar o login e a visualização de suas informações. 
# Instalação e Inicialização
- Instalar o Poetry e iniciar.
- Instalar o Python 3.8.
- Instalar o Flask 2.0.2.
- Instalar o Flask-Login 0.5.0.
- Instalar o Flask-SQLAlchemy 2.5.1.
- Instalar o SQLAlchemy 1.4.31.
- Instalar o PyMySQL 1.0.2.
- Instalar o cryptography 36.0.1.
- Após a instalação dos pacotes iniciais realizar a criação do banco de dados. Exemplo: MySQL Workbench -> create database ProjetoPT.
- Antes de rodar a aplicação, rodar o arquivo db.py para a criação das tabelas usadas no manuseio de dados do usuário.
- Rodar a aplicação e realizar o cadastro de usuário.
# Funcionalidades
# Login
Ao acessar a aplicação o usuário terá a renderização da página de login do usuário. O usuário poderá acessar o sistema realizando o login ou fazer um cadastro caso não esteja cadastrado, clicando em "Cadastrar".
![image](https://user-images.githubusercontent.com/88415808/163057242-1ea1aaac-cae9-4f51-8673-ff48c955f683.png)

# Cadastro de Usuário
Ao clicar em "Cadastrar" na tela de login, o usuário será redirecionado para a página de cadastro de usuário, onde poderá realizar o cadastro.
![image](https://user-images.githubusercontent.com/88415808/163057487-0048bf0e-ce98-4112-a442-847c5eecd0fc.png)

# Menu do Usuário (Home)
Ao usuário fazer o login na página inicial, a sessão do mesmo será armazenada em cookie pelo uso do Flask-Login, o qual conterá um token de autenticação gerado pelo mesmo.

![image](https://user-images.githubusercontent.com/88415808/163057979-bb9e3356-ce3a-481a-a286-51ea05dd8e8b.png)

Após a autenticação usuário no banco de dados, o mesmo será redirecionado para a página de menu do usuário, na qual poderá editar suas informações, excluir seu cadastro ou fazer logout da aplicação.

![image](https://user-images.githubusercontent.com/88415808/163058288-693d8bc1-8968-4fdd-9ef6-9fb34da2f561.png)

# Edição de Dados do Usuário
Caso o usuário deseje alterar as informações contidas em seu cadastro, o mesmo poderá clicar no botão de "Editar Informações", sendo redirecionado para a página de edição. Para concluir a edição o usuário deve preencher o campo de "senha" com a  mesma usada para login ou alterá-la como bem entender. No fim sendo redirecionado para a página de menu ou podendo deslogar ali mesmo.

![image](https://user-images.githubusercontent.com/88415808/163058686-dd39e707-9f84-4b3c-9d1d-c077d647a85d.png)
