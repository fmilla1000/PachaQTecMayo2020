"""empty message

Revision ID: 0f6f4efdddcd
Revises: ae7bc6b9d1b3
Create Date: 2020-08-04 19:58:49.408000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f6f4efdddcd'
down_revision = 'ae7bc6b9d1b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=True),
    sa.Column('ruc', sa.Integer(), nullable=True),
    sa.Column('direccion', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cliente_direccion'), 'cliente', ['direccion'], unique=False)
    op.create_index(op.f('ix_cliente_nombre'), 'cliente', ['nombre'], unique=False)
    op.create_table('compra',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('correlativo', sa.Integer(), nullable=True),
    sa.Column('subtotal', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('igv', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('total', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.Column('fecha', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['cliente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_compra_fecha'), 'compra', ['fecha'], unique=False)
    op.create_table('detalle_compra',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('precio', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('subtotal', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('compra_id', sa.Integer(), nullable=True),
    sa.Column('producto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['compra_id'], ['compra.id'], ),
    sa.ForeignKeyConstraint(['producto_id'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('detalle_compra')
    op.drop_index(op.f('ix_compra_fecha'), table_name='compra')
    op.drop_table('compra')
    op.drop_index(op.f('ix_cliente_nombre'), table_name='cliente')
    op.drop_index(op.f('ix_cliente_direccion'), table_name='cliente')
    op.drop_table('cliente')
    # ### end Alembic commands ###
