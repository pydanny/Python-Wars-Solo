import stuff
import random
import hashlib
import sys

def main():

    enemies = 'arrogance,killer,demon,evil,slaughter,monster,couch,tempest,bunny'.split(',')

    name = 'Pythonista'
    while True:
         zargons = input('How many Zargons can you handle (1-9)? ')
         try:
              zargons = int(zargons)
         except:
              print('Use numbers!  No special characters or letters or stuff!')
              continue
         if zargons < 1 or zargons > 9:
              print('Thats not between 1 and 9 Zargons!')
              continue

         break

    uni = stuff.Universe()
    uni.me = stuff.Cruiser(name)
    count = 0
    for enemy in range(zargons):
         title = enemies[count].capitalize()
         id = hashlib.md5((title + str(count)).encode('utf-8')).hexdigest()
         setattr(uni,id,stuff.Frigate(title,id,count * 10))
         count += 1


    turn = 0
    while True:



         print('*' * 80)
         print('Turn',turn + 1)
         print('*' * 80)

         #list enemies
         print('Enemies    Shields  Defense')


         short_names = {}
         win = True
         hero = True
         zargons = 0
         for ship in uni.list_ships():

              if ship.side == 'good': continue
              zargons += 1
              win = False
              short_names[ship.title[0].lower()] = ship
              ship.recharge()
              name = '(' + ship.title[0] + ')' + ship.title[1:]
              if ship.shields == 30:
                remaining = str(100)
              else:
                remaining = str((ship.shields / ship.max_shields) * 100)[:2]
              pad = ''
              for i in range(12-len(name)): pad += ' '
              print('%s %s  %s%% -    %s' % (name,pad,remaining,ship.dv))

              if turn:
                action = random.randrange(2)
                if action == 0:
                     hero = ship.pulsar.action(ship,uni.me)
                     if not hero:
                          print('SHIP DESTROYED!!!')
                          print('You lose!!!')
                          print('You lose!!!')
                          print('You lose!!!')
                          sys.exit()

                else:
                     print(' %s coming about for optimal firing position' % ship.title)
                     ship.recharge()




         if win:
              print('You win!!!')
              print('You win!!!')
              print('You win!!!')
              sys.exit()


         #list my ship

         for i in range(2): print('='*80)
         print('The Good Ship', uni.me.title)
         print('Shields:', uni.me.shields)

         while True:
              target = input('Who is your target? ').lower()
              try:
                target = short_names[target]
                break
              except:
                if target == 'exit':
                    return
                print('No Zargon uses that designation')
         print('Target:',target.title)
         print('Fire (S)pinal Mount - Capacitor at %s %%' % uni.me.spinal_mount.capacitor)
         if uni.me.missile.ammo:
              print('Fire (M)issle - %s missiles remaining' % uni.me.missile.ammo)
         print('Use (D)amage Control')

         action = input('What is your action? ').lower()
         if action == 's':
              print('Spinal Mount', target.title)
              survived = uni.me.spinal_mount.action(uni.me,target)
              if not survived:
                delattr(uni,target.id)
         elif action == 'm' and uni.me.missile.ammo:
              print('Missile', target.title)
              survived = uni.me.missile.action(uni.me,target)
              if not survived:
                delattr(uni,target.id)
         elif action == 'd':
              for i in range(random.randrange(zargons)+1):
                uni.me.damage_control()
                uni.me.recharge()
              print('Damage control report:')
              print(' Spinal Mount:', uni.me.spinal_mount.capacitor)
              print(' Shields:', uni.me.shields)
         elif action == 'exit':
              return

         uni.me.recharge()
         turn += 1

if __name__ == "__main__":
    main()
