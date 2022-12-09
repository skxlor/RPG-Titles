execute unless entity @s[tag=rpgtitles.killedWither] run title @s title {"text":"[Abomination Slain]","color": "gold","bold": true}
execute if entity @s[tag=rpgtitles.killedWither] if score @s gamerule.repeatBossTitles matches 1 run title @s title {"text":"[Abomination Slain]","color": "gold","bold": true}
tag @s add rpgtitles.killedWither
advancement revoke @s only rpgtitles:entity/kill/wither