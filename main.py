import tcod
from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler


def main() -> None:
    # screen size
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 50
    # Using font
    tileset = tcod.tileset.load_tilesheet(
        "chars.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}
    game_map = GameMap(map_width, map_height)
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)
    # Create window
    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Your rogalik",
            vsync=True,
    ) as context:
        # create console
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            # actually put the “@” symbol on the screen in its proper place
            engine.render(console=root_console, context=context)
            # Update window
            events = tcod.event.wait()
            engine.handle_events(events)


if __name__ == "__main__":
    main()
