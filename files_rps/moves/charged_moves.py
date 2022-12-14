class charged_moves():
    def __init__(self, type_move, damage, energy, effects=''):
        self.type_move = type_move
        self.damage = damage
        self.energy = energy
        self.damage_per_energy = round(self.damage / self.energy, 2)
        self.effects = effects

    def __str__(self):
        return f'{self.type_move}, {self.damage}, {self.energy}, {self.damage_per_energy}, {self.effects}'

    def info(self):
        return [self.type_move, self.damage, self.energy, self.damage_per_energy, self.effects]

charged_moves_dict = {
    'Acid Spray': charged_moves('poison', 20, 45, '100% chance -2 Def opponent'),
    'Aerial Ace': charged_moves('flying', 55, 45),
    'Aeroblast': charged_moves('flying', 170, 75, '12.5% chance +2 Atk self'),
    'Air Cutter': charged_moves('flying', 60, 55),
    'Ancient Power': charged_moves('rock', 45, 45, '10% chance +2 Atk +2 Def self'),
    'Aqua Jet': charged_moves('water', 45, 45),
    'Aqua Tail': charged_moves('water', 50, 35),
    'Aura Sphere': charged_moves('fighting', 100, 55),
    'Aurora Beam': charged_moves('ice', 80, 60),
    'Avalanche': charged_moves('ice', 90, 45),
    'Blast Burn': charged_moves('fire', 110, 50),
    'Blaze Kick': charged_moves('fire', 55, 40),
    'Blizzard': charged_moves('ice', 140, 75),
    'Body Slam': charged_moves('normal', 60, 35),
    'Bone Club': charged_moves('ground', 40, 35),
    'Brave Bird': charged_moves('flying', 130, 55, '100% chance -3 Def self'),
    'Brick Break': charged_moves('fighting', 40, 35),
    'Brine': charged_moves('water', 60, 50),
    'Bubble Beam': charged_moves('water', 25, 40, '100% chance -1 Atk opponent'),
    'Bug Buzz': charged_moves('bug', 90, 60, '30% chance -1 Def opponent'),
    'Bulldoze': charged_moves('ground', 80, 60),
    'Close Combat': charged_moves('fighting', 100, 45, '100% chance -2 Def self'),
    'Crabhammer': charged_moves('water', 85, 50, '12.5% chance +2 Atk self'),
    'Cross Chop': charged_moves('fighting', 50, 35),
    'Cross Poison': charged_moves('poison', 50, 35, '12.5% chance +2 Atk self'),
    'Crunch': charged_moves('dark', 70, 45, '30% chance -1 Def opponent'),
    'Dark Pulse': charged_moves('dark', 80, 50),
    'Dazzling Gleam': charged_moves('fairy', 110, 70),
    'Dig': charged_moves('ground', 100, 80),
    'Disarming Voice': charged_moves('fairy', 70, 45),
    'Discharge': charged_moves('electric', 65, 45),
    'Doom Desire': charged_moves('steel', 75, 40),
    'Draco Meteor': charged_moves('dragon', 150, 65, '100% chance -2 Atk self'),
    'Dragon Claw': charged_moves('dragon', 50, 35),
    'Dragon Pulse': charged_moves('dragon', 90, 60),
    'Draining Kiss': charged_moves('fairy', 60, 55),
    'Drill Peck': charged_moves('flying', 65, 40),
    'Drill Run': charged_moves('ground', 80, 45),
    'Dynamic Punch': charged_moves('fighting', 90, 50),
    'Earth Power': charged_moves('ground', 90, 55, '10% chance -1 Def opponent'),
    'Earthquake': charged_moves('ground', 120, 65),
    'Energy Ball': charged_moves('grass', 90, 55, '10% chance -1 Def opponent'),
    'Feather Dance': charged_moves('flying', 35, 50, '100% chance -2 Atk opponent'),
    'Fell Stinger': charged_moves('bug', 20, 35, '100% chance +1 Atk self'),
    'Fire Blast': charged_moves('fire', 140, 80),
    'Fire Punch': charged_moves('fire', 55, 40),
    'Flame Burst': charged_moves('fire', 70, 55),
    'Flame Charge': charged_moves('fire', 65, 50, '100% chance +1 Atk self'),
    'Flame Wheel': charged_moves('fire', 60, 55),
    'Flamethrower': charged_moves('fire', 90, 55),
    'Flash Cannon': charged_moves('steel', 110, 70),
    'Fly': charged_moves('flying', 80, 45),
    'Flying Press': charged_moves('fighting', 90, 40),
    'Focus Blast': charged_moves('fighting', 150, 75),
    'Foul Play': charged_moves('dark', 70, 45),
    'Frenzy Plant': charged_moves('grass', 100, 45),
    'Frustration': charged_moves('normal', 10, 70),
    'Future Sight': charged_moves('psychic', 120, 65),
    'Giga Drain': charged_moves('grass', 50, 80),
    'Giga Impact': charged_moves('normal', 150, 80),
    'Grass Knot': charged_moves('grass', 90, 50),
    'Gunk Shot': charged_moves('poison', 130, 75),
    'Gyro Ball': charged_moves('steel', 80, 60),
    'Heart Stamp': charged_moves('psychic', 40, 40),
    'Heat Wave': charged_moves('fire', 95, 75),
    'Heavy Slam': charged_moves('steel', 70, 50),
    'Horn Attack': charged_moves('normal', 40, 35),
    'Hurricane': charged_moves('flying', 110, 65),
    'Hydro Cannon': charged_moves('water', 80, 40),
    'Hydro Pump': charged_moves('water', 130, 75),
    'Hyper Beam': charged_moves('normal', 150, 80),
    'Hyper Fang': charged_moves('normal', 80, 50),
    'Ice Beam': charged_moves('ice', 90, 55),
    'Ice Punch': charged_moves('ice', 55, 40),
    'Icy Wind': charged_moves('ice', 60, 45, '100% chance -1 Atk opponent'),
    'Iron Head': charged_moves('steel', 70, 50),
    'Last Resort': charged_moves('normal', 90, 55),
    'Leaf Blade': charged_moves('grass', 70, 35),
    'Leaf Storm': charged_moves('grass', 130, 55, '100% chance -2 Atk self'),
    'Leaf Tornado': charged_moves('grass', 45, 40, '50% chance -2 Atk opponent'),
    'Low Sweep': charged_moves('fighting', 40, 40),
    'Lunge': charged_moves('bug', 60, 45, '100% chance -1 Atk opponent'),
    'Magnet Bomb': charged_moves('steel', 70, 45),
    'Mega Drain': charged_moves('grass', 25, 55),
    'Megahorn': charged_moves('bug', 110, 55),
    'Meteor Mash': charged_moves('steel', 100, 50),
    'Mirror Coat': charged_moves('psychic', 60, 55),
    'Mirror Shot': charged_moves('steel', 35, 35, '30% chance -1 Atk opponent'),
    'Moonblast': charged_moves('fairy', 110, 60, '10% chance -1 Atk opponent'),
    'Mud Bomb': charged_moves('ground', 55, 40),
    'Muddy Water': charged_moves('water', 35, 35, '30% chance -1 Atk opponent'),
    'Night Shade': charged_moves('ghost', 60, 55),
    'Night Slash': charged_moves('dark', 50, 35, '12.5% chance +2 Atk self'),
    'Octazooka': charged_moves('water', 50, 50, '50% chance -2 Atk opponent'),
    'Ominous Wind': charged_moves('ghost', 45, 45, '10% chance +2 Atk +2 Def self'),
    'Origin Pulse': charged_moves('water', 130, 60),
    'Outrage': charged_moves('dragon', 110, 60),
    'Overheat': charged_moves('fire', 130, 55, '100% chance -2 Atk self'),
    'Parabolic Charge': charged_moves('electric', 25, 55),
    'Payback': charged_moves('dark', 110, 60),
    'Petal Blizzard': charged_moves('grass', 110, 65),
    'Play Rough': charged_moves('fairy', 90, 60),
    'Poison Fang': charged_moves('poison', 40, 35, '100% chance -1 Def opponent'),
    'Power Gem': charged_moves('rock', 80, 60),
    'Power Whip': charged_moves('grass', 90, 50),
    'Power-Up Punch': charged_moves('fighting', 20, 35, '100% chance +1 Atk self'),
    'Precipice Blades': charged_moves('ground', 130, 60),
    'Psybeam': charged_moves('psychic', 70, 60),
    'Psychic': charged_moves('psychic', 90, 55, '10% chance -1 Def opponent'),
    'Psychic Fangs': charged_moves('psychic', 40, 35, '100% chance -1 Def opponent'),
    'Psycho Boost': charged_moves('psychic', 70, 35, '100% chance -2 Atk self'),
    'Psyshock': charged_moves('psychic', 70, 45),
    'Psystrike': charged_moves('psychic', 90, 45),
    'Razor Shell': charged_moves('water', 35, 35, '50% chance -1 Def opponent'),
    'Rest': charged_moves('normal', 50, 35),
    'Return': charged_moves('normal', 130, 70),
    'Rock Blast': charged_moves('rock', 50, 40),
    'Rock Slide': charged_moves('rock', 75, 45),
    'Rock Tomb': charged_moves('rock', 70, 60),
    'Rock Wrecker': charged_moves('rock', 110, 50),
    'Sacred Sword': charged_moves('fighting', 60, 35),
    'Sand Tomb': charged_moves('ground', 25, 40, '100% chance -1 Def opponent'),
    'Scald': charged_moves('water', 80, 50, '30% chance -1 Atk opponent'),
    'Seed Bomb': charged_moves('grass', 55, 40),
    'Shadow Ball': charged_moves('ghost', 100, 55),
    'Shadow Bone': charged_moves('ghost', 75, 45, '20% chance -1 Def opponent'),
    'Shadow Punch': charged_moves('ghost', 40, 35),
    'Shadow Sneak': charged_moves('ghost', 50, 45),
    'Signal Beam': charged_moves('bug', 75, 55, '20% chance -1 Atk -1 Def opponent'),
    'Silver Wind': charged_moves('bug', 45, 45, '10% chance +2 Atk +2 Def self'),
    'Skull Bash': charged_moves('normal', 130, 75, '100% chance +1 Def self'),
    'Sky Attack': charged_moves('flying', 75, 45),
    'Sludge': charged_moves('poison', 50, 40),
    'Sludge Bomb': charged_moves('poison', 80, 50),
    'Sludge Wave': charged_moves('poison', 110, 65),
    'Solar Beam': charged_moves('grass', 150, 80),
    'Stomp': charged_moves('normal', 55, 40),
    'Stone Edge': charged_moves('rock', 100, 55),
    'Struggle': charged_moves('normal', 35, 100),
    'Submission': charged_moves('fighting', 60, 50),
    'Superpower': charged_moves('fighting', 85, 40, '100% chance -1 Atk -1 Def self'),
    'Surf': charged_moves('water', 65, 40),
    'Swift': charged_moves('normal', 60, 55),
    'Synchronoise': charged_moves('psychic', 80, 50),
    'Techno Blast (Burn)': charged_moves('fire', 120, 55),
    'Techno Blast (Chill)': charged_moves('ice', 120, 55),
    'Techno Blast (Douse)': charged_moves('water', 120, 55),
    'Techno Blast (Normal)': charged_moves('normal', 120, 55),
    'Techno Blast (Shock)': charged_moves('electric', 120, 55),
    'Thunder': charged_moves('electric', 100, 60),
    'Thunder Punch': charged_moves('electric', 55, 40),
    'Thunderbolt': charged_moves('electric', 90, 55),
    'Tri Attack': charged_moves('normal', 65, 50, '50% chance -1 Atk -1 Def opponent'),
    'Twister': charged_moves('dragon', 45, 45),
    'V-Create': charged_moves('fire', 95, 40, '100% chance -3 Def self'),
    'Vise Grip': charged_moves('normal', 40, 40),
    'Water Pulse': charged_moves('water', 70, 60),
    'Weather Ball (Fire)': charged_moves('fire', 55, 35),
    'Weather Ball (Ice)': charged_moves('ice', 55, 35),
    'Weather Ball (Normal)': charged_moves('normal', 55, 35),
    'Weather Ball (Rock)': charged_moves('rock', 55, 35),
    'Weather Ball (Water)': charged_moves('water', 55, 35),
    'Wild Charge': charged_moves('electric', 100, 45, '100% chance -2 Def self'),
    'Wrap': charged_moves('normal', 60, 45),
    'Wrap Green': charged_moves('normal', 25, 45),
    'Wrap Pink': charged_moves('normal', 25, 45),
    'X-Scissor': charged_moves('bug', 45, 35),
    'Zap Cannon': charged_moves('electric', 150, 80, '100% chance -1 Atk opponent')
}
