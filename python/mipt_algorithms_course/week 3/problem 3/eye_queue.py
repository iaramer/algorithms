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


class AIDequeue:

    def __init__(self, init_len=100):
        self.length = 0
        self.array = [None] * init_len
        self.head = None
        self.tail = None

    def __len__(self) -> int:
        return self.length

    def len(self) -> int:
        return self.length

    def append(self, element) -> None:
        if self.length == 0:
            self.array[0] = element
            self.head = self.tail = 0
        else:
            if self.tail + 1 < len(self.array):  # don't need to do a circle
                if self.tail + 1 == self.head:
                    self.array = self.array[:self.head] \
                        + [None] * len(self.array) \
                        + self.array[self.head:]  # O(N)
                    self.head += len(self.array) // 2
                self.tail += 1
            else:  # need to do a circle
                if 0 == self.head:
                    self.array = [None] * len(self.array) + self.array  # O(N)
                    self.head += len(self.array) // 2
                self.tail = 0
        self.array[self.tail] = element
        self.length += 1

    def push_front(self, element) -> None:
        if self.length == 0:
            self.head = self.tail = 0
        else:
            if self.head - 1 >= 0:  # don't need to do a circle
                if self.head - 1 == self.tail:
                    self.array = self.array[:self.head] \
                        + [None] * len(self.array) \
                        + self.array[self.head:]  # O(N)
                    self.head += len(self.array) // 2
                self.head -= 1
            else:  # need to do a circle
                if len(self.array) - 1 == self.tail:
                    self.array += [None] * len(self.array)  # O(N)
                self.head = len(self.array) - 1
        self.array[self.head] = element
        self.length += 1

    def popleft(self):
        if self.length == 0:
            return None
        el = self.array[self.head]
        if self.head == len(self.array) - 1:
            self.head = 0
        else:
            self.head += 1
        self.length -= 1
        return el

    def insert(self, idx, element) -> None:
        if self.length == 0:
            self.append(element)
        elif idx == 0:
            self.push_front(element)
        elif self.length == 1:
            self.append(element)
        elif self.head < self.tail:
            self.array.insert(self.head + idx, element)
            self.tail += 1
            self.length += 1
        elif self.head > self.tail:
            self.array = self.array[self.head:] + self.array[:self.tail + 1]
            self.head = 0
            self.tail = len(self.array)  # self.tail+=1 already included
            self.array.insert(self.head + idx, element)
            self.length += 1


def func(events, n_shops):
    ans = list()
    inl = 30000  # 30k is the best option for now, 51 gives ML
    # inl = 1
    shops = [AIDequeue(init_len=inl) for _ in range(n_shops)]
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
                shops[id_shop].insert(new_idx, id_p)  # O(N)
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

    print('OK')
