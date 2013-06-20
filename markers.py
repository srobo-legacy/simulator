from game_object import GameObject
from sr.vision import create_marker_info_by_type, MARKER_TOKEN, MARKER_ARENA

class Token(GameObject):
    surface_name = 'token.png'
    grabbable = True

    def __init__(s, arena, number):
        GameObject.__init__(s, arena)
        s.marker_info = create_marker_info_by_type(MARKER_TOKEN, number)

    def grab(s):
        s.surface_name = 'token_grabbed.png'

    def release(s):
        s.surface_name = 'token.png'

class WallMarker(GameObject):
    surface_name = 'wall_marker.png'

    def __init__(s, arena, number, location=(0,0), heading=0):
        GameObject.__init__(s, arena)
        s.marker_info = create_marker_info_by_type(MARKER_ARENA, number)
        s.location = location
        s.heading = heading
