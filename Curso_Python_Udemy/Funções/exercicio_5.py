def ler_texto (a):
    
    if len(a) >= 20:
        return "muito longo", len(a)
    else:
        return "muito curto",len(a)
    

print(ler_texto("Este é um texto de base"))

