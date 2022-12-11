execute unless entity @s[tag=rpgtitles.vistedEnd] run title @s title {"text":"The End","color": "dark_purple","bold": true}
execute if entity @s[tag=rpgtitles.vistedEnd] if score @s gamerule.repeatDimensionTitles matches 1 run title @s title {"text":"The End","color": "dark_purple","bold": true}
tag @s add rpgtitles.vistedEnd
advancement revoke @s only rpgtitles:dimension/the_end