from .db_utils import *
from .constmap import *
from .requests import *

from typing import List, Dict, Tuple
from datetime import datetime
import json
import time
import logging
import logging.config

data = json.load(open('../config/logging.json', 'r+'))
logging.config.dictConfig(data)
logger = logging.getLogger("crawl_logger")
errors = logging.getLogger("error_logger")

auth = json.load(open('/home/ec2-user/chotot_estate/resource/db_prime.json', 'r+'))
engine = db_engine(auth)

def crawl_job(category) -> Dict[str, Tuple[str, int]]:
    link = url.format(category)
    res = request_api(link)
    return res

def insert_post_property(table_name: str, table_cols: tuple, info: Tuple):
    query = f"insert into {table_name} ({','.join(table_cols)}) values {info} on conflict do nothing"
    execute_query_commit(engine, query)


def process_info(result: dict, table_name: dict) -> dict:
    if table_name == 'dates':
        time = int2timestamp(result['list_time'])
        info = [result['list_time'], time2str(time), time2str(time.date()), time.day, time.month, time.year]
    elif table_name == 'shop_profile':
        info = [result['shop'][k] for k in table_info[table_name]]
        info[0] = time2str(int2timestamp(info[0]))
    elif table_name == 'property_info':
        info = [result[k] if k in result else '' for k in table_info[table_name]]
        info.append(info[4]/info[6]*1000)
        if 'shop' in result:
            info.append(result['shop']['alias'])
        else:
            info.append('')
    else:
        info = [result[k] if k in result else '' for k in table_info[table_name]]
    return tuple(info)


def int2timestamp(time: int):
    return  datetime.utcfromtimestamp(time/ 1e3)

def time2str(time: datetime) -> str:
    return time.strftime('%Y-%m-%d %H:%M:%S.%f')

def pipeline_one_cate(category: int):
    ##crawl 100 newest results for every category:
    results = crawl_job(category)
    logger.info(f'Crawl {category} -------------------------')
    for result in results['ads']:
        for table_name, table_cols in tables.items():
            if table_name == 'shop_profile' and 'shop' not in result:
                continue
            try:
                info = process_info(result, table_name)
                insert_post_property(table_name, table_cols, info)
                logger.info(f'Successully insert {table_name}')
            except Exception as e:
                errors.error(f'Fail to insert {table_name} with error {e}')
                pass







    
    