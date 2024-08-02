import random
import sqlite3

from faker import Faker

# Conecte ao banco de dados
conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

fake = Faker()


# Função para gerar dados de país
def random_pais(n):
    return [(fake.country_code(), fake.country()) for _ in range(n)]


# Função para gerar dados de areas
def random_area(n):
    return [
        (fake.word(),) for _ in range(n)
    ]  # A vírgula transforma a palavra em uma tupla


# Função para gerar dados de keyword (palavras-chaves)
def random_keyword(n):
    return [
        (fake.word(),) for _ in range(n)
    ]  # A vírgula transforma a palavra em uma tupla


# Função para gerar dados de estado
def random_estado(n, pais_ids):
    return [
        (fake.state_abbr(), fake.state(), random.choice(pais_ids)) for _ in range(n)
    ]


# Função para gerar dados de cidade
def random_cidade(n, estado_ids):
    return [(fake.city(), random.choice(estado_ids)) for _ in range(n)]


# Função para gerar dados de autor
def random_autor(n, cidade_ids):
    return [
        (
            fake.first_name(),
            fake.last_name(),
            fake.email(),
            fake.date_of_birth().isoformat().replace("-", ""),
            random.choice(cidade_ids),
        )
        for _ in range(n)
    ]


# Função para gerar dados de editora
def random_editora(n, cidade_ids):
    return [(fake.company(), random.choice(cidade_ids)) for _ in range(n)]


# Função para gerar dados de subarea
def random_subarea(n, area_ids):
    return [(fake.word(), random.choice(area_ids)) for _ in range(n)]


# Função para gerar dados de publicacao
def random_publicacao(n, editora_ids):
    return [
        (
            fake.sentence(),
            fake.year(),
            random.choice(editora_ids),
            fake.sentence(),
            fake.text(),
            fake.url(),
            random.choice(["J", "C", "L"]),
            random.choice(["INT", "NAC", "REG", "LOC"]),
            random.choice(
                [
                    "RESUM",
                    "FULLP",
                    "LIVRO",
                    "CAPLI",
                    "TESES",
                    "DISSE",
                    "RELAT",
                    "MONOG",
                    "OUTRO",
                ]
            ),
        )
        for _ in range(n)
    ]


# Função para gerar dados de associação de autores com publicações
def random_publicacao_autores(publicacao_ids, autor_ids):
    return [
        (random.choice(publicacao_ids), random.choice(autor_ids))
        for _ in range(len(publicacao_ids))
    ]


# Função para gerar dados de associação de keywords com publicações
def random_publicacao_keywords(publicacao_ids, keyword_ids):
    return [
        (random.choice(publicacao_ids), random.choice(keyword_ids))
        for _ in range(len(publicacao_ids))
    ]


# Popula a tabela de países
paises = random_pais(10)
c.executemany(
    """
    INSERT INTO fabricaNode_pais (sigla, nome) VALUES (?, ?)
""",
    paises,
)

# Obter os IDs dos países inseridos
c.execute("SELECT id FROM fabricaNode_pais")
pais_ids = [row[0] for row in c.fetchall()]

# Popula a tabela de estados
estados = random_estado(10, pais_ids)
c.executemany(
    """
    INSERT INTO fabricaNode_estado (sigla, nome, pais_id) VALUES (?, ?, ?)
""",
    estados,
)

# Obter os IDs dos estados inseridos
c.execute("SELECT id FROM fabricaNode_estado")
estado_ids = [row[0] for row in c.fetchall()]

# Popula a tabela de cidades
cidades = random_cidade(10, estado_ids)
c.executemany(
    """
    INSERT INTO fabricaNode_cidade (nome, estado_id) VALUES (?, ?)
""",
    cidades,
)

# Obter os IDs das cidades inseridas
c.execute("SELECT id FROM fabricaNode_cidade")
cidade_ids = [row[0] for row in c.fetchall()]

# Popula a tabela de autores
autores = random_autor(10, cidade_ids)
c.executemany(
    """
    INSERT INTO fabricaNode_autor (nome, sobrenome, email, dataNascimento, cidade_id) VALUES (?, ?, ?, ?, ?)
""",
    autores,
)

# Obter os IDs dos autores inseridos
c.execute("SELECT id FROM fabricaNode_autor")
autor_ids = [row[0] for row in c.fetchall()]

# Popula a tabela de editoras
editoras = random_editora(10, cidade_ids)
c.executemany(
    """
    INSERT INTO fabricaNode_editora (nome, cidade_id) VALUES (?, ?)
""",
    editoras,
)

# Obter os IDs das editoras inseridas
c.execute("SELECT id FROM fabricaNode_editora")
editora_ids = [row[0] for row in c.fetchall()]

# Popula a tabela de áreas
areas = random_area(10)
c.executemany(
    """
    INSERT INTO fabricaNode_area (nome) VALUES (?)
""",
    areas,
)

# Obter os IDs das áreas inseridas
c.execute("SELECT id FROM fabricaNode_area")
area_ids = [row[0] for row in c.fetchall()]

# Popula a tabela de subáreas
subareas = random_subarea(10, area_ids)
c.executemany(
    """
    INSERT INTO fabricaNode_subarea (nome, area_id) VALUES (?, ?)
""",
    subareas,
)

# Popula a tabela de keywords
keywords = random_keyword(10)
c.executemany(
    """
    INSERT INTO fabricaNode_keyword (palavra) VALUES (?)
""",
    keywords,
)

# Obter os IDs das keywords inseridas
c.execute("SELECT id FROM fabricaNode_keyword")
keyword_ids = [row[0] for row in c.fetchall()]

# Popula a tabela de publicações
publicacoes = random_publicacao(10, editora_ids)
c.executemany(
    """
    INSERT INTO fabricaNode_publicacao (titulo, dataPublicacao, editora_id, conferencia, abstract, url, publicado_em, abrangencia, tipo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""",
    publicacoes,
)

# Obter os IDs das publicações inseridas
c.execute("SELECT id FROM fabricaNode_publicacao")
publicacao_ids = [row[0] for row in c.fetchall()]

# Popula a tabela associativa de publicações e autores
publicacao_autores = random_publicacao_autores(publicacao_ids, autor_ids)
c.executemany(
    """
    INSERT INTO fabricaNode_publicacao_autor (publicacao_id, autor_id) VALUES (?, ?)
""",
    publicacao_autores,
)

# Popula a tabela associativa de publicações e keywords
publicacao_keywords = random_publicacao_keywords(publicacao_ids, keyword_ids)
c.executemany(
    """
    INSERT INTO fabricaNode_publicacao_keyword (publicacao_id, keyword_id) VALUES (?, ?)
""",
    publicacao_keywords,
)

conn.commit()
conn.close()

print("Done!")
