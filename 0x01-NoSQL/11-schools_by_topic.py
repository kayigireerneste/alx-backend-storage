#!/usr/bin/env python3
'''a Python function that returns the list of school having a specific topic
'''


def top_students(mongo_collection):
    '''Prints all students in a collection sorted by average score.
    '''
    students = mongo_collection.aggregate(
        [
            {
                '$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,
                },
            },
            {
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return students
