"""empty message

Revision ID: 1dbb6aea31ec
Revises: 5261344d5bfb
Create Date: 2014-09-05 14:22:22.230132

"""

# revision identifiers, used by Alembic.
revision = '1dbb6aea31ec'
down_revision = '5261344d5bfb'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cronotipos', sa.Column('result', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cronotipos', 'result')
    ### end Alembic commands ###