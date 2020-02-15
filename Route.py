graphRed = {
    " LWN Library " : {
        "nextStop" : " SBS ",
        "roadWeight" : 3
    },
    " SBS " : {
        "nextStop" : " WKWSCI ",
        "roadWeight" : 2
    },    
    " WKWSCI " : {
        "nextStop" : " Hall 7 ",
        "roadWeight" : 2
    },
    " Hall 7 " : {
        "nextStop" : " Yunnan Gardens ",
        "roadWeight" : 2
    },
    " Yunnan Gardens " : {
        "nextStop" : " Hall 4 ",
        "roadWeight" : 3
    },
    " Hall 4 " : {
        "nextStop" : " Hall 1 - Blk 18 ",
        "roadWeight" : 2
    },
    " Hall 1 - Blk 18 " : {
        "nextStop" : " Canteen 2 ",
        "roadWeight" : 2
    },
    " Canteen 2 " : {
        "nextStop" : " Hall 8 ",
        "roadWeight" : 2
    },
    " Hall 8 " : {
        "nextStop" : " Hall 11 ",
        "roadWeight" : 2
    },
    " Hall 11 " : {
        "nextStop" : " Grad Hall 1&2 ",
        "roadWeight" : 2
    },
    " Grad Hall 1&2 " : {
        "nextStop" : " Saraca Hall ",
        "roadWeight" : 2
    },
    " Saraca Hall " : {
        "nextStop" : " Hall 12&13 ",
        "roadWeight" : 2
    },
    " Hall 12&13 " : {
        "nextStop" : " LWN Library ",
        "roadWeight" : 3
    },
}

graphBlue = {
  " NIE " : {
    "nextStop" : " Opp Hall 3 & 16 ",
    "roadWeight" : 3
  },
  " Opp Hall 3 & 16 " : {
    "nextStop" : " Opp Hall 14 & 15 ",
    "roadWeight" : 2
  },
  " Opp Hall 14 & 15 " : {
    "nextStop" : " Opp Saraca Hall ",
    "roadWeight" : 2
  },
  " Opp Saraca Hall " : {
    "nextStop" : " Opp Hall 11 ",
    "roadWeight" : 3
  },
  " Opp Hall 11 " : {
    "nextStop" : " Opp Hall 8 ",
    "roadWeight" : 2
  },
  " Opp Hall 8 " : {
    "nextStop" : " Hall 6 ",
    "roadWeight" : 3
  },
  " Hall 6 " : {
    "nextStop" : " Opp Hall 4 ",
    "roadWeight" : 3
  },
  " Opp Hall 4 " : {
    "nextStop" : " Opp Yunnan Gardens ",
    "roadWeight" : 3
  },
  " Opp Yunnan Gardens " : {
    "nextStop" : " Opp SPMS ",
    "roadWeight" : 2
  },
  " Opp SPMS " : {
    "nextStop" : " Opp WKWSCI ",
    "roadWeight" : 2
  },
  " Opp WKWSCI " : {
    "nextStop" : " Opp CEE ",
    "roadWeight" : 2
  },
  " Opp CEE " : {
    "nextStop" : " NIE ",
    "roadWeight" : 2
  }
}

class Route:
    def getDetails(colour):
        if colour == 'red':
            return graphRed
        else:
            return graphBlue