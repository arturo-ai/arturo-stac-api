"""context extension"""
import attr
from fastapi import FastAPI

from stac_api.api.extensions.extension import ApiExtension


@attr.s
class ContextExtension(ApiExtension):
    """
    stac-api context extension
    (https://github.com/radiantearth/stac-api-spec/blob/master/fragments/context/README.md)
    """

    def register(self, app: FastAPI) -> None:
        """register extension with the application"""
        pass
