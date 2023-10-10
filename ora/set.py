def main():
    kosar = set(["alma", "citrom","ananász"])
    halmaz = set()
    szotar = {"elem", "alma"}
    szotar2 = {}
    print(type(szotar2))
    li = sorted(set([5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]))
    print(li)
    
    
    kosar.add("narancs")
    kosar.add("alma")
    print(kosar)
    
    kosar.union(szotar)
    kosar.intersection(szotar)
    kosar.difference(szotar)
    
    szotar ={} #kulcs-transzformációs tábla
    my_dic = {}
    my_dic['a'] = "alfa"
    my_dic['b'] = "beta"
    my_dic['g'] = "gamma"
    my_dic['o'] = "omega"
    my_dic['d'] = "delta"
    print(len(my_dic))
    print(my_dic)
    print(my_dic.get('what'))    
    print(my_dic.get('what','not found')) 
    #szotar.get(kulcs, ertek): a kulcson szereplo erteket adja meg, ha nincs ilyen kulcs, akkor erteket ad vissza
    dd = dict()
    print(type(dd.keys()))
    print(type(dd.values()))
    
    for k in sorted(my_dic.keys()):
        print(k, "------>", my_dic[k])
    
    print(my_dic.items())
    
    for k,v in my_dic.items():
        print(k, v)
    
    #del li[1] # kitorli az 1-es indexu erteket
    del my_dic['a']
    print(my_dic)

if __name__ == "__main__":
    main()