from setuptools import setup, find_packages

setup(
    name='supabase_utils',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'supabase',
        'psycopg2',
        'python-dotenv',# ou o client que você usa
    ],
    description='Utilitários compartilhados para consultas ao Supabase',
    author='Matheus Brito de Oliveira',
    url='https://github.com/matheus-brito-dev/supabase_utils'
)
