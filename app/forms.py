from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app import db, bcrypt
from app.models import Contato, User, Post, PostComentarios

class UseForme(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    btnsubmit = SubmitField('Cadastrar')

    def validade_email(self, email):
        if User.Query.filter(email=email.data).first():
            return ValidationError('Usuário já cadastro com esse e-mail')

    
    def save(self):
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
        user = User(
            nome = self.nome.data,
            sobrenome = self.sobrenome.data,
            email = self.email.data,
            senha = senha
        )

        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btnsubmit = SubmitField('Login')

    def login(self):
        # Recuperar o email
        user = User.query.filter_by(email=self.email.data).first()

        # Verificar se a senha é válida
        if user:
            if bcrypt.check_password_hash(user.senha, self.senha.data.encode('utf-8')):
                # Retorna o usuário
                return user
            else:
                raise Exception('Senha inválida!')
        else:
            raise Exception('Usuário não encontrado')


class ContatoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    assunto = StringField('Assunto', validators=[DataRequired()])
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    btnsubmit = SubmitField('Enviar')

    def save(self):
        contato = Contato(
            nome = self.nome.data,
            email = self.email.data,
            assunto = self.assunto.data,
            mensagem = self.mensagem.data
        )

        db.session.add(contato)
        db.session.commit()


class PostForm(FlaskForm):
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    btnsubmit = SubmitField('Enviar')

    def save(self, user_id):
        post = Post(
            mensagem = self.mensagem.data,
            user_id = user_id
        )

        db.session.add(post)
        db.session.commit()


class PostComentariosForm(FlaskForm):
    comentario = StringField('Comentario', validators=[DataRequired()])
    btnsubmit = SubmitField('Enviar')

    def save(self, user_id, post_id):
        comentario = PostComentarios(
            comentario =self.comentario.data,
            user_id=user_id,
            post_id=post_id
        )

        db.session.add(comentario)
        db.session.commit()

        

