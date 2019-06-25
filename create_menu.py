from os import getcwd

from PyInquirer import prompt

if __name__ == '__main__':
    current_path = getcwd()

    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Name?'
        },
        {
            'type': 'input',
            'name': 'global_',
            'message': 'Global?',
            'default': 'n'
        },
        {
            'type': 'input',
            'name': 'path',
            'message': 'path?',
            'defaults': getcwd()
        },
        {
            'type': 'input',
            'name': 'parent',
            'message': 'Parent?',
            'default': None
        },
        {
            'type': 'input',
            'name': 'command',
            'message': 'Cmd?'
        },
    ]

    answers = prompt(questions)

    print(answers)
