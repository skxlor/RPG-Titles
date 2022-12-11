scoreboard players enable @s gamerule.repeatBossTitles 
scoreboard players enable @s gamerule.repeatDimensionTitles 
scoreboard players enable @s gamerule.showCurrentBiome 

scoreboard players operation @s gamerule.repeatBossTitles %= #2 rpgtitles.dummy
scoreboard players operation @s gamerule.repeatDimensionTitles %= #2 rpgtitles.dummy
scoreboard players operation @s gamerule.showCurrentBiome %= #2 rpgtitles.dummy

execute if score @s gamerule.showCurrentBiome matches 1 run function rpgtitles:titles/biome/show