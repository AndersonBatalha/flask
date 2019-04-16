# Flask
#### Exemplo de aplicação construída com o framework Flask

1.  Instalar o pip, gerenciador de pacotes do Python

		$ sudo apt-get install python-pip

2.  Criar o ambiente virtual

	1.  Instalar o pacote virtualenv
	
			$ sudo apt-get install virtualenv virtualenvwrapper

	2. Na pasta do projeto, criar o ambiente virtual
	 
			$ mkvirtualenv -p `which python3` my_env

	3. Ativar / desativar o ambiente virtual
	
			$ source env/bin/activate
			$ deactivate
	
	4. Principais comandos
		
		1. Criar um novo ambiente
			
				$ mkvirtualenv -p `which python` my_env
					   
		2. Listar os ambientes criados
			
				$ lsvirtualenv

		3. Remover
			
				$ rmvirtualenv my_env

		4. Mostrar detalhes do ambiente virtual
			
				$ showvirtualenv env2

		5. Alternar entre ambientes
			
				(env) $ workon env2

3.  Controle de versão
 
	1. Criar repositório no GitHub / Bitbucket
	
	2. Adicionar .gitignore
		1.  http://gitignore.io
	
	3. Alterar arquivo README.md
	
	4. Comandos principais
		1. Obter o status atual do repositório

				$ git status
		2. Adicionar arquivos ao HEAD

				$ git add *
			
		3. Enviar os arquivos ao repositório local

				$ git commit -m "mensagem" 

		4. Enviar os arquivos ao repositório remoto

				$ git push origin master 


4. Gerenciar as dependências do projeto

	1. Listar todas as dependências instaladas
	
			$ pip freeze

	2. Após instalar todos os pacotes necessários, é possível gerar um arquivo com as dependências instaladas.
	
			$ pip freeze > requirements.txt

	3. Caso seja necessário reinstalar esses pacotes em outra máquina, basta executar:
	
			$ pip install -r requirements.txt

5.  Verificar as versões instaladas
	1. Python
	
			$ python --version

	2. Flask
	
		    $ flask --version

6. Flask
  
    1. Instalação
    
            $ workon env
            $ pip install flask flask_bootstrap wtforms
            $ pip freeze > requirements.txt
    
    2. Criar projeto
    
        1. Criar arquivo main.py
        2. Configurações iniciais
        
                from flask import Flask
                app = Flask(__name__)
                
        3. Roteamento
        
                @app.route('url')
                
           1. Passagem de parâmetros
                
                    @app.route('/index/<nome>')
                    @app.route('/index/<str:nome>')
                    @app.route('/index/<int: id>')
    
        4. 

6. Banco de dados 

    1. Instalação

            $ pip install flask_sqlalchemy flask_migrate

    2. Configurações
            
            app = Flask(__name__)

            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')
            app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            
            db = SQLAlchemy(app)
            migrate = Migrate(app=app, db=db)

    3. Shell    
    
            \>>> from main import Role
            
            \>>> from main import db
            
            \>>> admin = Role(name='Administrador')
            
            \>>> admin
            <Role 'Administrador'>
            \>>> db.session.add(admin)
            \>>> db.session.commit()

