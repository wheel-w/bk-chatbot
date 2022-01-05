"""
TencentBlueKing is pleased to support the open source community by making
蓝鲸智云PaaS平台社区版 (BlueKing PaaSCommunity Edition) available.
Copyright (C) 2017-2018 THL A29 Limited,
a Tencent company. All rights reserved.
Licensed under the MIT License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

import time

from opsbot import CommandSession
from component import JOB, RedisClient


class Flow:
    def __init__(self, session: CommandSession):
        self._session = session
        self._job = JOB()
        self._redis_client = RedisClient(env='prod')
        if self._session.ctx['msg_from_type'] == 'single':
            self.biz_id = self._redis_client.hash_get("chat_single_biz", self._session.ctx['msg_sender_id'])
        else:
            self.biz_id = self._redis_client.hash_get("chat_group_biz", self._session.ctx['msg_group_id'])

    async def _get_job_plan_list(self):
        data = await self._job.get_job_plan_list()
        return data

    async def _get_job_plan_detail(self):
        data = await self._job.get_job_plan_detail()
        return data

    async def render_job_plan_list(self):
        if not self.biz_id:
            return None

        bk_job_plans = self._get_job_plan_list(bk_biz_id=self.biz_id)
        template_card = {
            'card_type': 'multiple_interaction',
            'main_title': {
                'title': '欢迎使用JOB平台',
                'desc': '请选择JOB执行方案'
            },
            'task_id': str(int(time.time() * 100000)),
            'select_list': [
                {
                    'question_key': 'bk_job_plan_id',
                    'title': '选择执行方案',
                    'option_list': [{'id': job_plan['id'], 'text': job_plan['name']}
                                    for job_plan in bk_job_plans.get('data', [])]
                }
            ],
            'submit_button': {
                'text': '提交',
                'key': 'select_bk_job_plan'
            }
        }
        return template_card

