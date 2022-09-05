"""init db

Revision ID: 6692a1f9316b
Revises: 
Create Date: 2022-09-04 16:29:46.497722

"""
from alembic import op
import sqlalchemy as sa
from app2.app.api.entity1.category_enum import Category



# revision identifiers, used by Alembic.
revision = '6692a1f9316b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'product',
        sa.Column("id", sa.String, primary_key=True),
        sa.Column("created", sa.DateTime),
        sa.Column("updated", sa.DateTime, nullable=False),
        sa.Column("name", sa.String, nullable=False, unique=False),
        sa.Column("price", sa.String, nullable=True, unique=False),
        sa.Column("category", sa.Enum(Category), nullable=False, unique=False),
        sa.Column("quantity", sa.String, nullable=True, unique=False),
        sa.Column("added_user_id",sa.String, nullable=False),

    )


def downgrade():
    op.drop_table('product')

