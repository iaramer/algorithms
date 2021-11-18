"""
Компания Груша планирует старт продаж своего нового устройства «eyePhone Y». Поскольку очереди на старте продаж
устройств Компании бывают очень длинными, в этом году было придумано нововведение: Компанией были заранее проданы
сертификаты, которые позволяют покупателю отстоять не всю очередь, а только половину: владелец такого сертификата
имеет право встать в середину очереди, причём, если в очереди нечётное число человек, он встаёт перед центральным
человеком (дальше от магазина).

Конечно, такое поведение покупателей с сертификатами может вызвать недовольство, поэтому Компания просит Вас написать
программу, которая будет моделировать состояние очереди, дабы обеспечить честность процесса и избежать беспорядков.

У компании 0 ≤ N ≤ 100000 магазинов. Вам задана последовательность прихода и ухода покупателей в очередь в каждом
магазине, а так же запросы магазинов. Данные события обозначены символами:

`+' – покупатель без сертификата встал в очередь;
`!' – покупатель с сертификатом встал в очередь;
`?' – запрос от магазина, сколько в данный момент человек в очереди;
`-' – покупатель покинул очередь (совершил покупку и ушёл абсолютно счастливым обладателем нового устройства);
`#' – конец рабочего дня магазинов.

Выведите последовательность выхода покупателей из очереди и ответы на запросы магазинов.

Считается, что все владельцы сертификата воспользуются своей привилегией.

Формат ввода
На первой строке входного файла содержится единственное целое число 0 ≤ N ≤ 100000 – количество магазинов Компании,
которые необходимо отслеживать.

Следующие 0 ≤ M ≤ 100000 строк содержат события, которые нужно обрабатывать. Строка обозначающая i-е события
начинается с символа ci, который обозначает тип события в соответствии со списком приведённым выше.
Далее, для событий `+', `!', `?', `-', через пробел следует целое число 0 ≤ qi < N – номер магазина, к которому
относится данное событие. Далее, для событий типа `+' и `!' через пробел следует целое число idi — номер покупателя
вставшего в очередь (все покупатели нумеруются с нуля, нумерация общая по всем магазинам).

Формат вывода
Для каждого события типа `-', `?' выведите на отдельной строке одно целое число – ответ на запрос:
Для события типа `-' – номер покупателя, который покинет данный магазин в момент данного события.
Для события типа `?' – количество человек в очереди данного магазина в момент данного события.
"""


def read_cli(file):
    inputs = list()
    n_shops = None
    for line in open(file, 'r'):
        cmd = line.split()
        if len(cmd) == 1:
            if cmd[0].isdigit():
                n_shops = int(cmd[0])
            else:
                break
        elif len(cmd) == 2:
            inputs.append((cmd[0], int(cmd[1])))
        elif len(cmd) == 3:
            inputs.append((cmd[0], int(cmd[1]), int(cmd[2])))
    return inputs, n_shops


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class AIDeque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.mid = None
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.tail = temp
            self.mid = temp
        else:
            temp.next = self.tail
            self.tail.prev = temp
            self.tail = temp
            if self.mid is None:
                self.mid = self.head
            if self.size % 2 == 0:
                self.mid = self.mid.prev
        self.size += 1

    def popleft(self):
        if self.size == 0:
            return
        temp = self.head
        if self.size == 1:
            self.head = None
            self.mid = None
            self.tail = None
        else:
            if self.size % 2 == 0:
                if self.size == 3:
                    self.mid.next = None
                else:
                    self.mid = self.mid.prev
            self.head = self.head.prev
            if self.head is not None:
                self.head.next = None

        self.size -= 1
        return_val = temp.data
        del temp
        return return_val

    def insert_mid(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.mid = temp
            self.tail = temp
        elif self.size == 1:
            self.tail = temp
            # self.mid = self.head  # already
            self.head.prev = temp
            temp.next = self.head
        else:
            temp.prev = self.mid.prev
            temp.next = self.mid
            if self.mid.prev is not None:
                self.mid.prev.next = temp
            self.mid.prev = temp
            if self.size % 2 == 0:
                self.mid = temp
        self.size += 1


def func(events, n_shops):
    ans = list()
    shops = [AIDeque() for _ in range(n_shops)]
    for event in events:
        ev = event[0]
        id_shop = event[1]
        id_p = event[2] if len(event) > 2 else None
        if ev == '+':
            shops[id_shop].append(id_p)
        elif ev == '!':
            shops[id_shop].insert_mid(id_p)
        elif ev == '-':
            id_left = shops[id_shop].popleft()
            if id_left is not None:
                ans.append(id_left)
        elif ev == '?':
            ans.append(len(shops[id_shop]))
    return ans


def check(events, n_shops):
    from collections import deque
    ans = list()
    shops = [deque() for _ in range(n_shops)]
    for event in events:
        ev = event[0]
        id_shop = event[1]
        id_p = event[2] if len(event) > 2 else None
        if ev == '+':
            shops[id_shop].append(id_p)
        elif ev == '!':
            if len(shops[id_shop]) == 0:
                shops[id_shop].append(id_p)
            else:
                new_idx = len(shops[id_shop]) // 2 + len(shops[id_shop]) % 2
                shops[id_shop].insert(new_idx, id_p)
        elif ev == '-':
            ans.append(shops[id_shop].popleft())
        elif ev == '?':
            ans.append(len(shops[id_shop]))
    return ans


if __name__ == '__main__':
    res = func(*read_cli('ex1.txt'))
    act = [3, 0, 1, 1, 3, 2, 3, 4]
    assert res == act

    res = func(*read_cli('ex2.txt'))
    act = [0, 1, 2, 4, 3]
    assert res == act

    res = func(*read_cli('ex3.txt'))
    act = [0, 2, 1, 1, 5, 2, 3, 4]
    assert res == act

    res = func(*read_cli('ex4.txt'))
    act = check(*read_cli('ex4.txt'))
    assert res == act

    res = func(*read_cli('ex5.txt'))
    act = check(*read_cli('ex5.txt'))
    assert res == act

    res = func(*read_cli('ex6.txt'))
    act = [1, 3]
    assert res == act

    res = func(*read_cli('ex7.txt'))
    act = check(*read_cli('ex7.txt'))
    assert res == act

    print('OK')
