"""empty message

Revision ID: 497e5d7c61b9
Revises: 7fa1ba2215cb
Create Date: 2019-07-22 14:50:15.065352

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '497e5d7c61b9'
down_revision = '7fa1ba2215cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('billing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total_bill', sa.String(length=255), nullable=False),
    sa.Column('date_create', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('car',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('brand_name', sa.String(length=255), nullable=False),
    sa.Column('model', sa.String(length=255), nullable=False),
    sa.Column('class_name', sa.String(length=255), nullable=False),
    sa.Column('gear_box', sa.String(length=255), nullable=False),
    sa.Column('door', sa.String(length=255), nullable=False),
    sa.Column('img', sa.String(length=255), nullable=False),
    sa.Column('fuel', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=999), nullable=False),
    sa.Column('price', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('date_create', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flask_dance_oauth',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('provider', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('token', sqlalchemy_utils.types.json.JSONType(), nullable=False),
    sa.Column('provider_user_id', sa.String(length=256), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('provider_user_id')
    )
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('pick_date', sa.DateTime(), nullable=False),
    sa.Column('return_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['car_id'], ['car.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booking')
    op.drop_table('token')
    op.drop_table('flask_dance_oauth')
    op.drop_table('car')
    op.drop_table('user')
    op.drop_table('billing')
    # ### end Alembic commands ###
