"""Invoice model."""

from datetime import UTC
from datetime import datetime
from uuid import uuid4

from advanced_alchemy.base import orm_registry
from advanced_alchemy.types import DateTimeUTC
from sqlalchemy import UUID
from sqlalchemy import Column
from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy import Table

# Define the table for the Invoice model
order_table = Table(
    # META
    # -----------------------------
    # Table name
    "orders",
    # Metadata
    orm_registry.metadata,
    # COLUMNS
    # -----------------------------
    # Unique identifier for the user.
    Column("id", UUID, default=uuid4, primary_key=True, autoincrement=False),
    # Order name
    Column("_name", String, nullable=False),
    Column("_name2", String, nullable=False),
    Column("_name3", String, nullable=False),
    # Order address
    Column("_address", String, nullable=False),
    # Date/time of instance creation.
    Column(
        "created_at",
        DateTimeUTC(timezone=True),
        default=datetime.now(UTC),
        nullable=False,
    ),
    # Date/time of instance last update.
    Column(
        "updated_at",
        DateTimeUTC(timezone=True),
        default=datetime.now(UTC),
        onupdate=datetime.now(UTC),
        nullable=False,
    ),
    # Request ID of the user who created the invoice.
    Column("request_id_created", UUID, unique=True, nullable=True, default=None),
    # PARAMS
    # -----------------------------
    # Atlas likes to import multiple times
    extend_existing=True,
)

# Create indexes
if not orm_registry.metadata.tables["orders"].indexes:
    Index("ix_orders_id", order_table.c.id)
    Index("ix_orders_created_at", order_table.c.created_at)
    Index("ix_orders_updated_at", order_table.c.updated_at)
    Index("ix_orders_request_id_created", order_table.c.request_id_created)
