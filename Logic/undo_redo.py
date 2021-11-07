def do_undo(undo_list: list, redo_list: list, current_list: list):
    """
    copiaza in lista de undo primul obiect din lista curenta
    :param current_list: lista curenta
    :param undo_list: lista de undo
    :param redo_list: lista de redo
    :return:
    """
    if undo_list:
        top_undo = undo_list.pop()  # acceseaza primul obiect din lista de undo
        redo_list.append(current_list)  # puteam scrie si top_undo dar daca lista de redo este goala atunci la primul
        # redo nu se va executa nimic
        return top_undo

    return None


def do_redo(undo_list: list, redo_list: list, current_list: list):
    """
    copiaza in lista de redo primul obiect din lista curenta
    :param current_list: lista curenta
    :param undo_list: lista de undo
    :param redo_list:lista de redo
    :return:
    """
    if redo_list:
        top_redo = redo_list.pop()  # acceseaza primul obiect din lista de redo
        undo_list.append(current_list)  # puteam scrie si top_redo dar daca lista de undo este goala atunci la primul
        # redo nu se va executa nimic
        return top_redo

    return None
