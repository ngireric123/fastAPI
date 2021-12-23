"""create posts table

Revision ID: 129dc185d0f1
Revises: 
Create Date: 2021-12-22 12:11:20.010406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '129dc185d0f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.column('title'sa.String(), nullable=False))

    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title',                    sa.String(), nullable=False))
    
    pass


def downgrade():
    op.drop_table('posts')
    pass
