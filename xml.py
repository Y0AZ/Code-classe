import random

def xml(tag, content=None, **attr) :
    attr_str=""
    for key, value in attr.items():
        attr_str+=", "+key+"="+str(value)
    if content is None:
        content=""
    return "<"+tag+attr_str+">"+content+"</"+tag+">"

    
#print (xml("voiture", "moto", a=2, train=5))
#print (xml())

def create_password_generateur(template):
    def password_length(n):
        password=""
        for i in range(n):
            password+=random.choice(template)
        return password
    return password_length

alpha_password = create_password_generateur("vigilant")
#print(alpha_password(15))

def calculate_tax(price, city, hour):
    if hour<24:
        taux=float(hour/24)
    else:
        return "l'heure n'est pas dans le format 24H"
    
    dic={"Nord":60/100, "Sud":70/100, "Est":50/100, "Ouest":40/100}
    for key in dic.keys():
        if city==key:
            tax=dic[city]*price*taux
        #else : return "provinces introuvable"
    
    return tax

print(calculate_tax(800,"Nord", 21))