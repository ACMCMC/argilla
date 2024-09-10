#  Copyright 2021-present, the Recognai S.L. team.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import List
from datetime import datetime

from rq.job import Job
from sqlalchemy.ext.asyncio import AsyncSession

from argilla_server.models import Response
from argilla_server.jobs.webhook_jobs import enqueue_notify_events
from argilla_server.api.schemas.v1.responses import Response as ResponseSchema
from argilla_server.api.webhooks.v1.enums import ResponseEvent


async def notify_response_event(db: AsyncSession, response_event: ResponseEvent, response: Response) -> List[Job]:
    return await enqueue_notify_events(
        db,
        event=response_event,
        timestamp=datetime.utcnow(),
        data=ResponseSchema.from_orm(response).dict(),
    )