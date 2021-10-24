from pymongo import database
from typing import List, Dict


def get_courses(connection: database) -> List[Dict[str, str]]:
    return list(connection.Courses.find())