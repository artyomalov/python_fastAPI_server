from const import OFFSET_SIZE, LIMIT


def get_todos_handler(find_arg, data_base, model, skip_counter):
    todo_base_query = data_base.query(model).order_by(model.id.desc())
    if find_arg != None:
        todos_response = todo_base_query \
            .filter(model.completed == find_arg) \
            .offset(skip_counter*OFFSET_SIZE) \
            .limit(LIMIT).all()
        return todos_response

    todos_response = todo_base_query.offset(
        skip_counter*OFFSET_SIZE).limit(LIMIT).all()

    return todos_response
