class Player:
    new_team = []
    def __init__(self, dic):
        self.name = dic["name"]
        self.age = dic["age"]
        self.position = dic["position"]
        self.team = dic["team"]

    @classmethod
    def print_name_new_team(cls):
        for player in cls.new_team:
            print(player.name)


kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]


for player in players:
    Player.new_team.append(Player(player))
    
# Create your Player instances here!
player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)
print(player_jason.name)
print(player_kevin.name)
print(player_kyrie.name)
print(Player.new_team)
Player.print_name_new_team()
