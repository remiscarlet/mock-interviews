# Name, job, age tables - datastores
# "find me all engineers' names"
# "All people younger than X age"

from typing import Tuple, List, Dict
# Table
# CRUD

#db_schema = {
  # "table_name": ("col1", "col2", "etc"),
  # "etc": ()
#}
db = {
  # "table_name": [
  #     (val1, val2, val3, etc),
  #     etc
  # ]
}

"""
{
    "foo": {
        0: {
            "name1": [0]
        }
    }
}
"""
indices = {
}

def insert(table_name: str, row_vals: Tuple):
    global indices, db
    if table_name not in db:
        db[table_name] = []
    elif len(db[table_name][0]) != len(row_vals):
        raise Exception("Received invalid number of vals in inserted row")

    db[table_name].append(row_vals)

    if table_name not in indices:
        return

    row_idx = len(db[table_name]) - 1
    for col_num in indices[table_name].keys():
        index_val = row_vals[col_num]
        if index_val not in indices[table_name][col_num]:
            indices[table_name][col_num][index_val] = []
        indices[table_name][col_num][index_val].append(row_idx)


def get(table_name: str, filter_expr) -> List[Tuple]:
    global indices, db

    rows = db[table_name]
    return list(filter(filter_expr, rows))

def getFast(table_name: str, col_num: int, col_vals: List) -> List[Tuple]:
    row_idxs = []
    for rows in (indices[table_name][col_num][col_val] for col_val in col_vals):
        row_idxs.extend(rows)
    return [db[table_name][row_idx] for row_idx in row_idxs]
    

def createIndex(table_name: str, col_num: int, reindex: bool = True):
    global indices, db
    if table_name not in indices: 
        indices[table_name] = {}
    if col_num in indices[table_name]:
        return

    indices[table_name][col_num] = {} 

    if not reindex:
        return

    for idx, row in enumerate(db[table_name]):
        index_val = row[col_num]
        if index_val not in indices[table_name][col_num]:
            indices[table_name][col_num][index_val] = []
        indices[table_name][col_num][index_val].append(idx)


def main():
    insert("name", ("alex", "engineer", 25))
    insert("name", ("alex", "engineer", 22))
    insert("name", ("alexa", "engineer", 30))
    insert("name", ("alexa", "chemist", 30))
    insert("name", ("bob", "middle manager", 30))
    try:
        insert("name", (1,2))
    except:
        print("Okay")
    
    createIndex("name", 0, reindex=True)
    createIndex("name", 1, reindex=True)

    vals = getFast("name", 1, ["engineer"]) 
    print(vals)

    vals = getFast("name", 1, ["chemist"]) 
    print(vals)

    insert("name", ("claire", "chemist", 55))
    
    vals = getFast("name", 1, ["chemist"]) 
    print(vals)

if __name__ == "__main__":
    main()
