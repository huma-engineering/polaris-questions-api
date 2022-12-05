"""empty message

Revision ID: 1737fb34d6b6
Revises: 05e8dc6ab571
Create Date: 2018-02-28 13:58:54.912462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1737fb34d6b6'
down_revision = '05e8dc6ab571'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('survey', sa.Column('completed', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('survey', 'completed')
    # ### end Alembic commands ###