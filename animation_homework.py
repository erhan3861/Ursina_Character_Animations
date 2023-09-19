from ursina import *
from direct.actor.Actor import Actor
from ursina.shaders import lit_with_shadows_shader

Entity.default_shader = lit_with_shadows_shader

def update():
    if held_keys["w"]:
        if "Walk" in actor.getAnimNames() and actor.getCurrentAnim() != "Walk":
            actor.loop("Walk")
        player.position -= player.forward * time.dt * 8

    elif held_keys["s"]:
        if "Walk" in actor.getAnimNames() and actor.getCurrentAnim() != "Walk":
            actor.loop("Walk")
        player.position += player.forward * time.dt * 8

    elif held_keys["r"]:
        if "Run" in actor.getAnimNames() and actor.getCurrentAnim() != "Run":
            actor.loop("Run")
        player.position -= player.forward * time.dt * 20

    elif held_keys["f"]:
        if "Roll" in actor.getAnimNames() and actor.getCurrentAnim() != "Roll":
            actor.loop("Roll")
        player.position -= player.forward * time.dt * 8

    else:
        if "Idle" in actor.getAnimNames() and actor.getCurrentAnim() != "Idle":
            actor.loop("Idle")

    if held_keys["a"]:
        player.rotation_y -= 200 * time.dt
    if held_keys["d"]:
        player.rotation_y += 200 * time.dt
    
    cam.position = player.position + Vec3(0, 5, 48)
    rotate_camera()

def rotate_camera():
    camera.rotation_y = 180 

app = Ursina()

player = Entity(unlit=True)
actor = Actor("assets/character.gltf")
actor.reparentTo(player)
print(actor.getAnimNames())

Entity(model="plane",scale=400,texture="grass")

sun = DirectionalLight()
sun.look_at((-1, -1, 1))

Sky()
cam = EditorCamera()

app.run()
