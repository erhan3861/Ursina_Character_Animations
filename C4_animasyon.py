from ursina import *
from direct.actor.Actor import Actor
from ursina.shaders import lit_with_shadows_shader
from random import randint, uniform # randint -> random integer   uniform-> float

Entity.default_shader = lit_with_shadows_shader

def input(key):
    if key == "space":
        actor.loop("Walk")

def update():
    if held_keys["w"]:
        if actor.getCurrentAnim() == "Run":   # Şu anki animasyon ismini al
            player.position -= player.forward * time.dt * 20
        elif actor.getCurrentAnim() in ["Walk", "Roll"] :
            player.position -= player.forward * time.dt * 8

    # rotasyon
    if held_keys["a"]:
        player.rotation_y -= 100 * time.dt # fps den bağımsız oluyor -> time.dt

    if held_keys["d"]:
        player.rotation_y += 100 * time.dt
    
    # altınları toplama
    for coin in coin_list:
        coin.rotation_y += time.dt * 50 # altınları sağ-sol oalrak döndür
        if distance(player, coin) < 2: # eğer player ve altın arası uzaklık 2 birimden az ise
            coin_list.remove(coin) # listeden çıkar
            coin.fade_out(duration=1) # altını 1 sn'de gözden kaybet

    # kameranın oyuncuyu takip etmesi
    cam.position = player.position + Vec3(0, 10, -5)

app = Ursina()

btn_idle = Button("IDLE", scale=.1, x = 0.8, y = -0.2)
btn_idle.on_click = lambda : actor.loop("Idle")

btn_run = Button("RUN", scale=.1, x = 0.8, y = 0)
btn_run.on_click = lambda : actor.loop("Run") # anim name

btn_walk = Button("WALK", scale=.1, x = 0.8, y = 0.2)
btn_walk.on_click = lambda : actor.loop("Walk")

btn_die = Button("DIE", scale=.1, x = 0.8, y = 0.4)
btn_die.on_click = lambda : actor.loop("Death")

# sol taraf butonları
btn_roll = Button("ROLL", scale=.1, x = -0.8, y = -0.2)
btn_roll.on_click = lambda : actor.loop("Roll")

btn_pickUp = Button("PICK UP", scale=.1, x = -0.8, y = 0)
btn_pickUp.on_click = lambda : actor.loop("PickUp")

btn_attack = Button("ATTACK", scale=.1, x = -0.8, y = 0.2)
btn_attack.on_click = lambda : actor.loop("Dagger_Attack")

btn_hit = Button("HIT", scale=.1, x = -0.8, y = 0.4)
btn_hit.on_click = lambda : actor.loop("RecieveHit_Attacking")

player = Entity(unlit = True) # oyuncuya ışık etkisi verme

# animasyonu entitiye ekleme
actor = Actor("assets/character.gltf")
actor.reparentTo(player) # animasyonları playere yükledik

print(actor.getAnimNames()) # animasyonların isimlerini getir

ground = Entity(model="plane", scale=400, texture="shore")

coin_list = []

for i in range(20):
    coin = Entity(model="coin", scale=10, x=randint(-50, 50), y=uniform(0.5, 1.5), z=randint(-50,50), unlit=True)
    coin_list.append(coin)

sun = DirectionalLight()
sun.look_at((-1, -1, 1))

cam = EditorCamera()

app.run()