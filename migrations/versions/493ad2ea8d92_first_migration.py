"""first migration

Revision ID: 493ad2ea8d92
Revises: 
Create Date: 2022-09-12 07:47:54.571643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '493ad2ea8d92'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=150), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('drone',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('camera_quality', sa.String(length=150), nullable=True),
    sa.Column('flight_time', sa.String(length=100), nullable=True),
    sa.Column('max_speed', sa.String(length=100), nullable=True),
    sa.Column('dimensions', sa.String(length=100), nullable=True),
    sa.Column('weight', sa.String(length=100), nullable=True),
    sa.Column('cost_of_production', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('series', sa.String(length=150), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('drone')
    op.drop_table('user')
    # ### end Alembic commands ###
