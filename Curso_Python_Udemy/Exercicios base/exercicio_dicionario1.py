dic = {
    "pneus": 4,
    "portas": 2,
    "motor": 1,
    "janelas": 4
}

print(dic)

dic["teto_solar"] = 1

print(dic)

del dic["motor"]
del dic["janelas"]

print(dic)