-- Tabela USUARIOS
CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(40) NOT NULL,
    email VARCHAR(80) UNIQUE NOT NULL,
    senha VARCHAR(15) NOT NULL,
    localizacao VARCHAR(100),
    data_cadastro DATE DEFAULT CURRENT_DATE
);

-- Tabela TROCAS
CREATE TABLE trocas (
    id_troca SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    status VARCHAR(15),
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Tabela PLANTAS
CREATE TABLE plantas (
    id_planta SERIAL PRIMARY KEY,
    nome_popular VARCHAR(40),
    tipo VARCHAR(40),
    origem VARCHAR(80),
    familia VARCHAR(50),
    descricao TEXT,
    imagem VARCHAR(150),
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Tabela IMAGENS
CREATE TABLE imagens (
    id_imagem SERIAL PRIMARY KEY,
    url_imagem VARCHAR(150) NOT NULL,
    id_planta INT NOT NULL,
    FOREIGN KEY (id_planta) REFERENCES plantas(id_planta) ON DELETE CASCADE
);

-- Tabela MENSAGENS
CREATE TABLE mensagens (
    id_chat SERIAL PRIMARY KEY,
    mensagem TEXT NOT NULL,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Tabela AVALIACAO
CREATE TABLE avaliacao (
    id_avaliacao SERIAL PRIMARY KEY,
    nota DECIMAL(3,1) CHECK (nota >= 0 AND nota <= 10),
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    comentario TEXT,
    id_avaliador INT NOT NULL,
    id_avaliado INT NOT NULL,
    FOREIGN KEY (id_avaliador) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_avaliado) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);
