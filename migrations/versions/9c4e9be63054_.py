"""empty message

Revision ID: 9c4e9be63054
Revises: f34030dc7a29
Create Date: 2019-07-17 16:37:10.018352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c4e9be63054'
down_revision = 'f34030dc7a29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car', sa.Column('fuel', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('car', 'fuel')
    # ### end Alembic commands ###
