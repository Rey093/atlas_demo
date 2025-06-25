-- Create "orders" table
CREATE TABLE "orders" (
  "id" uuid NOT NULL,
  "_name" character varying NOT NULL,
  "_address" character varying NOT NULL,
  "created_at" timestamptz NOT NULL,
  "updated_at" timestamptz NOT NULL,
  "request_id_created" uuid NULL,
  CONSTRAINT "pk_orders" PRIMARY KEY ("id"),
  CONSTRAINT "uq_orders_request_id_created" UNIQUE ("request_id_created")
);
-- Create index "ix_orders_created_at" to table: "orders"
CREATE INDEX "ix_orders_created_at" ON "orders" ("created_at");
-- Create index "ix_orders_id" to table: "orders"
CREATE INDEX "ix_orders_id" ON "orders" ("id");
-- Create index "ix_orders_request_id_created" to table: "orders"
CREATE INDEX "ix_orders_request_id_created" ON "orders" ("request_id_created");
-- Create index "ix_orders_updated_at" to table: "orders"
CREATE INDEX "ix_orders_updated_at" ON "orders" ("updated_at");
