import json

from database.dbtools import DbTool
from game.objects.db_objects import FieldType, Field, CreatureGroup, CreatureType, SpawnedCreature, BoundedItem, Item
from tools.global_paths import MAP_DATA_FILE


def insert_initial_data():
    insert_map_data()
    insert_creature_groups()
    insert_creature_types()
    insert_spawned_creature()
    insert_items()
    insert_bounded_items()


def insert_map_data():
    obj_dict = {"FieldType": FieldType, "Field": Field}
    with open(MAP_DATA_FILE) as f:
        json_data = json.loads(f.read())
        for table_name in obj_dict.keys():
            for row in json_data[table_name]:
                DbTool().insert_row(obj_dict[table_name](**row))


def insert_creature_groups():
    DbTool().insert_many_rows([CreatureGroup(name="player", talkative=True, trader=True),
                               CreatureGroup(name="NPC", talkative=True, trader=True),
                               CreatureGroup(name="animal", talkative=False, trader=False)])


def insert_creature_types():
    DbTool().insert_many_rows(([CreatureType(name="Player", strength=20, agility=20, group_id=1),
                                CreatureType(name="Blacksmith", strength=30, agility=15, group_id=2),
                                CreatureType(name="Monk", strength=5, agility=30, group_id=2),
                                CreatureType(name="Wolf", strength=5, agility=40, group_id=3),
                                CreatureType(name="Bear", strength=40, agility=10, group_id=3)]))


def insert_spawned_creature():
    DbTool().insert_many_rows([SpawnedCreature(field_id=44, type_id=1),
                               SpawnedCreature(custom_name="Meldor", field_id=56, type_id=2),
                               SpawnedCreature(field_id=56, type_id=2),
                               SpawnedCreature(custom_name="Ornlu the wolf", field_id=33, type_id=4)])


def insert_items():
    for name, weight, value in zip(["Apple", "Potato", "Watermelon", 'Onion'], [3, 2, 8, 2], [5, 3, 12, 5]):
        DbTool().insert_row(Item(name=name, weight=weight, value=value))


def insert_bounded_items():
    DbTool().insert_many_rows([BoundedItem(item_id=1, quantity=2, character_id=1),
                               BoundedItem(item_id=2, quantity=13, character_id=1),
                               BoundedItem(item_id=4, quantity=23, character_id=1),
                               BoundedItem(item_id=3, quantity=1, character_id=2),
                               BoundedItem(item_id=2, quantity=5, character_id=2)])
