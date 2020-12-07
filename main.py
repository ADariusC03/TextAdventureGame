print("Welcome   ")
print('')

name = input('What is your name? ')
age = int(input('What is your age, to futher continue with the game? '))

health = 20

weapon = "knife"

rifle = 4

if age >= 18:
  print('Nice! Your Old Enough So Lets Have Some Fun!! But Wait...')

  wants_to_play = input('Do you want to play? ').lower()
  if wants_to_play == 'yes':
    print('You are starting with', health, 'health.')
    print("Let's begin to play!")
    print('')

    choice = input('You are walking down a long road and come across a fork in the road. you have two paths but One choice to make what do you pick. Left or Right (left/right) ')
    if choice == 'left':
      ans = input("You walk the left path, a gentle breeze and sun comes out. Walking along the path you see a villiage. Do you want to head that way or keep going? (village/walk) ")
      print('')

      if ans == 'village':
        print('You walk into the village, but strange you see nobody. Looks more like a ghost town. Your walking around and you see a house with the door open. Walking closer a horrible smell hits you...of dead flesh!! You walk inside and see a couple of bandits. Trying to move backwards slowly you slip on blood and pass out. ')
        print('')
      elif ans == 'walk':
        print(' You continue to walk along the mysterious road. Minding your business until you hear someone riding a horse behind you. You turn around to look and *BAM* Your knocked unconsious. You lost 5 health. ')
        print('')
        health -= 5

      answer = input(' You wake up to notice a bag is over your head with you hands tied behind the chair your sitting in. Noises of footstep leave from the room. Do you try to escape or do nothing? (nothing/escape) ')
      print('')

      if answer == 'nothing':
        print('20 minutes passes and random footsteps come in. Many people are asking you questions and shouting until its complete silence and BOOM ... shotgun shot in the chest. ')
        print('')
        health -= 15
        if health <= 0:
          print('You have 0 health left ... GAME OVER!! ')
        else:
          print('You survived the shot, left for dead they untie you and leave you with the other bodies. Left alone you stagger getting up looking for an escape route. ')
          print('')
      elif answer == 'escape':
        print('You stand up with the chair over your back and you leap backwards to break the chair. Free; you get your hands over your legs and lift the bag off to see yourself in a room full of dead bodies in a basement. Looking at the sharp edge of the broken chair you saw the tape of your hands free. ')
        print('')

      free = input('Looking around you see a window and a path that leads up staris. Which path do you choose? (window/upstairs) ')
      print('')

      if free == 'window':
        print('Standing on the piles of bodies, You lift up the basement window. Climbing out, you get up off the ground to where you make eye contact with a bandit. Alerting the others, you run into the woods.')
        print('')
      elif free == 'upstairs':
        print('Before going upstairs you grab a', weapon, 'and start creeping upstairs. You notice a bandit at the top of the stairs and you strike him. AHHHHHH, with a loud scream another bandit comes. Shooting you drop the ', weapon, 'before you make it out the house to run into the woods. You lose 5 health. ')
        print('')
        health -= 5
        if health <= 0:
          print('You have 0 health left ... GAME OVER!! ')
        else:
          print('In the tall grass you stop to check your wound and its nun major, you will survive. ')
          print('')

      woods = input('Inside the woods. You hear many footsteps approaching your way along with dogs barking. You continue running until you come across a lake. Do you Swim or Go Another Way? (Swim/GAW). ').lower()
      print('')

      if woods == 'swim':
        print('You go into the water and take a deep dive submerging into the lake to be undetected in the water. Bandits come to the lake; Looking around and turn back. You see an electric eel curl around your leg as you try to swim. Shocking you, you lose 5 health. ')
        print('')
        health -= 5
        if health <= 0:
          print('You have 0 health left ... GAME OVER!! ')
        else:
          print('You survived the shock. Swimming up the lake to the other side. Drying yourself off, you make your way deeper into the woods. ')
          print('')
      elif woods == 'gaw':
        print('You look left and see a bridge. Running on the bridge it collaspes behind you. Enraged bandits starts shooting and yelling, as you make your getaway to the other side. Deeper into the woods you go. ')
        print('')

      cabin = input('Exhausted from running through the woods all night. you stumble upon a cabin in the woods. Do you choose to enter or stay outside? (Enter/Outside) ').lower()
      print('')

      if cabin == 'enter':
        print('You walk in and search the fridge for food. You are full. You fall asleep on the couch. You gain 5 health. ')
        print('')
        health += 5
      elif cabin == 'outside': 
        print('You decide to sleep outside. Hungry and cold during the night you lose 5 heath. ')
        print('')
        health -= 5
        if health <= 0:
          print('You have 0 health left ... GAME OVER!! ')
        else:
          print('You wake up, feeling warm but stanky. A skunk sprayed you when you startled it with your snoring. Time to man up and go inside so you can take a shower.')
          print('')
        
        hide = input('After a long night of hunting. Six cultist make there way to the cabin. All carrying bags of unknown items. You hear footsteps approaching the cabin. And right before they enter do you hide or greet them? (hide/greet) ').lower()
        print('')

        if hide == 'greet':
            print('You stand there and wave Hello to them. THe six cultist look at you crazy and start shooting up the place. Two bullets graze you as you run amongst the place. Lost 5 health. ')
            print('')
            health -= 5
            if health <= 0:
              print('You have 0 health left ... GAME OVER!! ')
            else:
              print('Hurt, but not calling quits. You grab a weapon before jumping out the window. ')
            print('')
        elif hide == 'hide':
          print('You hide under the table behind the table cloth as soon as they walk in. Three head to the kitchen and two more go into the bedroom. Dropping bags on the table you smell rotten flesh as before. One guy places his gun against the table before leaving to the bathroom. You grab the gun and sneak out to the front door until the bathroom guy alerts the other the front door is open and his gun is gone. ')
          print('')

        shot = input('Outside you scrimmage around to find a safe hiding place and vantage point. You climb up a tree and down below two men are close by looking for you. Do you shoot or stay quiet? (shoot/quiet) ').lower()
        print('')

        if shot == "shoot":
          print('You line up the rifle to get a good shot. One cultist leaves to check somewhhere else and 1 minutes after .. BAM one shot fired off at the cultist near you to the head. Time to climb down and move to another spot.')
          print('')
          rifle -= 1
        elif shot == "quiet":
          print('You sneak around through the tall grass. Making sure your not seen by the enemy. As they walk one way you crawl another.  ')
          print('')

        gen = input('Still hiding you crawl and come across an abandoned campfire. Do you create an diversion or look for supplies? (diversion/supply) ').lower()

        if gen == 'diversion':
          print('Gathering small twigs, dry leaves and forest duff. You see lighter fuel and a match and start a fire. Minutes later after creating a smoke signal two cultist show up. in the tall grass you line up shot on one and BANG. Through the neck one falls as the other start shooting in panic. ')
          print('')
          rifle -= 1
        elif gen == 'supply':
          print('You ramage through the tents and find nothing. Only shelter for the time being until one cultist peeks in and gets startled to see you there. Before he could grab his gun you shoot and kill him. Running out the tent you spot another one and aim and shoot. BANG through the head.')
          print('')
          rifle -= 2

        fire = input('Running through the tall grass towards the cabin, again. You mistakenly ran in a circle. Footsteps are approaching quickly, will you fight or hide again? (fight/hide) ').lower()
        print('')

        if fire == 'fight':
          print('You stand ground to face three more cultist. BANG! BANG! two drop as one shot you thru the shoulder. You lose 5 health.')
          print('')
          health -= 5
          rifle -= 2
          if rifle <= 0:
            print('You ran outta bullets.')
          else:
            print('You have', rifle, 'amount of bullets left.')

            if health <= 0:
              print('You have 0 health left ... GAME OVER!! ')
            else:
              print('Hurt, but not calling quits. You toss the weapon at the emeny and grab their knife to cut there throat before they could aim. ')
          print('')


        elif fire == 'hide':
          print('Cowarding with a gun in your hand ... You make your way into the rotting smelling cabin only to hide into the bedroom. Doors lock. The cultist Run in the house banging and knocking on the door. You open the window and jump out only to get a good angle on them through the dinning room window. Firing off two shots each BANG BANG!')
          print('')
          rifle -= 2
          if rifle <= 0:
            print('You ran outta bullets.')
          else:
            print('You have', rifle, 'amount of bullets left. Now to find another weapon.')

        come_back = input('With two cultist left hot on your trail. You decide to head into the woods again and futher on with your escape without being seen. Shortly, night falls and you come out of the woods to see an unmarked park car. Do you go to car or keep walking? (car/walk) ').lower()
        print('')

        if come_back == 'car':
          print('You go inside the car and see the keys in the ignition. Cranking the car up you blow up into pieces. ')
          print('')
          health -= 15
          if health <= 0:
            print('You have 0 health left ... GAME OVER!! ')
          else:
            print('You must can escape death itself with your luck.')
        elif come_back == 'walk':
          print('You walk the lonely, dark road until the suns comes up. You see a sign that says Welcome to Atlantic City.')

        trap = input('Making it across city lines. You travel farther unto the road to see your home close by. Making final steps you approach the yard. Do you walk towards the house or go to a diner to eat? (home/diner) ').lower()

        if trap == 'home':
          print('You walk onto the lawn and without knowing you trigger a bomb. You put the key into the key hole to unlock the door and BOOMMM! ')
          health -= 10
          if health <= 0:
            print('Your health is 0. You died a horrible. death. GAME OVER!!!')
          else:
            print('You have major luck on your side. I like your skills.' )
        elif trap == 'diner':
          print('You look closer at the ground and see a trip wire and decides to go somewhhere else. Hungry you decied to go to a diner.')

        winner = input('Walking to the diner you walk inside and other a All-Star Platter with coffee to perk you up. After a long few days of surviving you deserve this break in life to relax and kick back. For A NEW Journey Awaits. (Done/Credit) ').lower()

        if winner == 'done':
          print('Thank You For Playing!! Hope To See You Again!! Cya!!')
        elif winner == 'credit':
          print(' Special Thanks To', name, 'for playing the game all the way through and not giving up. Luck was on your side. Thank You!!!!')



    else:
      print('You went right, walking for until the sun went down. You stepped into the meadow grass and BOOM!! You blew up by a land mine.... You Lost. ')


  else:
    print("Come back when your ready.")
else:
  print('Sorry Come Back When Your Older...')

