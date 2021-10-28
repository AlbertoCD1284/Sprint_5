"""
create table datos_usuario
date created: 2021-10-28 23:15:42.074543
"""


def upgrade(migrator):
    with migrator.create_table('datos_usuario') as table:
        table.text('documento', null=True, unique=True)
        table.text('nombre')
        table.text('apellido')
        table.text('genero')
        table.text('direccion')
        table.text('email', unique=True)
        table.text('telefono')
        table.text('cel', unique=True)
        table.text('cargo')
        table.text('clave')


def downgrade(migrator):
    migrator.drop_table('datos_usuario')
