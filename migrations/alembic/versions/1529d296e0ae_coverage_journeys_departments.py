"""coverage_journeys_departments

Revision ID: 1529d296e0ae
Revises: 2dc7abaa8047
Create Date: 2017-03-16 11:57:23.281634

"""

# revision identifiers, used by Alembic.
revision = '1529d296e0ae'
down_revision = '26cb07c8ace'

from alembic import op
import sqlalchemy as sa
import config
from migrations.utils import get_create_partition_sql_func, get_drop_partition_sql_func, \
    get_create_trigger_sql, get_drop_table_cascade_sql


table = "coverage_journeys_departments"
schema = config.db['schema']


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(table, sa.Column('request_date', sa.DateTime(), nullable=False),
                    sa.Column('region_id', sa.Text(), nullable=False),
                    sa.Column('is_internal_call', sa.SmallInteger(), nullable=False),
                    sa.Column('departure_department_code', sa.Text(), nullable=False),
                    sa.Column('arrival_department_code', sa.Text(), nullable=False),
                    sa.Column('nb_req', sa.BigInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('request_date', 'region_id', 'is_internal_call',
                                            'departure_department_code', 'arrival_department_code'),
                    schema=schema)

    op.execute(get_create_partition_sql_func(schema, table))
    op.execute(get_create_trigger_sql(schema, table))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(get_drop_table_cascade_sql(schema, table))
    op.execute(get_drop_partition_sql_func(table))
    # ### end Alembic commands ###
