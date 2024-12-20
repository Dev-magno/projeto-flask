"""empty message

Revision ID: 3a948af13c7b
Revises: 72c778bf4364
Create Date: 2024-11-28 13:23:48.593956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a948af13c7b'
down_revision = '72c778bf4364'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_comentarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_criação', sa.DateTime(), nullable=True),
    sa.Column('comentario', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_comentarios')
    # ### end Alembic commands ###
