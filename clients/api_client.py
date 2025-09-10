from typing import Any

from httpx import Client, Response, QueryParams
from httpx._types import URLTypes, RequestData, RequestFiles

from configs.config import DataUser


class ApiClient:

    def __init__(self, client: Client):
        self.client = client

    @property
    def headers(self) -> dict[str, str]:
        headers = {"Content-Type": "application/json"}
        token = DataUser.user_token()
        if token:
            headers["x-auth-token"] = token
        return headers

    def get(self,
            url: URLTypes,
            params: QueryParams | None = None
            ) -> Response:
        return self.client.get(url, headers=self.headers, params=params)

    def post(self,
             url: URLTypes,
             params: QueryParams | None = None,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None
             ) -> Response:
        return self.client.post(url, headers=self.headers, params=params, json=json, files=files, data=data)

    def put(self,
            url: URLTypes,
            params: QueryParams | None = None,
            json: Any | None = None,
            data: RequestData | None = None,
            files: RequestFiles | None = None
            ) -> Response:
        return self.client.put(url, headers=self.headers, params=params, json=json, files=files, data=data)

    def patch(self,
              url: URLTypes,
              params: QueryParams | None = None,
              json: Any | None = None,
              data: RequestData | None = None,
              files: RequestFiles | None = None
              ) -> Response:
        return self.client.patch(url, headers=self.headers, params=params, json=json, files=files, data=data)

    def delete(self,
               url: URLTypes,
               params: QueryParams | None = None,
               ) -> Response:
        return self.client.delete(url, headers=self.headers, params=params)
