"""add resource type to embed token

Revision ID: 23ea52e6d784
Revises: ceb00d7ff3bd
Create Date: 2020-02-12 09:29:31.592426

"""
from alembic import op
import sqlalchemy as sa

from meltano.api.models.embed_token import ResourceType


# revision identifiers, used by Alembic.
revision = '23ea52e6d784'
down_revision = 'ceb00d7ff3bd'
branch_labels = None
depends_on = None

Session = sa.orm.sessionmaker()


def upgrade():
    op.add_column("embed_tokens", sa.Column("resource_type", sa.String()))

    metadata = sa.MetaData(bind=op.get_bind())
    session = Session(bind=op.get_bind())
    Embed_Tokens = sa.Table("embed_tokens", metadata, autoload=True)

    for embed_token in session.query(Embed_Tokens):
        embed_token.resource_type = ResourceType.REPORT

    session.commit()


def downgrade():
    op.drop_column("embed_tokens", "resource_type")
