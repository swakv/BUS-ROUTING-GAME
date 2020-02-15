red_mapping = {(' Hall 11 ', 1): 0,
 (' Grad Hall 1&2 ', 0): 1,
 (' Grad Hall 1&2 ', 1): 2,
 (' Saraca Hall ', 0): 3,
 (' Saraca Hall ', 1): 4,
 (' Hall 12&13 ', 0): 5,
 (' Hall 12&13 ', 1): 6,
 (' Hall 12&13 ', 2): 7,
 (' LWN Library ', 0): 8,
 (' LWN Library ', 1): 9,
 (' LWN Library ', 2): 10,
 (' SBS ', 0): 11,
 (' SBS ', 1): 12,
 (' WKWSCI ', 0): 13,
 (' WKWSCI ', 1): 14,
 (' Hall 7 ', 0): 15,
 (' Hall 7 ', 1): 16,
 (' Yunnan Gardens ', 0): 17,
 (' Yunnan Gardens ', 1): 18,
 (' Yunnan Gardens ', 2): 19,
 (' Hall 4 ', 0): 20,
 (' Hall 4 ', 1): 21,
 (' Hall 1 - Blk 18 ', 0): 22,
 (' Hall 1 - Blk 18 ', 1): 23,
 (' Canteen 2 ', 0): 24,
 (' Canteen 2 ', 1): 25,
 (' Hall 8 ', 0): 26,
 (' Hall 8 ', 1): 27,
 (' Hall 11 ', 0): 28
 }

blue_mapping = {(' Opp Hall 11 ', 0): 0,
 (' Opp Hall 11 ', 1): 1,
 (' Opp Hall 8 ', 0): 2,
 (' Opp Hall 8 ', 1): 3,
 (' Opp Hall 8 ', 2): 4,
 (' Hall 6 ', 0): 5,
 (' Hall 6 ', 1): 6,
 (' Hall 6 ', 2): 7,
 (' Opp Hall 4 ', 0): 8,
 (' Opp Hall 4 ', 1): 9,
 (' Opp Hall 4 ', 2): 10,
 (' Opp Yunnan Gardens ', 0): 11,
 (' Opp Yunnan Gardens ', 1): 12,
 (' Opp SPMS ', 0): 13,
 (' Opp SPMS ', 1): 14,
 (' Opp WKWSCI ', 0): 15,
 (' Opp WKWSCI ', 1): 16,
 (' Opp CEE ', 0): 17,
 (' Opp CEE ', 1): 18,
 (' NIE ', 0): 19,
 (' NIE ', 1): 20,
 (' NIE ', 2): 21,
 (' Opp Hall 3 & 16 ', 0): 22,
 (' Opp Hall 3 & 16 ', 1): 23,
 (' Opp Hall 14 & 15 ', 0): 24,
 (' Opp Hall 14 & 15 ', 1): 25,
 (' Opp Saraca Hall ', 0): 26,
 (' Opp Saraca Hall ', 1): 27,
 (' Opp Saraca Hall ', 2): 28
 }

class Mapping:

    def getMapping(route):
        if route == 'red':
            return red_mapping
        else:
            return blue_mapping