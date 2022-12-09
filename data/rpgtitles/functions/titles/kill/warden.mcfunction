execute unless entity @s[tag=rpgtitles.killedWarden] run title @s title {"text":"[Titan Slain]","color": "gold","bold": true}
execute if entity @s[tag=rpgtitles.killedWarden] if score @s gamerule.repeatBossTitles matches 1 run title @s title {"text":"[Titan Slain]","color": "gold","bold": true}
tag @s add rpgtitles.killedWarden
advancement revoke @s only rpgtitles:entity/kill/warden