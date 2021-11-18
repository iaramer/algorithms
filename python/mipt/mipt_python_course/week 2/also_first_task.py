"""
Also first task
The previous task was intentionally simplified. Usually I have more data about participants:

solutions = [
    {
        'date': '2021-01-01 10:00:00',
        'name': 'Brad Pitt',
        'email': 'Participant1@mail.com',
        'phone': '+7 912-345-67-89',
        'code': '...'
    },
    {
        'date': '2021-01-01 10:01:00',
        'name': 'Not Brad Pitt',
        'email': 'participant2@mail.com',
        'phone': '+7(912) 3456789',
        'code': '...'
    },
    {
        'date': '2021-01-01 10:02:00',
        'name': 'Definitely not Brad Pitt',
        'email': 'particiPANT1@mail.com',
        'phone': '79001234567',
        'code': '...'
    },
    ...
]

In that "solutions" list, all 3 solutions are from 1 person: 1st and 2nd have the same phone, 1st and 3rd have the
same email.

Now, try to improve your previous algorithm to handle several contact details from every lottery participant.

I rate this variant of task as difficult for newbies. That's why I strongly advise you to discuss this algorithm with
each other. Remember that it is good to ask and give help. But it is bad to copy code without understanding how it
works.
"""

# pip install phonenumbers
import phonenumbers


def func(sols):
    res = list()
    emails = set()
    phones = set()
    for sol in reversed(sols):
        phone = phonenumbers.parse(sol['phone'], None)
        email = sol['email'].lower()
        if phone not in phones and email not in emails:
            res.append(sol)
        phones.add(phone)
        emails.add(email)
    return res


if __name__ == '__main__':
    solutions = [
        {
            'date': '2021-01-01 10:00:00',
            'name': 'Brad Pitt',
            'email': 'Participant1@mail.com',
            'phone': '+7 912-345-67-89',
            'code': '...'
        },
        {
            'date': '2021-01-01 10:01:00',
            'name': 'Not Brad Pitt',
            'email': 'participant2@mail.com',
            'phone': '+7(912) 3456789',
            'code': '...'
        },
        {
            'date': '2021-01-01 10:02:00',
            'name': 'Definitely not Brad Pitt',
            'email': 'particiPANT1@mail.com',
            'phone': '79001234567',
            'code': '...'
        }
    ]
    print(func(solutions))
