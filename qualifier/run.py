from qualifier import make_table


table = make_table(
   # rows=[
   #     ["Ducky Yellow", 3],
   #     ["Ducky Dave", 12],
   #     ["Ducky Tube", 7],
   #     ["Ducky Lemon", 1]
   # ],
   # labels=["Name", "Duckiness"],
    rows=[
        ["Lemon", 18_3285, "Owner"],
        ["Sebastiaan", 18_3285.1, "Owner"],
        ["KutieKatj", 15_000, "Admin"],
        ["Jake", "MoreThanU", "Helper"],
        ["Joe", -12, "Idk Tbh"]
    ],
    labels=["User", "Messages", "Role"],
   centered=True
)

print(table)
