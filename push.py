import os
import random
from .clone import github_user, github_repo

commit_messages = ['I deserve more commits',
                   'This is a very important commit',
                   'The app has become a hundred times better',
                   'App is incomplete without this commit',
                   'God gave birth to this commit',
                   'You know you did not do any work anyway',
                   'Vengeance for your fake commits',
                   'I am number 1',
                   'Please start doing some work',
                   ]

message = random.choice(commit_messages)


def push(custom_message, custom_file = '.gitcred'):
    if custom_file == '.gitcred':
        os.system('touch %s' % custom_file)
        os.system('git add %s' % custom_file)
        if custom_message:
            os.system('git commit -m % s' % custom_message)
        else:

    else:
        os.system('touch .gitcred')


