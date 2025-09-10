from fixtures.authenticated_fixtures import *
from schemas.user.user_schemas import *
from tools.assertions.base import assert_status_code
from tools.assertions.shema import validate_json_schema


class TestUsers:

    def test_get_user(self, authentications_client):
        user = authentications_client.get_user_api()
        schema = UserSchema.model_validate_json(user.text)
        assert_status_code(user.status_code, HTTPStatus.OK)
        validate_json_schema(instance=user.json(), schema=schema.model_json_schema())
