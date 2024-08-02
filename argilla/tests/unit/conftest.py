# Copyright 2024-present, Argilla, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pytest

import argilla as rg


# @pytest.fixture(scope="function", autouse=True)
# def mock_httpx_client(mocker) -> Generator[httpx.Client, None, None]:
#     mock_client = mocker.Mock(httpx.Client)
#     argilla.DEFAULT_HTTP_CLIENT = mock_client

#     return mock_client


@pytest.fixture(autouse=True)
def mock_client():
    # TODO: Mock the http layer
    client = rg.Argilla(api_url="http://test_url", api_key="mock")
    return client
