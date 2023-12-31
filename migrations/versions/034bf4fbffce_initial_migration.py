"""initial migration

Revision ID: 034bf4fbffce
Revises: 
Create Date: 2023-10-28 20:04:28.919432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '034bf4fbffce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('label', sa.Integer(), nullable=False),
    sa.Column('manufacturer', sa.String(), nullable=False),
    sa.Column('model', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('engine', sa.String(), nullable=True),
    sa.Column('horsepower', sa.String(), nullable=True),
    sa.Column('torque', sa.String(), nullable=True),
    sa.Column('transmission', sa.String(), nullable=True),
    sa.Column('drivetrain', sa.String(), nullable=True),
    sa.Column('doors', sa.Integer(), nullable=True),
    sa.Column('seating_capacity', sa.Integer(), nullable=True),
    sa.Column('fuel_type', sa.String(), nullable=True),
    sa.Column('fuel_capacity', sa.String(), nullable=True),
    sa.Column('fuel_consumption', sa.String(), nullable=True),
    sa.Column('weight', sa.String(), nullable=True),
    sa.Column('length', sa.String(), nullable=True),
    sa.Column('width', sa.String(), nullable=True),
    sa.Column('height', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('slug', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('label'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car')
    # ### end Alembic commands ###
