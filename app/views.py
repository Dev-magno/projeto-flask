from app import app, db
from flask import render_template, url_for, request, redirect
from flask_login import login_user, logout_user, current_user
from app.models import Contato
from app.forms import ContatoForm, UseForme, LoginForm



@app.route('/', methods = ['GET', 'POST'])
def homepage():
    usuario = 'Magno'
    form = LoginForm()

    if form.validate_on_submit():
        user = form.login()
        login_user(user, remember=True)
        

    context = {
        'usuario': usuario
    }

    return render_template('index.html', context=context, form=form)



@app.route('/cadastro/', methods = ['GET', 'POST'])
def cadastro():
    form = UseForme()
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    return render_template('cadasttro.html', form=form)


@app.route('/sair/')
def logout():
    logout_user()
    return redirect(url_for('homepage'))



@app.route('/contato/', methods = ['GET', 'POST'])
def contato():
    form = ContatoForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
     
    return render_template('contato.html', context=context, form=form)



@app.route('/contato/lista')
def contatoLista():
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')

    dados = Contato.query.order_by('nome')
    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa)
    context = {'dados': dados.all()}

    return render_template('contato_lista.html', context=context)


@app.route('/contato/<int:id>/')
def contatoDatail(id):
    obj = Contato.query.get(id)
    return render_template('contato_datail.html', obj=obj)
