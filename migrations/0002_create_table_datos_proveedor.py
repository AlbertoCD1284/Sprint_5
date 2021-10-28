"""
create table datos_proveedor
date created: 2021-10-28 22:57:01.391396
"""


def upgrade(migrator):
    with migrator.create_table('datos_proveedor') as table:
        table.text('nit', unique=True)
        table.text('nombre')
        table.text('direccion')
        table.text('email', unique=True)
        table.text('telefono')
        table.text('celular', unique=True)


def downgrade(migrator):
    migrator.drop_table('datos_proveedor')
