from ursina import *
from direct.actor.Actor import Actor
from ursina.shaders import lit_with_shadows_shader

Entity.default_shader = lit_with_shadows_shader

def input(key):
    if key == "space":
        actor.loop('Walk') 

def update():
    if held_keys["w"] and actor.getCurrentAnim() in ["Walk", "Run", "CharacterArmature|Roll"]: # şu anki animasyonu
        if actor.getCurrentAnim() == "Run": # oyuncu koşuyorsa
            player.position -= player.forward * time.dt * 20
        else:
            player.position -= player.forward * time.dt * 8

    if held_keys["a"]:
        player.rotation_y -= 100 * time.dt

    if held_keys["d"]:
        player.rotation_y += 100 * time.dt

    # cam.position = player.position + Vec3(0, 6, -3)

    # coin işlemleri
    for coin in coinlist:
        coin.rotation_y += time.dt * 50
        if distance(player, coin) < 2: # oyuncunun coine mesafesi
            coinlist.remove(coin)
            coin.fade_out(duration=3) # 3 sn sonra gözden kaybolur

app = Ursina()
# Right side
btn_idle = Button("IDLE", scale=.1, x=0.8, y=-0.2)
btn_idle.on_click = lambda : actor.loop("Idle")

btn_run = Button("RUN", scale=.1, x=0.8, y=0)
btn_run.on_click = lambda : actor.loop("Run")

btn_walk = Button("WALK", scale=.1, x=0.8, y=0.2)
btn_walk.on_click = lambda : actor.loop("Walk")

btn_die = Button("DIE", scale=.1, x=0.8, y=0.4)
btn_die.on_click = lambda : actor.loop("CharacterArmature|Death")

# left side
btn_roll = Button("ROLL", scale=.1, x=-0.8, y=-0.2)
btn_roll.on_click = lambda : actor.loop("CharacterArmature|Roll")

btn_pickUp = Button("Pick Up", scale=.1, x=-0.8, y=0)
btn_pickUp.on_click = lambda : actor.loop("PickUp")

btn_attack = Button("Attack", scale=.1, x=-0.8, y=0.2)
btn_attack.on_click = lambda : actor.loop("Dagger_Attack")

btn_hit = Button("HIT", scale=.1, x=-0.8, y=0.4)
btn_hit.on_click = lambda : actor.loop("RecieveHit_Attacking")

player = Entity(unlit=True) # gölge verme

# animasyon ekleme
actor = Actor("assets/character_light3.gltf")
actor.reparentTo(player)

print(actor.getAnimNames())

ground = Entity(model="plane", scale=300, texture="shore")

coin1 = Entity(model="coin", scale=5, x=5, y=1, z=5, unlit=True) # unlit değeri modeldeki gölgeyi siler
coin2 = Entity(model="coin", scale=5, x=-5, y=1.5, z=5, unlit=True) 
coin3 = Entity(model="coin", scale=5, x=5, y=1.3, z=-5, unlit=True) 
coin4 = Entity(model="coin", scale=5, x=15, y=1.3, z=-7, unlit=True) 
coin5 = Entity(model="coin", scale=5, x=20, y=1.3, z=10, unlit=True) 
coinlist = [coin1, coin2, coin3, coin4, coin5]

cam = EditorCamera()

sun = DirectionalLight() # yön verilmiş ışık
sun.look_at((-1, -2, 1)) # bu konuma bak

app.run()