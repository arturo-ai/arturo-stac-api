"""FastAPI application."""
from stac_fastapi.api.app import StacApi
from stac_fastapi.extensions.core import (
    FieldsExtension,
    QueryExtension,
    SortExtension,
    TransactionExtension,
)
from stac_fastapi.extensions.third_party import BulkTransactionExtension
from stac_fastapi.sqlalchemy.config import SqlalchemySettings
from stac_fastapi.sqlalchemy.core import CoreCrudClient
from stac_fastapi.sqlalchemy.session import Session
from stac_fastapi.sqlalchemy.transactions import (
    BulkTransactionsClient,
    TransactionsClient,
)

settings = SqlalchemySettings()
session = Session.create_from_settings(settings)
api = StacApi(
    settings=settings,
    extensions=[
        TransactionExtension(client=TransactionsClient(session=session)),
        BulkTransactionExtension(client=BulkTransactionsClient(session=session)),
        FieldsExtension(),
        QueryExtension(),
        SortExtension(),
    ],
    client=CoreCrudClient(session=session),
)
app = api.app


def run():
    """Run the app with uvicorn."""
    import uvicorn

    uvicorn.run(
        "stac_fastapi.sqlalchemy.app:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
        reload=True,
    )


if __name__ == "__main__":
    run()
