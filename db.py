from bson import ObjectId
from pymongo import database
from typing import List, Dict


def get_courses(connection: database) -> List[Dict[str, str]]:
    return list(connection.Courses.find())

def get_course(connection: database, course_id: str) -> Dict:
    course: Dict = connection.Courses.find_one({"_id": ObjectId(course_id)})
    course["lessons"]: List = list(connection.Lessons.find({"course_id": ObjectId(course["_id"])}))
    return course

def get_products(connection: database) -> List[Dict]:
    return list(connection.Products.find())