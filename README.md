# flask-exemplo
#### Aplicação construída com o framework Flask

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
