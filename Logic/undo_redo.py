def do_undo(undo_list: list, redo_list: list, current_list: list):
    """

    :param current_list: lista curenta
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return:
    """
    if undo_list:
        top_undo = undo_list.pop()
        redo_list.append(current_list)
        return top_undo
    else:
        return None


def do_redo(undo_list: list, redo_list: list, current_list: list):
    """

    :param current_list: lista curenta
    :param undo_list: lista de undo
    :param redo_list:lista de redo
    :return:
    """
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(current_list)
        return top_redo
    else:
        return None
