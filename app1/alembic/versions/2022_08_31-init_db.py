"""init db

Revision ID: dc0015ed558e
Revises: 07103a5d0de6
Create Date: 2022-08-31 16:05:04.179610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc0015ed558e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column("id",sa.String, primary_key=True),
        sa.Column("created",sa.DateTime),
        sa.Column("updated",sa.DateTime, nullable=False),
        sa.Column("username",sa.String, nullable=False, unique=True),
        sa.Column("hashed_password",sa.String, nullable=False),
        sa.Column("email",sa.String, nullable=True, unique=False),
        sa.Column("first_name",sa.String, nullable=True, unique=False),
        sa.Column("last_name",sa.String, nullable=True, unique=False),
        sa.Column("bio",sa.String, nullable=True, unique=False),
        sa.Column("nationality",sa.String, nullable=True, unique=False)

    )


def downgrade():
    op.drop_table('user')

