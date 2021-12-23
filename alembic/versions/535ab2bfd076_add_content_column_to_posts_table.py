"""add content column to posts table

Revision ID: 535ab2bfd076
Revises: 129dc185d0f1
Create Date: 2021-12-22 13:05:23.268924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '535ab2bfd076'
down_revision = '129dc185d0f1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
