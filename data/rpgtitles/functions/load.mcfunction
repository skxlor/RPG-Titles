scoreboard objectives add gamerule.repeatBossTitles trigger
scoreboard objectives add gamerule.repeatDimensionTitles trigger
scoreboard objectives add gamerule.showCurrentBiome trigger

scoreboard objectives add rpgtitles.dummy dummy
execute unless score #firstload rpgtitles.dummy matches 1.. run tellraw @a {"text":"You have RPG Titles by IzukiKa installed!"}
scoreboard players set #firstload rpgtitles.dummy 1
scoreboard players set #2 rpgtitles.dummy 2

function rpgtitles:main