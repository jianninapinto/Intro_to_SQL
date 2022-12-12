TOTAL_CHARACTERS = """
    SELECT COUNT(*)
    FROM charactercreator_character AS cc_char;
    """

TOTAL_DISTINCT_CHARACTERS = """
    SELECT COUNT(DISTINCT(name)) AS distinct_names
    FROM charactercreator_character;
    """

TOTAL_SUBCLASS = """
    SELECT COUNT(*)
    FROM charactercreator_necromancer;
    """

TOTAL_ITEMS = """
    SELECT COUNT(*)
    FROM armory_item;
    """

WEAPONS = """
    SELECT COUNT(*)
    FROM armory_weapon  AS aw
        INNER JOIN armory_item AS ai
    WHERE ai.item_id = aw.item_ptr_id;
    """

NON_WEAPONS = """
    SELECT COUNT(*)
    FROM armory_item
    WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon);
    """

CHARACTER_ITEMS = """
    SELECT name, COUNT(item_id)
    FROM charactercreator_character AS cc_char
        INNER JOIN charactercreator_character_inventory AS cc_char_inv
        ON cc_char.character_id = cc_char_inv.character_id

    GROUP BY cc_char.character_id
    LIMIT 20;
    """

CHARACTER_WEAPONS = """
    SELECT cc_char.name, COUNT(ai.item_id)  AS total_weapons
    FROM armory_item AS ai
        INNER JOIN armory_weapon AS aw
        ON ai.item_id = aw.item_ptr_id

        INNER JOIN charactercreator_character_inventory as cc_char_inv
        ON ai.item_id = cc_char_inv.item_id

        INNER JOIN charactercreator_character as cc_char
        ON cc_char.character_id = cc_char_inv.character_id

    GROUP BY cc_char.character_id
    LIMIT 20;
    """

AVG_CHARACTER_ITEMS = """
    SELECT AVG(total_items)
    FROM (SELECT cc_char.name, COUNT(item_id) AS total_items
        FROM charactercreator_character AS cc_char
            INNER JOIN charactercreator_character_inventory AS cc_char_inv
            ON cc_char.character_id = cc_char_inv.character_id
            GROUP BY cc_char.character_id);
    """

AVG_CHARACTER_WEAPONS = """
    SELECT AVG(total_weapons)
    FROM (SELECT cc_char.name, COUNT(ai.item_id)  AS total_weapons
        FROM armory_item AS ai
            INNER JOIN armory_weapon AS aw
            ON ai.item_id = aw.item_ptr_id

            INNER JOIN charactercreator_character_inventory as cc_char_inv
            ON ai.item_id = cc_char_inv.item_id

            INNER JOIN charactercreator_character as cc_char
            ON cc_char.character_id = cc_char_inv.character_id
        GROUP BY cc_char.character_id);
    """

QUERY_LIST = [TOTAL_CHARACTERS,
              TOTAL_DISTINCT_CHARACTERS,
              TOTAL_SUBCLASS,
              TOTAL_ITEMS,
              WEAPONS,
              NON_WEAPONS,
              CHARACTER_ITEMS,
              CHARACTER_WEAPONS,
              AVG_CHARACTER_ITEMS,
              AVG_CHARACTER_WEAPONS]
