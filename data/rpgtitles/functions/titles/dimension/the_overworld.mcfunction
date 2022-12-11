execute unless entity @s[tag=rpgtitles.vistedOverworld] run title @s title {"text":"The Overworld","color": "dark_green","bold": true}
execute if entity @s[tag=rpgtitles.vistedOverworld] if score @s gamerule.repeatDimensionTitles matches 1 run title @s title {"text":"The Overworld","color": "dark_green","bold": true}
tag @s add rpgtitles.vistedOverworld
advancement revoke @s only rpgtitles:dimension/the_overworld