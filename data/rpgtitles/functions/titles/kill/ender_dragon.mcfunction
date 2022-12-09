execute unless entity @s[tag=rpgtitles.killedEnderDragon] run title @s title {"text":"[Dragon Slain]","color": "gold","bold": true}
execute if entity @s[tag=rpgtitles.killedEnderDragon] if score @s gamerule.repeatBossTitles matches 1 run title @s title {"text":"[Dragon Slain]","color": "gold","bold": true}
tag @s add rpgtitles.killedEnderDragon
advancement revoke @s only rpgtitles:entity/kill/ender_dragon