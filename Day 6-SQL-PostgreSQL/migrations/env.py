
import os

from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context

from app.database import Base, engine
from app import models


# Alembic configuration
config = context.config

# Configure logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# Use SQLAlchemy model metadata
target_metadata = Base.metadata


# Use the same secure database URL as the application
config.set_main_option(
    "sqlalchemy.url",
    os.getenv("DATABASE_URL", "").replace("%", "%%")
)


def run_migrations_offline() -> None:
    """Run migrations without a database connection."""

    url = os.getenv("DATABASE_URL")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations using a database connection."""

    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
