"""empty message

Revision ID: a72808072d8
Revises: 1dbb6aea31ec
Create Date: 2014-09-05 14:36:08.346777

"""

# revision identifiers, used by Alembic.
revision = 'a72808072d8'
down_revision = '1dbb6aea31ec'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cronotipos', sa.Column('result_type', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cronotipos', 'result_type')
    ### end Alembic commands ###
