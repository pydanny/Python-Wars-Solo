import random
import operator

tab = ' '

class Universe(object):
    """ Container for ships """
    def __init__(self):
        self.dtype = 'universe'

    def list_ships(self):
        ships = []
        for local in self.__dict__.keys():
            local = self.__dict__[local]
            if hasattr(local,'dtype'):
                if local.dtype == 'Ship':
                    ships.append(local)
        ships.sort(key=operator.attrgetter('title'))
        return ships

class Ship(object):
    """ The big ship object """

    def __init__(self):
        self.dtype = 'Ship'
        self.shields = 0
        self.max_shields = 0
        self.alive = True
        self.title = ''


    def take_damage(self, damage):
        self.shields -= damage
        if self.shields < 1:
            print(tab + self.title, 'Destroyed!!!')
            self.alive = False
            return self.alive
        remaining = str(self.shields / self.max_shields * 100)[:2]

        print('%s%s shields down to %s%%.' % (tab,self.title,remaining))
        return self.alive

class Component(object):
    """ Parts of the ship """

    def __init__(self):
        self.dtype = 'Component'
    def action(self):
        pass

class Spinal_Mount(Component):
    """ Big honking laster """

    def __init__(self):
        self.av = 0
        self.dv = 0
        self.volume = 1
        self.capacitor = 100
        self.max_capacitor = 100
        self.recharge_capacitor = 10
        self.range = 15
        self.option = 'Fire (S)pinal Mount'

    def recharge(self):

        self.capacitor = min(self.max_capacitor, self.capacitor + self.recharge_capacitor)

    def action(self,me=None,enemy=None):
        print(tab + 'Firing Spinal Mount!')
        hit = False
        energy = 0
        survived = True
        for laser in range(10):
            energy = (laser + 1) ** 2
            if energy > self.capacitor:
                print(tab + 'Spinal Mount out of juice')
                break
            if not hit:
                av = random.randrange(me.av + self.av + laser)
                dv = random.randrange(enemy.dv)
                if av > dv:
                    hit = True
                else:
                    print(tab + 'Spinal Mount missed')
            if hit:
                print(tab + 'Spinal Mount locked on')
                survived = enemy.take_damage(random.randrange(10)+1)
            if not survived:
                break

        self.capacitor -= energy
        print(tab + 'Spinal mount firing sequence over.'        )
        return survived


class Pulsar(Component):
    def __init__(self):
        self.av = 0
        self.dv = 0
        self.volume = 1
        self.range = 5
        self.option = 'Fire (P)ulsar'

    def action(self,me=None,enemy=None):
        print(tab + me.title + ' firing Pulsar!')
        av = random.randrange(me.av + self.av)
        dv = random.randrange(enemy.dv)
        return enemy.take_damage(10)


class Missile(Component):
    def __init__(self):
        self.av = 20
        self.dv = 0
        self.damage = 'd2'
        self.volume = 1
        self.range = 10
        self.ammo = 5
        self.option = 'Fire (M)issile'

    def action(self,me=None,enemy=None):
        if self.ammo == 0:
            print(tab + 'Out of missiles.')
            return True
        print(tab + 'Launching missile!')
        self.ammo -= 1
        av = random.randrange(me.av + self.av)
        dv = random.randrange(enemy.dv)
        if av < dv:
            print(tab + 'Missile missed'        )
            return True
        print(tab + 'Missile hit!!!'                    )
        damage = (random.randrange(10) + 1) * (random.randrange(10) + 1)
        return enemy.take_damage(damage)

class ECM(Component):
    def __init__(self):
        self.av = 0
        self.dv = 40
        self.volume = 1
        self.option = '(E)CM'

    def action(self,me=None,enemy=None):
        return True

class Frigate(Ship):
    def __init__(self,name='',id='',dv=None):
        Ship.__init__(self)
        self.title = name
        self.id = id
        self.av = 40
        if dv:
            self.dv = dv
        else:
            self.dv = 1 + (random.randrange(10) * random.randrange(10))
        self.volume = 2
        self.shields = 30.0
        self.max_shields = 30.0
        self.recharge_shields = 3
        self.thrust = 8
        self.pulsar = Pulsar()
        self.ecm = ECM()
        self.side = 'bad'

    def recharge(self):
        self.shields = min(self.shields + self.recharge_shields, self.max_shields)

class Cruiser(Ship):
    def __init__(self,name='',id=''):
        Ship.__init__(self)
        self.title = name
        self.id = id
        self.av = 20
        self.dv = 10
        self.volume = 3
        self.shields = 100.0
        self.max_shields = 100.0
        self.recharge_shields = 1
        self.thrust = 5
        self.spinal_mount = Spinal_Mount()
        self.missile = Missile()
        self.ecm = ECM()
        self.side = 'good'

    def recharge(self):
        self.shields = min(self.shields + self.recharge_shields, self.max_shields)
        self.spinal_mount.recharge()

    def damage_control(self):
        self.shields = min(self.shields + 10, self.max_shields)
