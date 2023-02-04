import random
import os


class Name():
    special_suffixes = {
        "kitten": "kit",
        "apprentice": "paw",
        "medicine cat apprentice": "paw",
        "mediator apprentice": "paw",
        "leader": "star"
    }
    normal_suffixes = [  # common suffixes
        "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", 'fur', 'fur', 'fur',
        "tuft", "tuft", "tuft", "tuft", "tuft", "tooth", "tooth", "tooth", "tooth", "tooth",
        'pelt', "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt",
        "tail", "tail", "tail", "tail", "tail", "tail", "tail", "tail", "claw", "claw", "claw", "claw", "claw", "claw", "claw",
        "foot", "foot", "foot", "foot", "foot", "whisker", "whisker", "whisker", "whisker", "whisker", "whisker",
        "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart", 'heart',

        # regular suffixes
        "acorn", "ash", "aster", "back", "bark", "beam", "bee", "belly", "berry", "bite", "bird", "blaze", "blink", "bloom", 
        "blossom", "blotch", "bounce", "bracken", "branch", "breeze", "briar", "bright", "brook", "burr", "burrow", "bush", "call",
        "catcher", "cloud", "clouds", "clover", "coral", "crawl", "creek", "cry", "dapple", "daisy", "dawn", "drift", "drop", "dusk", "dust",
        "ear", "ears", "eater", "eye", "eyes", "face", "fall", "fang", "fawn", "feather", "fern", "fin", "fire", "fish", "flake",
        "flame", "flight", "flick", "flood", "flower", "fox", "frost", "gaze", "goose", "gorse", "grass", "hail", "hare", "hawk", "haze",
        "heather", "hollow", "holly", "horse", "ice", "ivy", "jaw", "jay", "jump", "kite", "lake", "larch", "leaf", "leap", 
        "leaves", "leg", "light", "lightning", "lilac", "lily", "lotus", "mask", "mark", "minnow", "mist", "moth", "moon", "moss", "mouse",
        "muzzle", "needle", "nettle", "night", "noise", "nose", "nut", "pad", "patch", "path", "peak", "petal", "plume", "pond",
        "pool", "poppy", "pounce", "puddle", "rain", "rapid", "ripple", "river", "roar", "rose", "rump", "run", "runner", "scar",
        "scratch", "seed", "shade", "shadow", "shell", "shine", "sight", "skip", "sky", "slip", "snout", "snow", "song", "spark",
        "speck", "speckle", "spirit", "splash", "spot", "spots", "spring", "stalk", "stem", "step", "stone", "storm", "streak",
        "stream", "strike", "stripe", "sun", "swipe", "swoop", "talon", "teeth", "thistle", "thorn", "throat", "toe", "tree", 
        "throat", "watcher", "water", "wave", "whisper", "whistle", "willow", "wind", "wing", "wish"
    ]

    pelt_suffixes = {
        'TwoColour': ['patch', 'spot', 'splash', 'patch', 'spots'],
        'Tabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Marbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Speckled': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'Bengal': ['dapple', 'speckle', 'spots', 'speck', 'freckle'],
        'Tortie': ['dapple', 'speckle', 'spot', 'dapple'],
        'Rosette': ['dapple', 'speckle', 'spots', 'dapple', 'freckle'],
        'Calico': ['stripe', 'dapple', 'patch', 'patch'],
        'Smoke': ['fade', 'dusk', 'dawn', 'smoke'],
        'Ticked': ['spots', 'pelt', 'speckle', 'freckle'],
        'Mackerel': ['stripe', 'feather', 'leaf', 'stripe', 'fern'],
        'Classic': ['stripe', 'feather', 'leaf', 'stripe', 'fern'],
        'Sokoke': ['stripe', 'feather', 'leaf', 'stripe', 'fern'],
        'Agouti': ['back', 'pelt', 'fur'],
        'VoiSokoke': ['stripe', 'feather', 'leaf', 'stripe', 'fern'],
        'SpeckledTabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'dapple', 'speckle', 'spot', 'speck', 'freckle', 'stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Stain': ['dapple', 'speckle', 'spot', 'speck', 'freckle']
    }

    tortie_pelt_suffixes = {
        'tortiesolid': ['dapple', 'speckle', 'spots', 'splash'],
        'tortietabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiebengal': ['dapple', 'speckle', 'spots', 'speck', 'fern', 'freckle'],
        'tortiemarbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortieticked': ['spots', 'pelt', 'speckle', 'freckle'],
        'tortiesmoke': ['fade', 'dusk', 'dawn', 'smoke'],
        'tortierosette': ['dapple', 'speckle', 'spots', 'dapple', 'fern', 'freckle'],
        'tortiespeckled': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'tortiemackerel': ['stripe', 'feather', 'fern', 'shade'],
        'tortieclassic': ['stripe', 'feather', 'fern'],
        'tortiesokoke': ['stripe', 'feather', 'fern', 'shade', 'dapple'],
        'tortieagouti': ['back', 'pelt', 'fur', 'dapple', 'splash'],
        'tortievoisokoke': ['stripe', 'feather', 'fern', 'shade', 'dapple'],
        'tortiespeckledtabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern', 'dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'tortiecombo': ['spots', 'speckle', 'speck']
    }

    normal_prefixes = [
        'Acacia', 'Adder', 'Alder', 'Algae', 'Aloe', 'Ant', 'Antler', 'Apple', 'Apricot', 'Arc', 'Arch', 'Aspen', 'Aster', 'Autumn',
        'Badger', 'Barley', 'Basil', 'Bass', 'Bay', 'Bayou', 'Beam', 'Bear', 'Beaver', 'Bee', 'Beech', 'Beetle', 'Berry',
        'Big', 'Birch', 'Bird', 'Bite', 'Bitter', 'Bittern', 'Bleak', 'Blight', 'Blink', 'Bliss', 'Blizzard', 'Bloom',
        'Blossom', 'Blotch', 'Bluebell', 'Bluff', 'Bog', 'Bold', 'Borage', 'Bough', 'Boulder', 'Bounce', 'Bracken', 'Bramble', 
        'Brave', 'Breeze', 'Briar', 'Bright', 'Brindle', 'Bristle', 'Broken', 'Brook', 'Broom', 'Brush', 'Bubble', 'Bubbling', 'Buck',
        'Bug', 'Bumble', 'Burdock', 'Burr', 'Bush', 'Buzzard', 'Carp', 'Cave', 'Cedar', 'Chaffinch', 'Char', 'Chasing', 'Cheetah', 'Cherry',
        'Chestnut', 'Chive', 'Cicada', 'Claw', 'Clay', 'Clear', 'Cliff', 'Clover', 'Coast', 'Cobra', 'Cod', 'Cold', 'Condor', 
        'Cone', 'Conifer', 'Cougar', 'Cow', 'Coyote', 'Crab', 'Crag', 'Crane', 'Creek', 'Cress', 'Crested', 'Cricket', 'Crooked',
        'Crouch', 'Curl', 'Curlew', 'Curly', 'Cypress', 'Dahlia', 'Daisy', 'Damp', 'Dancing', 'Dandelion', 'Dangling', 'Dapple',
        'Dappled', 'Dapples', 'Dawn', 'Day', 'Dead', 'Deer', 'Dew', 'Dewy', 'Doe', 'Dog', 'Down', 'Downy', 'Drake', 'Drift', 
        'Drizzle', 'Drought', 'Dry', 'Duck', 'Dull', 'Dune', 'Dusk', 'Eagle', 'Echo', 'Eel', 'Egret', 'Elder', 'Elm', 
        'Ermine', 'Faded', 'Faded', 'Fading', 'Falcon', 'Fallen', 'Falling', 'Fallow', 'Fawn', 'Feather', 'Fennel', 'Fern', 
        'Ferret', 'Fidget', 'Fierce', 'Fin', 'Finch', 'Fir', 'Fish', 'Flail', 'Flash', 'Flax', 'Fleck', 'Fleet', 'Flicker', 
        'Flight', 'Flint', 'Flip', 'Flood', 'Flower', 'Flutter', 'Fluttering', 'Fly', 'Foam', 'Fog', 'Forest', 'Freckle', 'Fringe',
        'Frog', 'Frond', 'Furled', 'Furze', 'Fuzzy', 'Gale', 'Gander', 'Gannet', 'Garlic', 'Gem', 'Giant', 'Gill', 'Gleam', 'Glow', 'Goose',
        'Gorge', 'Gorse', 'Grass', 'Gravel', 'Grouse', 'Gull', 'Gust', 'Hail', 'Half', 'Hare', 'Harvest',
        'Hatch', 'Haven', 'Hawk', 'Hay', 'Haze', 'Heath', 'Heavy', 'Hedge', 'Hen', 'Heron', 'Hill', 'Hoarse', 'Hollow', 'Holly',
        'Honey', 'Hoot', 'Hop', 'Hope', 'Hornet', 'Hound', 'Iris', 'Ivy', 'Jackdaw', 'Jagged', 'Jay', 'Jump', 'Juniper', 'Kestrel',
        'Kink', 'Kite', 'Lake', 'Lapping', 'Larch', 'Lark', 'Laurel', 'Lavender', 'Leaf', 'Leap', 'Leopard', 'Lichen', 'Light',
        'Lightning', 'Lilac', 'Lily', 'Lion', 'Little', 'Lizard', 'Locust', 'Long', 'Lost', 'Lotus', 'Loud', 'Low', 'Lynx', 
        'Maggot', 'Mallow', 'Mantis', 'Maple', 'Marigold', 'Marsh', 'Marten', 'Meadow', 'Mellow', 'Melting', 'Merry', 'Midge', 
        'Milk', 'Milkweed', 'Mink', 'Minnow', 'Mistle', 'Mite', 'Mock', 'Mole', 'Monkey', 'Moon', 'Moor', 'Morning', 'Moss', 
        'Mossy', 'Moth', 'Mottle', 'Mottled', 'Mouse', 'Mumble', 'Murk', 'Myrtle', 'Nacre', 'Narrow', 'Nectar', 'Needle', 'Nettle',
        'Newt', 'Nut', 'Oat', 'Odd', 'One', 'Orange', 'Osprey', 'Pansy', 'Panther', 'Parsley', 'Partridge', 'Patch', 'Peak', 
        'Pear', 'Peat', 'Perch', 'Petal', 'Pheasant', 'Pigeon', 'Pike', 'Pine', 'Pink', 'Piper', 'Plover', 'Plum', 'Pod',
        'Pond', 'Pool', 'Poppy', 'Posy', 'Pounce', 'Prance', 'Prickle', 'Prim', 'Primrose', 'Puddle', 'Python', 'Quail', 'Quick',
        'Pop', 'Quiet', 'Quill', 'Rabbit', 'Raccoon', 'Ragged', 'Rain', 'Rainswept', 'Rambling', 'Rat', 'Rattle', 'Raven', 'Reed',
        'Ridge', 'Rift', 'Ripple', 'Rising', 'River', 'Roach', 'Rook', 'Root', 'Rose', 'Rosy', 'Rot', 'Rowan', 'Rubble',
        'Running', 'Rush', 'Rye', 'Sage', 'Scar', 'Scorch', 'Sea', 'Sedge', 'Seed', 'Shard', 'Sharp', 'Shattered', 'Sheep', 
        'Shell', 'Shimmer', 'Shining', 'Shivering', 'Short', 'Shred', 'Shrew', 'Shy', 'Silk', 'Silt', 'Skip', 'Sky', 'Slate', 
        'Sleek', 'Sleet', 'Slight', 'Sloe', 'Slope', 'Small', 'Snail', 'Snake', 'Snap', 'Sneeze', 'Snip', 'Snook', 'Soft', 'Song',
        'Sorrel', 'Spark', 'Sparrow', 'Speckle', 'Spider', 'Spike', 'Spire', 'Splash', 'Spot', 'Spotted', 'Spring', 'Spruce', 
        'Squirrel', 'Starling', 'Steam', 'Stem', 'Stoat', 'Stork', 'Stream', 'Strike', 'Stripe', 'Strong', 'Stump', 
        'Stumpy', 'Sunny', 'Swallow', 'Swamp', 'Sweet', 'Swift', 'Sycamore', 'Tall', 'Talon', 'Tangle', 'Tansy', 'Tawny', 'Thistle', 'Thorn',
        'Thrift', 'Thrush', 'Thunder', 'Thyme', 'Tiger', 'Timber', 'Tiny', 'Tip', 'Toad', 'Torn', 'Trout', 'Tuft', 'Tulip', 
        'Tumble', 'Turtle', 'Twisted', 'Vine', 'Vixen', 'Warm', 'Wasp', 'Wave', 'Weasel', 'Web', 'Weed', 'Wet', 'Wheat', 'Whirl', 'Whisker',
        'Whisper', 'Whispering', 'Whistle', 'Whorl', 'Wild', 'Willow', 'Wind', 'Wish', 'Wing', 'Wisteria', 'Wolf', 'Wood', 'Wren', 'Yarrow', 'Yew'
    ]

    colour_prefixes = {
        'WHITE': [
            'White', 'White', 'Pale', 'Snow', 'Cloud', 'Cloudy', 'Milk', 'Hail', 'Frost', 'Frozen', 'Freeze', 'Ice', 'Icy', 'Sheep',
            'Blizzard', 'Flurry', 'Moon', 'Star', 'Light', 'Bone', 'Bright', 'Swan', 'Dove', 'Wooly', 'Wool', 'Cotton', 'Warm', 'Arctic'
        ],
        'PALEGREY': [
            'Grey', 'Silver', 'Pale', 'Light', 'Cloud', 'Cloudy', 'Hail', 'Frost', 'Ice', 'Icy', 'Mouse', 'Bright', "Fog", 'Freeze',
            'Frozen', 'Stone', 'Pebble', 'Dove', 'Sky', 'Cotton', 'Heather', 'Warm', 'Arctic', 'Ashen'
        ],
        'SILVER': [
            'Grey', 'Silver', 'Cinder', 'Ice', 'Icy', 'Frost', 'Frozen', 'Freeze', 'Rain', 'Blue',
            'River', 'Blizzard', 'Flurry', 'Bone', 'Bleak', 'Stone', 'Pebble', 'Heather', 'Warm', 'Arctic'
        ],
        'GREY': [
            'Grey', 'Grey', 'Ash', 'Ashen', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse', 'Smoke', 'Smoky', 'Shadow', "Fog", 'Bone', 
            'Bleak', 'Rain', 'Storm', 'Soot', 'Pebble', 'Mist', 'Misty', 'Heather',
        ],
        'DARKGREY': [
            'Grey', 'Shade', 'Raven', 'Crow', 'Stone', 'Dark', 'Night', 'Cinder', 'Ash', 'Ashen',
            'Smoke', 'Smokey', 'Shadow', 'Bleak', 'Rain', 'Storm', 'Pebble', 'Mist', 'Misty'
        ],
        'GHOST': [
            'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Midnight', 'Bleak', 'Storm', 'Violet', 'Pepper', 'Bat'
        ],
        'PALEGINGER': [
            'Pale', 'Ginger', 'Sand', 'Sandy', 'Yellow', 'Sun', 'Sunny', 'Light', 'Lion', 'Bright',
            'Honey', 'Daisy', 'Warm', 'Robin'
        ],
        'GOLDEN': [
            'Gold', 'Golden', 'Yellow', 'Sun', 'Sunny', 'Light', 'Lightning', 'Thunder',
            'Honey', 'Tawny', 'Lion', 'Dandelion', 'Marigold', 'Warm'
        ],
        'GINGER': [
            'Ginger', 'Ginger', 'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun', 'Sunny', 'Light', 'Primrose', 'Rose',
            'Rowan', 'Fox', 'Tawny', "Plum", 'Orange', 'Warm', 'Burn', 'Burnt', 'Robin', 'Amber'
        ],
        'DARKGINGER': [
            'Ginger', 'Ginger', 'Red', 'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Oak', 'Shade', 'Russet',
            'Rowan', 'Fox', 'Orange', 'Copper', 'Cinnamon', 'Burn', 'Burnt', 'Jasper', 'Robin'
        ],
        'CREAM': [
            'Sand', 'Sandy', 'Yellow', 'Pale', 'Cream', 'Light', 'Milk', 'Fawn',
            'Bone', 'Daisy', 'Branch', 'Warm', 'Robin', 'Almond', 'Acorn'
        ],
        'LIGHTBROWN': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Dusty', 'Sand', 'Sandy', 'Bright', 'Mud',
            'Hazel', 'Vole', 'Branch', 'Warm', 'Robin', 'Almond', 'Acorn', 'Bark'
        ],
        'BROWN': [
            'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Dust', 'Dusty', 'Acorn', 'Mud', 'Deer', 'Fawn', 'Doe', 'Stag',
            'Twig', 'Owl', 'Otter', 'Log', 'Vole', 'Branch', 'Hazel', 'Robin', 'Acorn', 'Bark'
        ],
        'DARKBROWN': [
            'Brown', 'Dark', 'Shade', 'Night', 'Russet', 'Rowan', 'Mud', 'Oak', 'Stag', 'Elk', 'Twig',
            'Owl', 'Otter', 'Log', 'Hickory', 'Branch', 'Robin', 'Bark'
        ],
        'BLACK': [ 'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark', 'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt'],
        'PEACHYELLOW': ['Sand', 'Yellow', 'Pale', 'Cream', 'Light', 'Milk', 'Fawn',
            'Bone', 'Daisy'],
        'MOCHA': ['Bean', 'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag',
            'Acorn', 'Mud', 'Deer', 'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Bright', 'Mud',
            'Hazel', 'Brown', 'Shade', 'Dark', 'Night', 'Russet', 'Rowan', 'Mud'],
        'METALLICBRONZE': ['Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag',
            'Acorn', 'Mud', 'Deer', 'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Bright', 'Mud',
            'Hazel', 'Brown', 'Shade', 'Dark', 'Night', 'Russet', 'Rowan', 'Mud'],
        'WALNUT': ['Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag',
            'Acorn', 'Mud', 'Deer', 'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Bright', 'Mud',
            'Hazel'],
        'FOX': ['Fox', 'Honey',],
        'ESPRESSO': ['Bean', 'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag',
            'Acorn', 'Mud', 'Deer', 'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Bright', 'Mud',
            'Hazel', 'Brown', 'Shade', 'Dark', 'Night', 'Russet', 'Rowan', 'Mud'],
        'PALEORANGE': ['Pale', 'Gold', 'Golden', 'Yellow', 'Sun', 'Light', 'Lightning', 'Thunder', 'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun',
			'Light', 'Rose','Rowan', 'Fox', 'Tawny', 'Plum', 'Red', 'Red', 'Fire', 'Rust', 'Flame', 'Oak', 'Shade', 'Russet','Rowan', 'Fox'],
        'PALECARMINE': ['Pale', 'Gold', 'Golden', 'Yellow', 'Sun', 'Light', 'Lightning', 'Thunder', 'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun',
            'Light', 'Rose','Rowan', 'Fox', 'Tawny', 'Plum', 'Red', 'Red', 'Fire', 'Rust', 'Flame', 'Oak', 'Shade', 'Russet','Rowan', 'Fox'],
        'CARAMEL': ['Gold', 'Golden', 'Yellow', 'Sun', 'Light', 'Lightning', 'Thunder', 'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun',
			'Light', 'Rose','Rowan', 'Fox', 'Tawny', 'Plum', 'Red', 'Red', 'Fire', 'Rust', 'Flame', 'Oak', 'Shade', 'Russet','Rowan', 'Fox'],
        'SIENNA': ['Honey',],
        'VANILLA': ['Sand', 'Yellow', 'Pale', 'Cream', 'Light', 'Milk', 'Fawn',
            'Bone', 'Daisy'],
        'MUSHROOM': ['Sand', 'Yellow', 'Pale', 'Cream', 'Light', 'Milk', 'Fawn',
            'Bone', 'Daisy', 'Mushroom'],
        'COFFEE': ['Bean', 'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag',
            'Acorn', 'Mud', 'Deer'],
        'RICHGOLD': ['Honey', 'Honey', 'Honey', 'Honey', 'Honey', 'Gold', 'Golden', 'Yellow', 'Sun', 'Light', 'Lightning', 'Thunder', 'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun',
			'Light', 'Rose','Rowan', 'Fox', 'Tawny', 'Plum', 'Red', 'Red', 'Fire', 'Rust', 'Flame', 'Oak', 'Shade', 'Russet','Rowan', 'Fox'],
        'MOCCACCINO': ['Bean', 'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag',
            'Acorn', 'Mud', 'Deer'],
        'PALEBROWN': ['Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag',
            'Acorn', 'Mud', 'Deer', 'Brown', 'Shade', 'Dark', 'Night', 'Russet', 'Rowan', 'Mud'],
        'DUSTYPINK': ['Dust', 'Strange', ],
        'GRASSY': ['Moss', 'Mud'],
        'CLOUD': ['Mint', 'White', 'White', 'Pale', 'Snow', 'Cloud', 'Milk', 'Hail', 'Frost', 'Ice', 'Sheep',
			'Blizzard', 'Moon', 'Light', 'Bone''Grey', 'Silver', 'Pale', 'Cloud', 'Hail', 'Frost', 'Ice', 'Mouse', 'Bright', "Fog"
			'Grey', 'Silver', 'Cinder', 'Ice', 'Frost', 'Rain', 'Blue','River', 'Blizzard', 'Bone', 'Icy'
			'Grey', 'Grey', 'Ash', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse','Smoke', 'Shadow', "Fog", 'Bone'],
        'VAMPIRE': ['Grey', 'Shade', 'Raven', 'Crow', 'Stone', 'Dark', 'Night',
            'Smoke', 'Shadow', 'Fang'],
        'DOVE': ['Feather', 'Water', 'Dove',],
        'GRAVEL': ['Grey', 'Shade', 'Raven', 'Crow', 'Stone', 'Dark', 'Night',
            'Smoke', 'Shadow', 'Fang'],
        'SLATEGREY': ['Grey', 'Shade', 'Raven', 'Crow', 'Stone', 'Dark', 'Night',
            'Smoke', 'Shadow', 'Fang'],
        'ICE': ['White', 'White', 'Pale', 'Snow', 'Cloud', 'Milk', 'Hail', 'Frost', 'Ice', 'Sheep',
        	'Blizzard', 'Moon', 'Light', 'Bone''Grey', 'Silver', 'Pale', 'Cloud', 'Hail', 'Frost', 'Ice', 'Mouse', 'Bright', "Fog"
            'Grey', 'Silver', 'Cinder', 'Ice', 'Frost', 'Rain', 'Blue','River', 'Blizzard', 'Bone', 'Icy'
            'Grey', 'Grey', 'Ash', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse','Smoke', 'Shadow', "Fog", 'Bone'],
        'CADETBLUE': ['Blue', 'Feather',],
        'OLDLAVENDER': ['Lavender', 'Flower'],
        'COMET': ['Rock', 'Comet', 'Dragon',],
        'MIDGREY': ['Grey',],
        'IRONGREY': ['Iron',],
        'DUST': ['Grey', 'Shade', 'Raven', 'Crow', 'Stone', 'Dark', 'Night',
            'Smoke', 'Shadow', 'Dusty'],
        'VIOLET': ['Comet'],
        'DARKVIOLET': ['Dragon', 'Comet', 'Violet'],
        'BLUEVIOLET': ['Dragon', 'Comet', 'Violet'],
        'CHARCOAL': ['Grey', 'Shade', 'Raven', 'Crow', 'Stone', 'Dark', 'Night',
            'Smoke', 'Shadow', 'Coal', 'Black', 'Black', 'Shade', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Midnight'],
        'ASH': ['Grey', 'Shade', 'Raven', 'Crow', 'Stone', 'Dark', 'Night',
            'Smoke', 'Shadow',],
        'PALEVIOLET': ['Pale', 'Dragon', 'Comet', 'Violet'],
        'BLACK1': [ 'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark', 'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt'],
        'BLACK2': [ 'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark', 'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt'],
        'BLACK3': [ 'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark', 'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt'],
        'BLACK4': [ 'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark', 'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt'],
        'BLACK5': [ 'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark', 'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt'],
        'BLACK6': [ 'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark', 'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt'],
        'SILVER1': ['Grey', 'Silver', 'Cinder', 'Ice', 'Icy', 'Frost', 'Frozen', 'Freeze', 'Rain', 'Blue', 'River', 'Blizzard', 'Flurry', 'Bone', 'Bleak', 'Stone', 'Pebble', 'Heather', 'Warm', 'Arctic'],
        'SILVER2': ['Grey', 'Silver', 'Cinder', 'Ice', 'Icy', 'Frost', 'Frozen', 'Freeze', 'Rain', 'Blue', 'River', 'Blizzard', 'Flurry', 'Bone', 'Bleak', 'Stone', 'Pebble', 'Heather', 'Warm', 'Arctic'],
        'SILVER3': ['Grey', 'Silver', 'Cinder', 'Ice', 'Icy', 'Frost', 'Frozen', 'Freeze', 'Rain', 'Blue', 'River', 'Blizzard', 'Flurry', 'Bone', 'Bleak', 'Stone', 'Pebble', 'Heather', 'Warm', 'Arctic'],
        'SILVER4': ['Grey', 'Silver', 'Cinder', 'Ice', 'Icy', 'Frost', 'Frozen', 'Freeze', 'Rain', 'Blue', 'River', 'Blizzard', 'Flurry', 'Bone', 'Bleak', 'Stone', 'Pebble', 'Heather', 'Warm', 'Arctic'],
        'SILVER5': ['Grey', 'Silver', 'Cinder', 'Ice', 'Icy', 'Frost', 'Frozen', 'Freeze', 'Rain', 'Blue', 'River', 'Blizzard', 'Flurry', 'Bone', 'Bleak', 'Stone', 'Pebble', 'Heather', 'Warm', 'Arctic'],
        'SILVER6': ['Grey', 'Silver', 'Cinder', 'Ice', 'Icy', 'Frost', 'Frozen', 'Freeze', 'Rain', 'Blue', 'River', 'Blizzard', 'Flurry', 'Bone', 'Bleak', 'Stone', 'Pebble', 'Heather', 'Warm', 'Arctic'],
        'BROWN1': ['Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Dust', 'Dusty', 'Acorn', 'Mud', 'Deer', 'Fawn', 'Doe', 'Stag', 'Twig', 'Owl', 'Otter', 'Log', 'Vole', 'Branch', 'Hazel', 'Robin', 'Acorn', 'Bark'],
        'BROWN2': ['Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Dust', 'Dusty', 'Acorn', 'Mud', 'Deer', 'Fawn', 'Doe', 'Stag', 'Twig', 'Owl', 'Otter', 'Log', 'Vole', 'Branch', 'Hazel', 'Robin', 'Acorn', 'Bark'],
        'BROWN3': ['Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Dust', 'Dusty', 'Acorn', 'Mud', 'Deer', 'Fawn', 'Doe', 'Stag', 'Twig', 'Owl', 'Otter', 'Log', 'Vole', 'Branch', 'Hazel', 'Robin', 'Acorn', 'Bark'],
        'BROWN4': ['Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Dust', 'Dusty', 'Acorn', 'Mud', 'Deer', 'Fawn', 'Doe', 'Stag', 'Twig', 'Owl', 'Otter', 'Log', 'Vole', 'Branch', 'Hazel', 'Robin', 'Acorn', 'Bark'],
        'BROWN5': ['Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Dust', 'Dusty', 'Acorn', 'Mud', 'Deer', 'Fawn', 'Doe', 'Stag', 'Twig', 'Owl', 'Otter', 'Log', 'Vole', 'Branch', 'Hazel', 'Robin', 'Acorn', 'Bark'],
        'BROWN6': ['Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Dust', 'Dusty', 'Acorn', 'Mud', 'Deer', 'Fawn', 'Doe', 'Stag', 'Twig', 'Owl', 'Otter', 'Log', 'Vole', 'Branch', 'Hazel', 'Robin', 'Acorn', 'Bark'],
        }

#        'SKINBLACK': ['Grey', 'Shade', 'Raven', 'Crow', 'Stone', 'Dark', 'Night', 'Night', 'Shadow', 'Scorch', 'Midnight'],
#        'SKINCOFFEE': ['Bean', 'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag', 'Acorn', 'Mud', 'Deer'],
#        'SKINCHOCOLATE': ['Bean', 'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag', 'Acorn', 'Mud', 'Deer'],
#        'SKINGINGER': ['Pale', 'Gold', 'Golden', 'Yellow', 'Sun', 'Light', 'Lightning', 'Thunder', 'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun', 'Light', 'Rose','Rowan', 'Fox', 'Tawny', 'Plum', 'Red', 'Red', 'Fire', 'Rust', 'Flame', 'Oak', 'Shade', 'Russet','Rowan', 'Fox'],
#        'SKINPALEGREY': ['Grey', 'Shade', 'Raven', 'Crow', 'Stone', 'Dark', 'Night', 'Smoke', 'Shadow', 'Dusty'],
#        'SKINPALECOFFEE': ['Bean', 'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag', 'Acorn', 'Mud', 'Deer'],
#        'SKINPALEBROWN': ['Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag', 'Acorn', 'Mud', 'Deer', 'Brown', 'Shade', 'Dark', 'Night', 'Russet', 'Rowan', 'Mud'],
#        'SKINPALECREAMY': ['Sand', 'Yellow', 'Pale', 'Cream', 'Light', 'Milk', 'Fawn', 'Bone', 'Daisy'],
#        'SKINGREY': ['Grey', 'Shade', 'Raven', 'Crow', 'Stone', 'Dark', 'Night', 'Smoke', 'Shadow',],
#        'SKINWHITE': ['White', 'White', 'Pale', 'Snow', 'Cloud', 'Milk', 'Hail', 'Frost', 'Ice', 'Sheep', 'Blizzard', 'Moon', 'Light', 'Bone'],
#        'SKINPINK': ['Pale', 'Gold', 'Golden', 'Yellow', 'Sun', 'Light', 'Lightning', 'Thunder', 'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun', 'Light', 'Rose','Rowan', 'Fox', 'Tawny', 'Plum', 'Red', 'Red', 'Fire', 'Rust', 'Flame', 'Oak', 'Shade', 'Russet','Rowan', 'Fox'],
#        'SKINBROWN': ['Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag', 'Acorn', 'Mud', 'Deer', 'Brown', 'Shade', 'Dark', 'Night', 'Russet', 'Rowan', 'Mud'],

    eye_prefixes = {
        'YELLOW': ['Yellow', 'Moon', 'Daisy', 'Honey', 'Light'],
        'AMBER': ['Amber', 'Sun', 'Fire', 'Gold', 'Honey', 'Scorch'],
        'HAZEL': ['Hazel', 'Tawny', 'Hazel', 'Gold', 'Daisy', 'Sand'],
        'PALEGREEN': ['Pale', 'Green', 'Mint', 'Fern', 'Weed', 'Olive'],
        'GREEN': ['Green', 'Fern', 'Weed', 'Holly', 'Clover', 'Olive'],
        'BLUE': ['Blue', 'Blue', 'Ice', 'Sky', 'Lake', 'Frost', 'Water', 'Sea'],
        'DARKBLUE': ['Dark', 'Blue', 'Sky', 'Lake', 'Berry', 'Water', 'Deep'],
        'GREY': ['Grey', 'Stone', 'Silver', 'Ripple', 'Moon', 'Rain', 'Storm', 'Heather'],
        'CYAN': ['Sky', 'Blue', 'River', 'Rapid', 'Sea'],
        'EMERALD': ['Emerald', 'Green', 'Shine', 'Blue', 'Pine', 'Weed'],
        'PALEBLUE': ['Pale', 'Blue', 'Sky', 'River', 'Ripple', 'Day', 'Cloud', 'Sea'],
        'PALEYELLOW': ['Pale', 'Yellow', 'Sun', 'Gold', 'Ray'],
        'GOLD': ['Gold', 'Golden', 'Sun', 'Amber', 'Sap', 'Honey'],
        'HEATHERBLUE': ['Heather', 'Blue', 'Lilac', 'Rosemary', 'Lavender', 'Wisteria'],
        'COPPER': ['Copper', 'Red', 'Amber', 'Brown', 'Fire', 'Cinnamon', 'Jasper'],
        'SAGE': ['Sage', 'Leaf', 'Olive', 'Bush', 'Clove', 'Green', 'Weed'],
        'BLUE2': ['Blue', 'Blue', 'Ice', 'Icy', 'Sky', 'Lake', 'Frost', 'Water'],
        'SUNLITICE': ['Sun', 'Ice', 'Icy', 'Frost', 'Sunrise', 'Dawn', 'Dusk', 'Odd', 'Glow'],
        'GREENYELLOW': ['Green', 'Yellow', 'Tawny', 'Hazel', 'Gold', 'Daisy', 'Sand', 'Sandy', 'Weed']
    }

    loner_names = [
        "Abyss", "Ace", "Ah" ,"Alcina", "Alec", "Alice", "Amber", "Amity", "Amy", "Angel", "Anita", "Ankh", "Anubis", "Armin", "April", "Ash",
        "Aurora", "Azula", "Aries", "Aquarius", "Bagel", "Bailey", "Bandit", "Baphomet", "Bastet", "Bean", "Beanie Baby", "Beans", "Bede",
        "Belle", "Benny", "Bently", "Bentley", "Beverly", "Big Man", "Birb", "Blu",  "Bluebell", "Bologna", "Bolt", "Bonbon", "Bongo", "Bonnie",
        "Bonny", "Boo", "Broccoli", "Buddy", "Bumblebee", "Bunny", "Burger", "Burm", "Bub", "Cake", "Callie", "Calvin", "Caramel", "Carmen", 
        "Carmin", "Carolina", "Caroline", "Carrie", "Catie", "Cat", "Catty", "Chance", "Chanel", "Chansey", "Chaos", "Charles", "Charlie", "Charlotte",
        "Charm", "Chase", "Cheese", "Cheesecake", "Cheeto", "Cheetoman", "Chef", "Cherry", "Chester", "Chewie", "Chewy", "Chicco", "Chief", "Chinook",
        "Chip", "Chloe", "Chocolate", "Chocolate Chip", "Chris", "Chrissy", "Cinder", "Cinderblock", "Cloe", "Cloud", "Cocoa", "Cocoa Puff", "Coffee",
        "Conan", "Cookie", "Coral", "Cosmo", "Cowbell", "Cowboy", "Crab", "Cracker", "Cream", "Crispy", "Crow", "Crunchwrap", "Crunchy", "Cupcake", "Cooper",
        "Cancer", "Capricorn", "Dakota", "Dan", "Dave", "Deli", "Delilah", "Della", "Delta", "Dewey", "Dirk", "Dog", "Doggo", "Dolly", "Donald", "Dragonfly", "Dreamy", "Duchess", "Dune",
        "Dunnock" "Eclipse", "Daisy Mae",  "Eda", "Eddie", "Eevee", "Egg", "Ember", "Emerald", "Emi", "Emma", "Emy", "Erica", "Espresso", "Eve", "Evelyn", "Evie",
        "Evilface", "Erebus", "Fallow", "Fang", "Fawn", "Feather", "Felix", "Fern", "Ferret", "Ferry", "Finch", "Firefly", "Fishleg", "Fishtail", "Fiver", "Flabby",
        "Flower", "Fluffy", "Flutie", "Fork", "Frank", "Frankie", "Frannie", "Fred", "Freddy", "Free", "French", "French Fry", "Frito", "Fry", "Frye", "Gamble", 
        "Gargoyle", "Garnet", "Geode", "George", "Ghost", "Gibby", "Gir", "Gizmo", "Glass", "Glory", "Goose", "Grace", "Grain", "Grasshopper", "Gravy", "Guinness",
        "Gust", "Gwendoline", "Gwynn", "Gemini", "Habanero", "Hamilton", "Haku", "Harvey", "Havoc", "Herc", "Hercules", "Hiccup", "Holly", "Hop", "Hot Sauce", "Hotdog",
        "Hughie", "Human", "Hunter", "Harlequin", "Ice", "Icecube", "Ice Cube", "Icee", "Igor", "Ike", "Indi", "Insect", "Isabel", "Jack", "Jade", "Jaiden",
        "Jake", "James", "Jasper", "Jaxon", "Jay", "Jenny", "Jesse", "Jessica", "Jester", "Jethro", "Jewel", "Jewels", "Jimmy", "Jinx", "John", "Johnny",
        "Jellybean", "Joker", "Jolly", "Jolly Rancher", "Joob", "Jubie", "Judas", "Jude", "Judy", "Juliet", "June", "Jupiter", "KD", "Kate", "Katy", "Kelloggs", "Ken",
        "Kendra", "Kenny", "Kermit", "Kerry", "Ketchup", "King", "Kingston", "Kip", "Kisha", "Kitty", "Kitty Cat", "Klondike", "Knox", "Kodiak", "Kong", "L", "Lacy",
        "Lakota", "Laku", "Lee", "Lemon", "Leo", "Leon", "Lester", "Lex", "Lilith", "Lily", "Lily", "Loaf", "Lobster", "Lola", "Loona", "Lora", "Louie", "Louis", "Lucky",
        "Lucy", "Lugnut", "Luigi", "Luke", "Luna", "Lupo", "Loyalty", "Libra", "Madi", "Makwa", "Maleficent", "Manda", "Mange", "Mango", "Marceline", "Matcha",
        "Maverick", "Max", "May", "McChicken", "McFlurry", "Meatlug", "Melody", "Menopause", "Meow-Meow", "Meowyman", "Mera", "Mew", "Miles", "Millie", "Milo",
        "Milque", "Mimi", "Minette", "Mini", "Minna", "Minnie", "Mint", "Minty", "Missile Launcher", "Mitski", "Mittens", "Mocha", "Mocha", "Mojo", "Mollie",
        "Molly", "Molly Murder Mittens", "Monika", "Monster", "Monte", "Monzi", "Moon", "Mop", "Moxie", "Mr. Kitty", "Mr. Kitty Whiskers", "Mr. Whiskers",
        "Mr. Wigglebottom", "Mucha", "Murder", "Mushroom", "Mitaine", "Myko", "Neel", "Nagi", "Nakeena", "Neil", "Nemo", "Nessie", "Nick", "Nightmare", "Nikki",
        "Niles", "Ninja", "Nintendo", "Nisha", "Nitro", "Noodle", "Norman" "Nova", "Nugget", "Nuggets", "Nuka", "Nutella", "O'Leary", "Oakley", "Oapie", "Obi Wan",
        "Old Man Sam", "Oleander", "Olga", "Oliver", "Oliva", "Ollie", "Omelet", "Onyx", "Oops", "Ophelia", "Oreo", "Orion", "Oscar", "Owen", "Peach", "Peanut",
        "Peanut Wigglebutt", "Pear", "Pearl", "Pecan", "Penny", "Peony", "Pepper", "Pichi", "Pickles", "Pikachu", "Ping", "Ping Pong",
        "Pip", "Piper", "Pipsqueak", "Pocket", "Poki", "Polly", "Pong", "Poopy", "Porsche", "Potato", "Prickle", "Princess", "Pumpernickel", "Punk", "Purdy",
        "Purry", "Pisces", "Pushee", "Quagmire", "Quake", "Queen", "Queenie", "Queeny", "Queso", "Queso Ruby", "Quest", "Quickie", "Quimby",
        "Quinn", "Quino", "Quinzee", "Quesadilla", "Ramble", "Randy", "Rarity", "Rat", "Ray", "Reese", "Reeses Puff", "Ren", "Rio", "Riot", "River",
        "Riya", "Rocket", "Rolo", "Roman", "Roomba", "Rooster", "Rory", "Rose", "Roselie", "Ruby", "Rudolph", "Rue", "Ruffnut", "Rum", "Sadie", "Saki",
        "Salmon", "Salt", "Sam", "Samantha", "Sandwich", "Sandy", "Sausage", "Schmidt", "Scotch", "Scrooge", "Seamus", "Sekhmet", "Seri", "Shampoo", "Shay",
        "Shimmer", "Shiver", "Silva", "Silver", "Skrunkly", "Sloane", "Slug", "Slushie", "Smoothie", "Smores", "Smudge", "Sneakers", "Snek", "Snotlout", "Socks", "Soda",
        "Sofa", "Sol", "Sonic", "Sophie", "Sorbet", "Sox", "Spam", "Sparky", "Spots", "Stan", "Star", "Starfish", "Stella", "Steve", "Steven", "Stinky",
        "Stolas", "Stripes", "Sundae", "Sunny", "Sunset", "Sweet", "Sweetie", "Scorpio", "Sagittarius", "Tabatha", "Tabby", "Tabbytha", "Taco", "Taco Bell",
        "Tasha", "Tempest", "Tetris", "Teufel", "Tiny", "Toast", "Toffee", "Tom", "Tomato", "Tomato Soup", "Toni", "Toothless", "Torque", "Tortilla", 
        "Treasure", "Triscuit", "Trixie", "Trouble", "Tucker", "Tuffnut", "Tumble", "Turbo", "Twilight", "Twister", "Twix", "Toastee", "Taurus", "Ula", "Union",
        "Uriel", "Vanilla", "Vaxx", "Velociraptor", "Venture", "Via", "Vida", "Viktor", "Vinnie", "Vinyl", "Violet", "Vivienne", "Void", "Voltage", "Vox", "Virgo", "Wanda", "Washington", "Webby",
        "Wendy", "Whiskers", "Whisper", "Wigglebutt", "Windy", "Wishbone", "Whiskey", "Wisp", "Wisteria", "Worm", "X'ek", "Zelda", "Zim", "Zoe"
    ]

    if os.path.exists('saves/prefixlist.txt'):
        with open('saves/prefixlist.txt', 'r') as read_file:
            name_list = read_file.read()
            if_names = len(name_list)
        if if_names > 0:
            new_names = name_list.split('\n')
            for new_name in new_names:
                if new_name != '':
                    normal_prefixes.append(new_name)

    if os.path.exists('saves/suffixlist.txt'):
        with open('saves/suffixlist.txt', 'r') as read_file:
            name_list = read_file.read()
            if_names = len(name_list)
        if if_names > 0:
            new_names = name_list.split('\n')
            for new_name in new_names:
                if new_name != '':
                    normal_suffixes.append(new_name)

    def __init__(self,
                 status="warrior",
                 prefix=None,
                 suffix=None,
                 colour=None,
                 eyes=None,
                 pelt=None,
                 tortiepattern=None):
        self.status = status
        self.prefix = prefix
        self.suffix = suffix
        
        # Set prefix
        if prefix is None:
            named_after_appearance = not random.getrandbits(3)  # Chance for True is '1/8'.
            # Add possible prefix categories to list.
            possible_prefix_categories = []
            if eyes in self.eye_prefixes:
                possible_prefix_categories.append(self.eye_prefixes[eyes])
            if colour in self.colour_prefixes:
                possible_prefix_categories.append(self.colour_prefixes[colour])
            # Choose appearance-based prefix if possible and named_after_appearance because True.
            if named_after_appearance and possible_prefix_categories:
                prefix_category = random.choice(possible_prefix_categories)
                self.prefix = random.choice(prefix_category)
            else:
                self.prefix = random.choice(self.normal_prefixes)
                    
        # Set suffix
        while self.suffix is None or self.suffix == self.prefix.casefold() or str(self.suffix) in self.prefix.casefold() and not str(self.suffix) == '':
            if pelt is None or pelt == 'SingleColour':
                self.suffix = random.choice(self.normal_suffixes)
            else:
                named_after_pelt = not random.getrandbits(3) # Chance for True is '1/8'.
                # Pelt name only gets used if there's an associated suffix.
                if (named_after_pelt
                    and pelt in ["Tortie", "Calico"]
                    and tortiepattern in self.tortie_pelt_suffixes):
                    self.suffix = random.choice(self.tortie_pelt_suffixes[tortiepattern])
                elif named_after_pelt and pelt in self.pelt_suffixes:
                    self.suffix = random.choice(self.pelt_suffixes[pelt])
                else:
                    self.suffix = random.choice(self.normal_suffixes)

    def __repr__(self):
        if self.status in self.special_suffixes:
            return self.prefix + self.special_suffixes[self.status]
        else:
            return self.prefix + self.suffix



names = Name()
