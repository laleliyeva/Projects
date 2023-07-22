"""empty message

Revision ID: 750a8606c5df
Revises: 5d0b72f6a2d8
Create Date: 2023-07-21 23:11:34.178136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '750a8606c5df'
down_revision = '5d0b72f6a2d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kredit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('desk1', sa.String(length=255), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.Column('a1', sa.String(length=50), nullable=False),
    sa.Column('a11', sa.String(length=50), nullable=False),
    sa.Column('a2', sa.String(length=50), nullable=False),
    sa.Column('a22', sa.String(length=50), nullable=False),
    sa.Column('a3', sa.String(length=50), nullable=False),
    sa.Column('a33', sa.String(length=50), nullable=False),
    sa.Column('a4', sa.String(length=50), nullable=False),
    sa.Column('a44', sa.String(length=50), nullable=False),
    sa.Column('desk2', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('xeber',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('time', sa.String(length=50), nullable=False),
    sa.Column('desk', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('xeber')
    op.drop_table('kredit')
    # ### end Alembic commands ###
