"""empty message

Revision ID: fc4b3bd6f52a
Revises: f7ddfaed9bf8
Create Date: 2020-01-22 23:26:56.571599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc4b3bd6f52a'
down_revision = 'f7ddfaed9bf8'
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
