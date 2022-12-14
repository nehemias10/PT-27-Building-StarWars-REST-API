"""empty message

Revision ID: deab1c8671c3
Revises: 
Create Date: 2022-08-24 00:23:00.102651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'deab1c8671c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=120), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('hair', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('planets',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email')
    )
    op.create_table('favPeople',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=120), nullable=True),
    sa.Column('people_uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people_uid'], ['people.uid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favPlanet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=120), nullable=True),
    sa.Column('planet_uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_uid'], ['planets.uid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favPlanet')
    op.drop_table('favPeople')
    op.drop_table('user')
    op.drop_table('planets')
    op.drop_table('people')
    # ### end Alembic commands ###
