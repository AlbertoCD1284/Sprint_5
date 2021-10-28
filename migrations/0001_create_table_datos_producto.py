"""
create table datos_producto
date created: 2021-10-26 20:10:56.099370
"""


def upgrade(migrator):
    with migrator.create_table('datos_producto') as table:
        table.text('codigo', unique=True)
        table.text('marca')
        table.text('nombre')
        table.text('color')
        table.text('procesador')


def downgrade(migrator):
    migrator.drop_table('datos_producto')
