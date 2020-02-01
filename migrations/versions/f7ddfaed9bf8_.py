"""empty message

Revision ID: f7ddfaed9bf8
Revises: f3e125645776
Create Date: 2020-01-22 23:24:27.394734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7ddfaed9bf8'
down_revision = 'f3e125645776'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'image')
    op.add_column('project', sa.Column('blurb', sa.String(), nullable=True))
    op.add_column('project', sa.Column('type_project', sa.String(), nullable=True))
    op.add_column('project', sa.Column('url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'url')
    op.drop_column('project', 'type_project')
    op.drop_column('project', 'blurb')
    op.add_column('post', sa.Column('image', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###