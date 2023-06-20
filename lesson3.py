base_random = [1, 4543534, 64565, 3, 45, 'david', 'inna', 456, 'word']
print(base_random)

control = input('Введіть логін і пароль адміна: ').split()

while control[0] == 'a' and control[1] == 'p':
    ch = input('Виберіть дію: append, extend, insert, index,count, sort, reverse, pop, remove, len, set, clear: ')
    ch_index = int(input('Виберіть індекс: '))
    typ = input('Виберіть тип даних int or str?: ')
    if typ == 'str':
        ch_el = input('Напишіть елемент: ')
    elif typ == 'int':
        ch_el = int(input('Напишіть елемент: '))
    for i in base_random:
         if i == ch_el:
             print('e')
             que = input('dali?')
    while ch == 'append' and typ == 'str':
        if i != ch_el or que == 'y':
            base_random.append(ch_el)
            base_random.insert(ch_index, ch_el)
            print(base_random)
            break
        break
    while ch == 'append' and typ == 'int':
        if i != ch_el or que == 'y':
            #ch_el = int(ch_el)
            base_random.append(ch_el)
            base_random.insert(ch_index, ch_el)
            print(base_random)
            break
    while ch == 'insert' and typ == 'str':
        base_random.insert(ch_index, ch_el)
        print(base_random)
        break
    while ch == 'insert' and typ == 'int':
        #ch_el = int(ch_el)
        base_random.insert(ch_index, ch_el)
        print(base_random)
        break
    while ch == 'index' and typ == 'str':
        print(base_random.index(ch_el)) #якщо є повтореня елементу, то шукає індекс тільки першого#
        break
    while ch == 'index' and typ == 'int':
        print(base_random.index(ch_el))
        break
    while ch == 'sort':
        base_random.sort(key=str, reverse=True)
        #print(sorted(map(str, base_random), reverse=True)) #працює так само#
        print(base_random)
        break
    while ch == 'reverse':
        #base_random.sort(reverse=True)
        print(list(reversed(base_random)))
        break
    while ch == 'extend' and typ == 'str':
        ch_el = [[str(ch_el)]]
        base_random.extend(ch_el)
        print(base_random)
        break
    while ch == 'extend' and typ == 'int':
        ch_el = [[int(ch_el)]]
        base_random.extend(ch_el)
        print(base_random)
        break
    while ch == 'count':
        a = base_random.count(ch_el)
        print(a)
        break
    while ch == 'pop':
        print(base_random.pop())
        print(base_random)
        break
    while ch == 'remove':
        print(base_random.remove(ch_el))
        print(base_random)
        break
    while ch == 'len':
        print(len(base_random))
        break
    while ch == 'set':
        print(set(base_random))
        break
    while ch == 'clear':
        print(base_random.clear())
        print(base_random)
        break
    
    
         
    



    

                    
                
        
    
