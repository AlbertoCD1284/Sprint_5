"""
create table datos_usuario
date created: 2021-10-26 20:10:56.104367
"""


def upgrade(migrator):
    with migrator.create_table('datos_usuario') as table:
        table.text('documento', unique=True)
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
