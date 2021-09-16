from typing import Any, List, Optional


def make_table(
    rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False
) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.

    Chars that can be used as borders: │ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘
    # <++>
    """

    rows = list_to_str(rows, 2)
    if labels != None:
        labels = list_to_str(labels, 1)

    num_of_cols = len(rows[0])
    longest_str = []

    i = 0

    while i < num_of_cols:
        longest_str.append(0)
        i += 1

    for j in rows:

        k = 0
        while k < num_of_cols:
            if len(j[k]) > longest_str[k]:
                longest_str[k] = len(str(j[k]))
            if labels != None:
                if len(labels[k]) > longest_str[k]:
                    longest_str[k] = len(str(labels[k]))
            k += 1

    z = 0

    top = "┌"
    mid = "├"
    bot = "└"
    if centered == False:
        while z < len(longest_str):
            top += "─" * (longest_str[z] + 2) + "┬"
            bot += "─" * (longest_str[z] + 2) + "┴"
            mid += "─" * (longest_str[z] + 2) + "┼"
            z += 1
    else:
        while z < len(longest_str):
            top += "─" * (longest_str[z] + 2) + "┬"
            bot += "─" * (longest_str[z] + 2) + "┴"
            mid += "─" * (longest_str[z] + 2) + "┼"
            z += 1

    top = top[0:-1] + "┐"
    bot = bot[0:-1] + "┘"
    mid = mid[0:-1] + "┤"

    table = ""

    table += top + "\n"
    if labels != None:
        table += "│ "
        u = 0
        while u < len(longest_str):
            if centered == True:
                table += labels[u].center(longest_str[u]) + " │ "
            else:
                table += labels[u] + (" " * (longest_str[u] - len(labels[u]))) + " │ "
            u += 1
        table = table[0:-1]
        table += "\n"
        table += mid + "\n"


    for l in rows:
        table += "│ "
        m = 0
        while m < len(longest_str):
            if centered == True:
                table += l[m].center(longest_str[m]) + " │ "
            else:
                table += l[m].ljust(longest_str[m]) + " │ "
            m += 1
        table = table[0:-1]
        table += "\n"
    table += bot + "\n"
    # print(table)
    return table


def list_to_str(l, dim):
    def conv_sub_list(i):
        for j in i:
            return list(map(str, i))

    if dim == 2:
        str_list = []
        for i in l:
            str_list.append(conv_sub_list(i))

        return str_list

    str_list = []
    if dim == 1:
        str_list.append(conv_sub_list(l))

        return str_list[0]
