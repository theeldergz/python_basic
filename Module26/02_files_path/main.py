import os

test_dir = 'Module17'


def gen_files_path(required_dir, user_path=os.path.join('C:\\')):
    for root, dirs, files in os.walk(user_path):
        for direct in dirs:
            if direct == required_dir:
                for file in files:
                    yield os.path.join(root, direct, file)


test = gen_files_path(test_dir)

for elem in test:
    print(elem)

