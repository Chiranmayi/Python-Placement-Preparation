
"""create database models

Revision ID: 15a8762c87a3
Revises:
Create Date: 2026-10-31 18:27:41.062096

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15a8762c87a3'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Existing tables and indexes were created using SQL scripts.
    # No schema changes are required in this migration.
    pass


def downgrade() -> None:
    """Downgrade schema."""
    # No changes were made, so nothing needs to be reversed.
    pass
