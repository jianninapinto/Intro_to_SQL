GET_CHARACTERS = 'SELECT * FROM charactercreator_character;'


AVG_ITEM_WEIGHT_PER_CHARACTER = """
    SELECT cc_char.name, AVG(ai.weight) AS avg_item_weight
    FROM charactercreator_character AS cc_char
        JOIN charactercreator_character_inventory	AS cc_inv
        ON cc_char.character_id = cc_inv.character_id

        JOIN armory_item AS ai
        ON ai.item_id = cc_inv.item_id
    GROUP BY cc_char.character_id;
    """

CREATE_TEST_TABLE = """
    CREATE TABLE IF NOT EXISTS test_table
    ("id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL,
    "age" INT NOT NULL,
    "country_of_origin" VARCHAR(200) NOT NULL);
"""

INSERT_TEST_TABLE = """
    INSERT INTO test_table ("name", "age", "country_of_origin")
    VALUES ('Jiannina Pinto', 30, 'Colombia')
"""

DROP_TEST_TABLE = """
    DROP TABLE IF EXISTS test_table
"""

CREATE_CHARACTER_TABLE = """
    CREATE TABLE IF NOT EXISTS characters
    (
    "character_id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(30) NOT NULL,
    "level" INT NOT NULL,
    "exp" INT NOT NULL,
    "hp" INT NOT NULL,
    "strength" INT NOT NULL,
    "intelligence" INT NOT NULL,
    "dexterity" INT NOT NULL,
    "wisdom" INT NOT NULL
    );
"""

INSERT_JIANNINA = """
    INSERT INTO characters ("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom")
    VALUES ('Jiannina Pinto', 50, 100, 1000, 9000, 4, -5, 12)
"""

DROP_CHARACTER_TABLE = """
    DROP TABLE IF EXISTS characters
"""


QUERY_LIST = [GET_CHARACTERS,
              AVG_ITEM_WEIGHT_PER_CHARACTER,
              CREATE_TEST_TABLE,
              INSERT_TEST_TABLE,
              DROP_TEST_TABLE,
              CREATE_CHARACTER_TABLE,
              INSERT_JIANNINA,
              DROP_CHARACTER_TABLE
              ]
