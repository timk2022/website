"""empty message

Revision ID: 6a911b6eb7c0
Revises: d774d35ef1d0
Create Date: 2020-01-21 12:54:25.302635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a911b6eb7c0'
down_revision = 'd774d35ef1d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('blurb', sa.String(), nullable=True))
    op.drop_column('post', 'image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('image', sa.VARCHAR(), nullable=True))
    op.drop_column('post', 'blurb')
    # ### end Alembic commands ###