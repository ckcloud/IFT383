#!/usr/bin/python
#==============================================================================
# pokemon.py
# By -READACTED-
# Extra Credit script submission
# ASU - Professor -REDACTED-
# Imports csv file with pokemon info and runs some metrics against it
# My son loves pokemon, so I had to do this one for him
# Sources:
# https://www.asciiart.eu/video-games/pokemon
# https://pokemondb.net/pokedex/national
# https://docs.python.org/3/library/csv.html
# https://stackoverflow.com/a/44690120
# 
#==============================================================================

# importing csv module 
import csv 
import random
def Header():
    print("="*80 + "\n")
    print("                                  ,'\\\n"+
    "    _.----.        ____         ,'  _\\   ___    ___     ____\n" +
    "_,-'       `.     |    |  /`.   \\,-'    |   \\  /   |   |    \\  |`.\n"+
    "\\      __    \\    '-.  | /   `.  ___    |    \\/    |   '-.   \\ |  |\n" +
    " \\.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \\|  |\n"+
    "   \\    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |\n"+
    "    \\     ,-'/  / \\ \\    ,'   | \/ / ,`.|         /  / \\ \\  |     |\n"+
    "     \\    \\ |   \\_/  |   `-.  \\    `'  /|  |    ||   \\_/  | |\\    |\n"+
    "      \\    \\ \\      /       `-.`.___,-' |  |\  /| \\      /  | |   |\n"+
    "       \\    \\ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |\n"+
    "        \\_.-'       |__|    `-._ |              '-.|     '-.| |   |\n"+
    "                                `'                            '-._|\n")
    print("="*80 + "\n")
    # that was fun, now on to the menu...what do I want to do?
def Border():
    print("")
    print("*"*80)

Header()
menuIn = 99
statTrackerDef = {'Normal': 0, 'Fire': 0, 'Water': 0, 'Grass': 0, 'Electric': 0, 'Ice': 0, \
    'Fighting': 0, 'Poison': 0, 'Ground': 0, 'Flying': 0, 'Psychic': 0, 'Bug': 0, 'Rock': 0, \
    'Ghost': 0, 'Dark': 0, 'Dragon': 0, 'Steel': 0, 'Fairy': 0}

while menuIn != 0:
    
    with open('pokemon.csv', 'r') as csvfile: # Opens the pokemon csv file and while it's still open runs the main program
        pkmnList = csv.DictReader(csvfile)
        menuIn = input("Pokemon Information Program:\n1: Random Pokemon\n2: List of Pokemon by Type\n" + 
        "3: List of Pokemon by Generation\n4: List of Starter Pokemon by Generation\n5: Stat Sorter: Find the Highest Stats\n" +
        "6: List of Legendary Pokemon\n7: Count the Pokemon by Type\n8: Statistics\n9: See the Logo Again\n" +
        "10: See My Gen 1 Squad\nMake a Selection (or press 0 to exit): ")
        if menuIn == 1:         # randomizer
            Border()
            num = 0
            num = random.randint(1,721)
            for row in pkmnList:
                if row['#'] == str(num):
                    print row['#'], row['Name']
            Border()
        if menuIn == 2:         # Asks the user to pick a type and searches for matching pokemon
            listDict = {1: 'Normal', 2: 'Fire', 3: 'Water', 4: 'Grass', 5: 'Electric', 6: 'Ice', 7: 'Fighting', \
                8: 'Poison', 9: 'Ground', 10: 'Flying', 11: 'Psychic', 12: 'Bug', 13: 'Rock', 14: 'Ghost' ,\
                15: 'Dark', 16: 'Dragon', 17: 'Steel', 18: 'Fairy'}
            Border()
            newType = 0
            newType = input("Available Types: \n1: Normal\t2: Fire\t3: Water\t4: Grass\n" +
                "5: Electric\t6: Ice\t7: Fighting\t8: Poison\n" + 
                "9: Ground\t10: Flying\t11: Psychic\t12: Bug\n" +
                "13: Rock\t14: Ghost\t15: Dark\t16: Dragon\n" +
                "17: Steel\t18: Fairy\n Select a number to see the Pokemon with the primary type: ")
            for row in pkmnList:
                if row['Type 1'] == listDict[newType]:
                    print row['#'], row['Name']
            Border()
        if menuIn == 3:         # Asks the user to pick a gen number and searches for matching pokemon
            Border()
            newGen = 0
            newGen = input("List of Pokemon by Generation:\nEnter a Generation Number (1 - 6): ")
            for row in pkmnList:
                if int(row['Generation']) == newGen:
                    print row['Name']
            Border()
        if menuIn == 4:         # Finds the three starting pokemon for each generation (and pikachu)
            Border()
            newGen = 0
            newGen = input("List of Starter Pokemon by Generation:\nEnter a Generation Number (1 - 6): ")
            if newGen == 1:
                for row in pkmnList:
                    if int(row['#']) == 1 or int(row['#']) == 4 or int(row['#']) == 7 or int(row['#']) == 25:
                        print row['#'], row['Name']
            if newGen == 2:
                for row in pkmnList:
                    if int(row['#']) == 152 or int(row['#']) == 155 or int(row['#']) == 158:
                        print row['#'], row['Name']
            if newGen == 3:
                for row in pkmnList:
                    if int(row['#']) == 252 or int(row['#']) == 255 or int(row['#']) == 258:
                        print row['#'], row['Name']
            if newGen == 4:
                for row in pkmnList:
                    if int(row['#']) == 387 or int(row['#']) == 390 or int(row['#']) == 393:
                        print row['#'], row['Name']
            if newGen == 5:
                for row in pkmnList:
                    if int(row['#']) == 495 or int(row['#']) == 498 or int(row['#']) == 501:
                        print row['#'], row['Name']
            if newGen == 6:
                for row in pkmnList:
                    if int(row['#']) == 650 or int(row['#']) == 653 or int(row['#']) == 656:
                        print row['#'], row['Name']
            Border()
        if menuIn == 5:         # Finds the Pokemon with highest/lowest stats
            Border()
            # Total, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed
            stats = {'TotalHi': 0, 'TotalLow': 0, 'HPHi': 0, 'HPLow': 0, 'AttackHi': 0, 'AttackLow': 0, \
                'DefHi': 0, 'DefLow': 0, 'SpAtkHi': 0, 'SpAtkLow': 0, 'SpDefHi': 0, 'SpDefLow': 0, 'SpeedHi': 0, 'SpeedLow': 0}
            print("Stat Sorter: Finding the Highest (and Lowest) Stats...\n")
            for row in pkmnList:
                if int(row['Total']) > stats['TotalHi'] or stats['TotalHi'] == 0:
                    TotalHiPKMN = [row['Name'], row['Total']]
                    stats['TotalHi'] = int(row['Total'])
                if int(row['Total']) < stats['TotalLow'] or stats['TotalLow'] == 0:
                    TotalLowPKMN = [row['Name'], row['Total']]
                    stats['TotalLow'] = int(row['Total'])
                if int(row['HP']) > stats['HPHi'] or stats['HPHi'] == 0:
                    HPHiPKMN = [row['Name'], row['HP']]
                    stats['HPHi'] = int(row['HP'])
                if int(row['HP']) < stats['HPLow'] or stats['HPLow'] == 0:
                    HPLowPKMN = [row['Name'], row['HP']]
                    stats['HPLow'] = int(row['HP'])
                if int(row['Attack']) > stats['AttackHi'] or stats['AttackHi'] == 0:
                    AttackHiPKMN = [row['Name'], row['Attack']]
                    stats['AttackHi'] = int(row['Attack'])
                if int(row['Attack']) < stats['AttackLow'] or stats['AttackLow'] == 0:
                    AttackLowPKMN = [row['Name'], row['Attack']]
                    stats['AttackLow'] = int(row['Attack'])
                if int(row['Defense']) > stats['DefHi'] or stats['DefHi'] == 0:
                    DefHiPKMN = [row['Name'], row['Defense']]
                    stats['DefHi'] = int(row['Defense'])
                if int(row['Defense']) < stats['DefLow'] or stats['DefLow'] == 0:
                    DefLowPKMN = [row['Name'], row['Defense']]
                    stats['DefLow'] = int(row['Defense'])
                if int(row['Sp. Atk']) > stats['SpAtkHi'] or stats['SpAtkHi'] == 0:
                    SpAtkHiPKMN = [row['Name'], row['Sp. Atk']]
                    stats['SpAtkHi'] = int(row['Sp. Atk'])
                if int(row['Sp. Atk']) < stats['SpAtkLow'] or stats['SpAtkLow'] == 0:
                    SpAtkLowPKMN = [row['Name'], row['Sp. Atk']]
                    stats['SpAtkLow'] = int(row['Sp. Atk'])
                if int(row['Sp. Def']) > stats['SpDefHi'] or stats['SpDefHi'] == 0:
                    SpDefHiPKMN = [row['Name'], row['Sp. Def']]
                    stats['SpDefHi'] = int(row['Sp. Def'])
                if int(row['Sp. Def']) < stats['SpDefLow'] or stats['SpDefLow'] == 0:
                    SpDefLowPKMN = [row['Name'], row['Sp. Def']]
                    stats['SpDefLow'] = int(row['Sp. Def'])
                if int(row['Speed']) > stats['SpeedHi'] or stats['SpeedHi'] == 0:
                    SpeedHiPKMN = [row['Name'], row['Speed']]
                    stats['SpeedHi'] = int(row['Speed'])
                if int(row['Speed']) < stats['SpeedLow'] or stats['SpeedLow'] == 0:
                    SpeedLowPKMN = [row['Name'], row['Speed']]
                    stats['SpeedLow'] = int(row['Speed'])
            print("Pokemon with Highest Total: %s, with %s.") %(TotalHiPKMN[0],TotalHiPKMN[1])
            print("Pokemon with Lowest Total: %s, with %s.")%(TotalLowPKMN[0],TotalLowPKMN[1])
            print("Pokemon with Highest HP: %s, with %s.") %(HPHiPKMN[0],HPHiPKMN[1])
            print("Pokemon with Lowest HP: %s, with %s.")%(HPLowPKMN[0],HPLowPKMN[1])
            print("Pokemon with Highest Attack: %s, with %s.") %(AttackHiPKMN[0],AttackHiPKMN[1])
            print("Pokemon with Lowest Attack: %s, with %s.")%(AttackLowPKMN[0],AttackLowPKMN[1])
            print("Pokemon with Highest Defense: %s, with %s.") %(DefHiPKMN[0],DefHiPKMN[1])
            print("Pokemon with Lowest Defense: %s, with %s.")%(DefLowPKMN[0],DefLowPKMN[1])
            print("Pokemon with Highest Sp. Attack: %s, with %s.") %(SpAtkHiPKMN[0],SpAtkHiPKMN[1])
            print("Pokemon with Lowest Sp. Attack: %s, with %s.")%(SpAtkLowPKMN[0],SpAtkLowPKMN[1])
            print("Pokemon with Highest Sp. Defense: %s, with %s.") %(SpDefHiPKMN[0],SpDefHiPKMN[1])
            print("Pokemon with Lowest Sp. Defense: %s, with %s.")%(SpDefLowPKMN[0],SpDefLowPKMN[1])
            print("Pokemon with Highest Speed: %s, with %s.") %(SpeedHiPKMN[0],SpeedHiPKMN[1])
            print("Pokemon with Lowest Speed: %s, with %s.")%(SpeedLowPKMN[0],SpeedLowPKMN[1])
            Border()

        if menuIn == 6:         # Searches for legendary Pokemon
            Border()
            countLegend = 0
            print ("Finding Legendary Pokemon...")
            for row in pkmnList:
                if row['Legendary'] == 'True':
                    print row['#'], row['Name']
                    countLegend += 1
            print("Done. Found %i legendary Pokemon.")%(countLegend)
            Border()
        if menuIn == 7:         # returns a list of primary types with number of matching pkmn
            Border()
            print("Counting Pokemon by Primary Type (Type 1)...")
            statTracker = statTrackerDef.copy()
            for row in pkmnList:
                statTracker[row['Type 1']] +=1
            print("Done! The count of each Pokemon by type is:")
            for types, count in sorted(statTracker.iteritems()):  
                print("{} ({})".format(types, count))
            Border()
        if menuIn == 8:         # presents a sampling of statistics on PKMN to user
            menu2 = 99
            Border()
            while menu2 != 0:
                menu2 = input("Statistics Menu\n1: Legendary Pokemon Stats\n2: Primary Type Stats\n3: Generation 1 Stats\n" +
                    "Please enter your selection (or 0 to return to main): ")
                if menu2 == 0:
                    Border()
                if menu2 == 1:
                    Border()
                    tSpeed = 0
                    tTotal = 0
                    lCount = 0
                    for row in pkmnList:
                        if row['Legendary'] == 'True':
                            tSpeed += int(row['Speed'])
                            tTotal += int(row['Total'])
                            lCount += 1
                    avgSpeed = tSpeed / lCount
                    avgTotal = tTotal / lCount
                    print("The average speed of a legendary Pokemon is: %i")%(avgSpeed)
                    print("The average Total rating of a legendary Pokemon is: %i")%(avgTotal)
                    menu2 = 0       # My loops won't re-run unless I exit to main menu
                    Border()
                if menu2 == 2:            # the type with the highest ___ is ___
                    Border()
                    # Defense
                    defTracker = statTrackerDef.copy()
                    defHi = ["",0]
                    # Attack
                    atkTracker = statTrackerDef.copy()
                    atkHi = ["",0]
                    # Speed
                    spdTracker = statTrackerDef.copy()
                    spdHi = ["",0]
                    # Total
                    totalTracker = statTrackerDef.copy()
                    totalHi = ["",0]
                    # Counter
                    statCounter = statTrackerDef.copy()
                    for row in pkmnList:
                        defTracker[row['Type 1']] += int(row['Defense'])
                        atkTracker[row['Type 1']] += int(row['Attack'])
                        spdTracker[row['Type 1']] += int(row['Speed'])
                        totalTracker[row['Type 1']] += int(row['Total'])
                        statCounter[row['Type 1']] += 1
                    # iterate through the dictionaries and compute averages
                    for types, count in sorted(statCounter.iteritems()):  
                        print("{} ({})".format(types, count))
                    for key in statCounter:
                        defTracker[key] = defTracker[key] / statCounter[key]
                        atkTracker[key] = atkTracker[key] / statCounter[key]
                        spdTracker[key] = spdTracker[key] / statCounter[key]
                        totalTracker[key] = totalTracker[key] / statCounter[key]
                    # iterate through averages and find highest value for each average
                    for key in statCounter:
                        if defTracker[key] > defHi[1] or defHi[1] == 0:
                            defHi[0] = str(key)
                            defHi[1] = defTracker[key]
                        if atkTracker[key] > atkHi[1] or atkHi[1] == 0:
                            atkHi[0] = str(key)
                            atkHi[1] = atkTracker[key]
                        if spdTracker[key] > spdHi[1] or spdHi[1] == 0:
                            spdHi[0] = str(key)
                            spdHi[1] = spdTracker[key]
                        if totalTracker[key] > totalHi[1] or totalHi[1] == 0:
                            totalHi[0] = str(key)
                            totalHi[1] = totalTracker[key]
                    # Display results
                    print("The type with the highest average Defense rating is %s, with %s")%(defHi[0], defHi[1])
                    print("The type with the highest average Attack rating is %s, with %s")%(atkHi[0], atkHi[1])
                    print("The type with the highest average Speed rating is %s, with %s")%(spdHi[0], spdHi[1])
                    print("The type with the highest average Total rating is %s, with %s")%(totalHi[0], totalHi[1])
                    Border()
                    menu2 = 0       # My loops won't re-run unless I exit to main menu
                if menu2 == 3: # We checked Attack, Defense, Speed, and Total by type above, let's check the specials
                    Border()
                    # Sp Def
                    spDefTracker = statTrackerDef.copy()
                    spDefHi = ["", 0]
                    # Sp Atk
                    spAtkTracker = statTrackerDef.copy()
                    spAtkHi = ["", 0]
                    #counter
                    spCounter = statTrackerDef.copy()
                    for row in pkmnList:
                        if row['Generation'] == '1':
                            spDefTracker[row['Type 1']] += int(row['Sp. Def'])
                            spAtkTracker[row['Type 1']] += int(row['Sp. Atk'])
                            spCounter[row['Type 1']] += 1
                    for key in spCounter:
                        if spCounter[key] > 0: # Gen 1 PKMN don't cover every type as a primary
                            spDefTracker[key] = spDefTracker[key] / spCounter[key]
                            spAtkTracker[key] = spAtkTracker[key] / spCounter[key]
                    for key in spCounter:
                        if spDefTracker[key] > spDefHi[1] or spDefHi[1] == 0:
                            spDefHi[0] = str(key)
                            spDefHi[1] = spDefTracker[key]
                        if spAtkTracker[key] > spAtkHi[1] or spAtkHi[1] == 0:
                            spAtkHi[0] = str(key)
                            spAtkHi[1] = spAtkTracker[key]
                    print("The Gen 1 type with the highest average Special Defense rating is %s, with %s")%(spDefHi[0], spDefHi[1])
                    print("The Gen 1 type with the highest average Special Attack rating is %s, with %s")%(spAtkHi[0], spAtkHi[1])
                    menu2 = 0       # My loops won't re-run unless I exit to main menu
                    Border()
        if menuIn == 9:
            Header()
        if menuIn == 10:
            Border()
            crew = [6, 26, 65, 94, 130, 143]
            # I went to the Indigo Plateau with this crew several times
            for row in pkmnList:
                for member in crew:
                    if row['#'] == str(member) and not 'Mega' in row['Name']: # There were no Mega PKMN in the Game Boy game
                        print row['#'], row['Name']
            Border()
# The End
# Thank you