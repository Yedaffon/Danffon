# coding=utf-8
# Copyright 2020 Yedaffon Author.
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

from DFTensorFlow.DFASR.BaiDuAPI.mysql_helper import MysqlHelper

import socket

from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode

import numpy as np
import requests
import json
import sys
import base64
import time

import pymysql

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
socket.setdefaulttimeout(20)

APPID = "19419101"
API_KEY = 'xQM69KK214IOUm9sutj4NiIP'
SECRET_KEY = 'QWzFa2lKrw9FoMdEYfZpnXXioFxgYwvI'


class DemoError(Exception):
    pass


TOKEN_URL = "https://openapi.baidu.com/oauth/2.0/token"

SCOPE = "brain_asr_async"


def fetch_token():
    params = {"grant_type": "client_credentials",
              "client_id": API_KEY,
              "client_secret": SECRET_KEY}
    post_data = urlencode(params)
    post_data = post_data.encode("utf-8")
    req = Request(TOKEN_URL, post_data,)

    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print("token http response http code:" + str(err))
        result_str = err

    result_str = result_str.decode()
    result = json.loads(result_str)
    if ('access_token' in result.keys()) and ('scope' in result.keys()):
        if SCOPE not in result['scope'].split(' '):
            raise DemoError('scope is not correct')
        return result['access_token']
    else:
        raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: '
                        'access_token or scope not found in token response')


def create_task(prd):
    speech_url_list = []
    task_ids = {}
    for i in prd:
        speech_url_list.append(i[3].strip())

    for i in range(len(speech_url_list)):
        url = 'https://aip.baidubce.com/rpc/2.0/aasr/v1/create'

        body = {
            "speech_url": speech_url_list[i],
            "format": "mp3",        #音频格式，支持pcm,wav,mp3，音频格式转化可通过开源ffmpeg工具（https://ai.baidu.com/ai-doc/SPEECH/7k38lxpwf）或音频处理软件
            "pid": 1537,        #模型pid，1537为普通话输入法模型，1737为英语模型
            "rate": 16000       #音频采样率，支持16000采样率，音频格式转化可通过开源ffmpeg工具（https://ai.baidu.com/ai-doc/SPEECH/7k38lxpwf）或音频处理软件
        }

        token = {"access_token": fetch_token()}

        headers = {'content-type': "application/json"}

        response = requests.post(url,
                                 params=token,
                                 data=json.dumps(body),
                                 headers=headers,
                                 timeout=1)
        timeArray = time.localtime(int(prd[i][2]))
        time_style = time.strftime("%Y-%m-%d-%H-%M-%S", timeArray)
        filename = prd[i][1] + "_" + prd[i][0] + "_" + str(time_style)
        task_ids[eval(response.text)["task_id"]] = [filename, prd[i][1], prd[i][0], str(time_style)]
        response.close()

    return task_ids


def insert_txt(file_name, customer_tel, employee_id, date, text):
    dbutil = MysqlHelper()
    sql_key = "insert ignore into audio2text (`file_name`, `customer_tel`, `employee_id`, `date`, `text`) value " \
              "(%s, %s, %s, %s, %s)"
    dbutil.inset(sql_key, (file_name, customer_tel, employee_id, date, text))


def query_result(task_ids_list: dict):
    for task_id in task_ids_list.keys():
        url = "https://aip.baidubce.com/rpc/2.0/aasr/v1/query"

        body = {
            "task_ids": [task_id],
        }

        token = {"access_token": fetch_token()}

        headers = {'content-type': "application/json"}

        while True:
            response = requests.post(url,
                                     params=token,
                                     data=json.dumps(body),
                                     headers=headers,
                                     timeout=1)
            if response.status_code == 200:
                response.close()
                break
            else:
                print("连接断开, 正在重连中....")
                response.close()
                time.sleep(10)
        results = json.dumps(response.json(), ensure_ascii=False)

        # results = results.split("\n")
        # for result in results:

        try:
            result = eval(results)
            # print(result)
            res = result["tasks_info"][0]["task_result"]["detailed_result"]
            res_task_id = result["tasks_info"][0]["task_id"]
            tmysql = task_ids_list[res_task_id]
            out = ""
            for i in range(len(res)):
                if i % 2 == 0:
                    out += "|$:" + '"' + res[i]["res"][0] + '"'
                else:
                    out += "|&:" + '"' + res[i]["res"][0] + '"'

            insert_txt(tmysql[0], int(tmysql[1]), int(tmysql[2]), tmysql[3], text=out)
            return "success"
        except Exception as e:
            print("error")
            return "error"


if __name__ == '__main__':
    with open("phone_record.txt", "r", encoding="utf-8") as fr:
        PRD = [i.split("\t") for i in fr]
    task_list = []
    num = 0
    for pred in PRD[785:]:
        try:
            task_ids_list = create_task([pred])
            time.sleep(40)
            re_err = query_result(task_ids_list)
            if re_err == "success":
                num += 1
                print("success: %d" % num)
                time.sleep(3)
            else:
                with open('task.txt', 'a', encoding="utf-8") as f:
                    f.write(str(task_ids_list) + "\n")
                    time.sleep(3)
        except Exception as e:
            print("final error")
            time.sleep(3)
