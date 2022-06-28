import sys

sys.path.insert(0, 'C:\dbconfig')  # DB 접속정보를 저장한 폴더 경로 c:\
import dbconfig as config  # DB 접속정보를 가져온다.


def get_db_info(db_name):
    return {"Maria": config.Maria, "Postgresql": config.Postgresql}.get(db_name, config.nodb)