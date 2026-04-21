import time

def step(msg):
    print(msg)
    time.sleep(0.2)

project_name = input()
author_name  = input()
python_ver   = input()

step(f'Creating project: {project_name}')
step(f'Author : {author_name}')
step(f'Python : {python_ver}')

dirs = [
    project_name,
    f'{project_name}/src/',
]

step('\nCreating project directories...')
for d in dirs:
    step(f'    {d}')

files = [
    f'{project_name}/pyproject.toml',
    f'{project_name}/.gitignore',
    f'{project_name}/src/{project_name}/main.py',
]

step('\nCreating files...')
for f in files:
    step(f'    {f}')

step(f'\nCreating virtual env...')
step(f'    python{python_ver} -m venv {project_name}/.venv')
step('    Installing pip... done')
step('    Installing setuptools... done')

step(f'\nInitializing git repository...')
step(f'    git init {project_name}/')
step(f'    git -C {project_name}/ add .')
step(f'    git -C {project_name}/ commit -m "Initial commit"')

step(f'\nDone! To get started:')
step(f'    cd {project_name}')
step(f'    source .venv/bin/activate')
step(f'    pip install -e .[dev]')
