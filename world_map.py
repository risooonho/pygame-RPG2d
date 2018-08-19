from dbtools import DbTool
from game_objects import Field, Character


class WorldMap:
    def __init__(self):
        self.size = 20
        self.__fields = DbTool().get_all_rows(Field)

    def __getitem__(self, item):
        return self.__fields[item - 1]

    def __setitem__(self, key, value, asd):
        pass

    def __format__(self, format_spec='c'):

        if format_spec in "tc":
            list_to_format = ['{} ' if field.id % self.size != 0 else '{}\n' for field in self.__fields]
            joined_list = "".join(list_to_format)
            if format_spec == "t":
                return joined_list.format(*(field.biome for field in self.__fields))
            elif format_spec == "c":
                return joined_list.format(*(field.biome if field.id not in self.player_id
                                            else "X" for field in self.__fields))
        elif format_spec == "i":
            list_to_format = ['{}' + " " * round(1 / (len(str(field.id)) / 3)) if field.id % self.size != 0
                              else '{}\n' for field in self.__fields]
            joined_list = "".join(list_to_format)
            return joined_list.format(*(field.id for field in self.__fields))

    def __repr__(self):
        return format(self, "t")

    @property
    def player_id(self):
        return [character.field_id for character in DbTool().get_all_rows(Character)]