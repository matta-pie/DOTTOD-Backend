"""add_response_id_to_piece

Revision ID: 59bb29bfa3e4
Revises: cbbeaf1fd7ff
Create Date: 2022-08-22 08:10:27.029699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59bb29bfa3e4'
down_revision = 'cbbeaf1fd7ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('piece', sa.Column('tweet_response_id', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('piece', 'tweet_response_id')
    # ### end Alembic commands ###