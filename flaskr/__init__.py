import os

from flask import Flask

def create_app(test_config=None):
    # criaçao e configuraçao do aplicativo
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path,'flask.sqlite'),
    )
    #print(app.instance_path )
    if test_config is None :
        # carregar a configuraçao
        app.config.from_pyfile('config.py',silent=True)  
    else:
        # carregar a configuraçao de teste
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)
    from . import auth
    app.register_blueprint(auth.bp)
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/',endpoint='index')

    # return app
    # simples pagina que mostra ola
    @app.route('/hello')
    def hello():
        return 'Ola, mundo flask'
    return app
