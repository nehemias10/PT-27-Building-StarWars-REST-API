"""empty message

Revision ID: 56026d47babf
Revises: 2075814f217f
Create Date: 2022-08-18 22:42:42.016325

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '56026d47babf'
down_revision = '2075814f217f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favPlanet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_uid'], ['planets.uid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('favPlanets')
    op.drop_index('name', table_name='user')
    op.drop_column('user', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', mysql.VARCHAR(length=120), nullable=False))
    op.create_index('name', 'user', ['name'], unique=False)
    op.create_table('favPlanets',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('planets_uid', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['planets_uid'], ['planets.uid'], name='favPlanets_ibfk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='favPlanets_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('favPlanet')
    # ### end Alembic commands ###
