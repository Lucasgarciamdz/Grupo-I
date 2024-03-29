"""prueba

Revision ID: d773dce1e950
Revises: 
Create Date: 2023-10-29 17:38:19.439723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd773dce1e950'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('alumno', schema=None) as batch_op:
        batch_op.alter_column('estado',
               existing_type=sa.VARCHAR(length=45),
               nullable=True)
        batch_op.alter_column('altura',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('peso',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('clase', schema=None) as batch_op:
        batch_op.alter_column('tipo',
               existing_type=sa.VARCHAR(length=45),
               nullable=True)
        batch_op.drop_column('titulo')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('clase', schema=None) as batch_op:
        batch_op.add_column(sa.Column('titulo', sa.VARCHAR(length=45), nullable=False))
        batch_op.alter_column('tipo',
               existing_type=sa.VARCHAR(length=45),
               nullable=False)

    with op.batch_alter_table('alumno', schema=None) as batch_op:
        batch_op.alter_column('peso',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('altura',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('estado',
               existing_type=sa.VARCHAR(length=45),
               nullable=False)

    # ### end Alembic commands ###
