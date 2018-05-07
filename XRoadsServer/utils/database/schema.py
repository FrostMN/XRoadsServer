drop_users = """DROP TABLE IF EXISTS users"""
drop_characters = """DROP TABLE IF EXISTS characters"""

create_users = """
CREATE TABLE users(
    user_id INTEGER AUTO_INCREMENT,
    user_name VARCHAR(120) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    email_confirmed SMALLINT NOT NULL DEFAULT 0,
    temp_email VARCHAR(120) UNIQUE,
    admin SMALLINT NOT NULL DEFAULT 0,
    banned SMALLINT NOT NULL DEFAULT 0,
    first_name VARCHAR(120) DEFAULT '',
    last_name VARCHAR(120) DEFAULT '',
    hash VARCHAR(60) NOT NULL,
    nonce VARCHAR(64) DEFAULT '',
    nonce_timestamp DATETIME,
    creation_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id)
)
"""

create_characters = """
CREATE TABLE characters(
    characters_id INTEGER AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    character_name VARCHAR(120) NOT NULL,
    character_background VARCHAR(3) NOT NULL,
    character_class VARCHAR(3) NOT NULL DEFAULT 'UNT', -- added NOT NULL and didn't test right away
    character_rank INTEGER DEFAULT 0,
    rank_up SMALLINT DEFAULT 0,

    -- Abilities 
    lance_corporal_ability INTEGER DEFAULT NULL,
    corporal_ability INTEGER DEFAULT NULL,
    sergeant_ability INTEGER DEFAULT NULL,
    staff_sergeant_ability INTEGER DEFAULT NULL,
    tech_sergeant_ability INTEGER DEFAULT NULL,
    gunnery_sergeant_ability INTEGER DEFAULT NULL,
    master_sergeant_ability INTEGER DEFAULT NULL,
        
    CONSTRAINT fk_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,
    PRIMARY KEY (characters_id)
)
"""

schema = [drop_characters, drop_users, create_users, create_characters]
