"""
That task is from my practice. Sometimes I do Python webinars and organizers want to send gifts to some listeners.

To choose those who will receive a prize, I send them Home Assignment and Google Form for solutions. Then I receive
solutions table (like in 1st HA), download table as CSV file and upload it into Python using csv.DictReader.

We will skip that part. The point is - table becomes this data structure:

solutions = [
    {
        'date': '2021-01-01 10:00:00',
        'email': 'Participant1@mail.com',
        'code': '...'
    },
    {
        'date': '2021-01-01 10:01:00',
        'email': 'participant2@mail.com',
        'code': '...'
    },
    {
        'date': '2021-01-01 10:02:00',
        'email': 'particiPANT1@mail.com',
        'code': '...'
    },
    ...
]

Then I do a lottery - randomly choose winners using "random.choice(solutions)" command in live broadcast.

But some participants trying to cheat - they send solution several times, so they chances became bigger. For example,
in a given "solutions" list, 1st and 3rd solutions have the same email.

Sometimes it is not a cheating - a participant can send 2 works accidentally or just because he found an error in first
solution.

The task is to help me to equalize the odds using participant's emails. As a result, you need to create the
"filtered_solutions" list with only 1 solution from 1 participant.

If a participant sent 2 or more solutions, you need to keep only the last attempt. Solutions are sorted by date.
"""


def func(sols):
    emails = set()
    res = list()
    for sol in reversed(sols):
        if sol['email'].lower() not in emails:
            emails.add(sol['email'].lower())
            res.append(sol)
    return res


if __name__ == '__main__':
    solutions = [
        {
            'date': '2021-01-01 10:00:00',
            'email': 'Participant1@mail.com',
            'code': '...'
        },
        {
            'date': '2021-01-01 10:01:00',
            'email': 'participant2@mail.com',
            'code': '...'
        },
        {
            'date': '2021-01-01 10:02:00',
            'email': 'particiPANT1@mail.com',
            'code': '...'
        },
    ]
    print(func(solutions))
