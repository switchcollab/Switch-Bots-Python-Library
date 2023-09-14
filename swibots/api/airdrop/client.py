import swibots
from swibots.base import SwitchRestClient
from swibots.config import get_config
from .controllers import TournamentController


class AirdropClient(SwitchRestClient):
    def __init__(
        self,
        app: "swibots.App" = None,
        base_url: str = None,
    ):
        base_url = base_url or get_config()["AIRDROP_SERVICE"]["BASE_URL"]
        super().__init__(app, base_url)

        self._tournament: TournamentController = None

    @property
    def tournament(self) -> TournamentController:
        """Get the controller"""
        if self._tournament is None:
            self._tournament = TournamentController(self)
        return self._tournament

    def prepare_request_headers(self, headers: dict) -> dict:
        headers = super().prepare_request_headers(headers)
        if self.token is not None:
            headers["authtoken"] = f"{self.token}"
        return headers
