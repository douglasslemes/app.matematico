from setuptools import setup, find_packages

with open('README.md', 'r') as f:
  long_description = f.read()

setup(
  name='calculos_matematicos',  # Nome do seu pacote (único no PyPI)
  version='0.1.0',  # Versão do seu pacote
  author='Seu nome',
  author_email='seu_email@exemplo.com',
  description='Pacote com funções matemáticas e conversão de números',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/seu_usuario/seu_repositorio',  # Opcional: link para o repositório do seu código
  packages=find_packages(),  # Encontra automaticamente os pacotes e subpacotes
  classifiers=[  # Informações sobre o pacote (licença, versão do Python, etc.)
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.7',  # Versão mínima do Python
  install_requires=[  # Dependências do seu pacote (se houver alguma)
    # Ex: 'requests', 'numpy'
  ],
)