from NAME import Room
from NAME import objetos

def test_room():
    gold = Room("GoldRoom", """This room has gold it you can grab. There's a door  to the north.""")
    assert gold.name == "GoldRoom"
    assert gold.paths == {}

def test_room_paths():
    center = Room("Center", "Test room in the center")
    north = Room ("North", "Tests room in the north")
    south = Room("South", "Test room in the south")

    center.add_paths({'north': north, 'south': south})
    assert center.go('north') == (north, "Test room in the center")
    assert center.go('south') == (south, "Test room in the center")

def test_map():
    start = Room("Start", "You can go west and down a hole")
    west = Room("Trees", "There are threes here, you can go east.")
    down = Room("Dougeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})
    movimiento, description_1= start.go('west')
    movimiento_1, description_2 = start.go('down')

    recompensa_start = start.inspeccion()
    recompensa_west = west.inspeccion()
    recompensa_down = down.inspeccion()


    assert recompensa_start in start.recompensa
    assert recompensa_west in west.recompensa
    assert recompensa_down in down.recompensa
    assert start.go('west') == (west, "You can go west and down a hole") and start.name == "Start"
    assert movimiento.go('east') == (start, "There are threes here, you can go east.") and west.name == "Trees"
    assert movimiento_1.go('up') == (start, "It's dark down here, you can go up.") and down.name == "Dougeon"
