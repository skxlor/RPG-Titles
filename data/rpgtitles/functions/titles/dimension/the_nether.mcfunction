execute unless entity @s[tag=rpgtitles.vistedNether] run title @s title {"text":"The Nether","color": "dark_red","bold": true}
execute if entity @s[tag=rpgtitles.vistedNether] if score @s gamerule.repeatDimensionTitles matches 1 run title @s title {"text":"The Nether","color": "dark_red","bold": true}
tag @s add rpgtitles.vistedNether
advancement revoke @s only rpgtitles:dimension/the_nether