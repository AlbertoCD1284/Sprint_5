"""
create table datos_producto
date created: 2021-10-30 03:45:02.730493
"""


def upgrade(migrator):
    with migrator.create_table('datos_producto') as table:
        table.text('codigo', unique=True)
        table.text('marca')
        table.text('nombre')
        table.text('color')
        table.text('procesador')
        table.text('stock_Requerido')
        table.text('stock_Actual')
        table.foreign_key('TEXT', 'nit_proveedor_id', on_delete=None, on_update=None, references='datos_proveedor.nit')


def downgrade(migrator):
    migrator.drop_table('datos_producto')
