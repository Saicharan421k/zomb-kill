Snippet 1: The Backend (Paste this where it says [INSERT CODE SNIPPET HERE: The Python psutil script Kiro generated])
Python

import psutil

def scan_for_monsters():
    dungeon = []
    # Scan system for processes consuming resources
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            # Memory usage in MB becomes Health Points
            ram_usage = proc.info['memory_info'].rss / (1024 * 1024)
            
            monster = {
                "id": proc.info['pid'],
                "monster_type": proc.info['name'],
                "health_points": int(ram_usage),
                "status": "ZOMBIE" if proc.status() == psutil.STATUS_ZOMBIE else "ALIVE"
            }
            dungeon.append(monster)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass # Some ghosts cannot be seen
            
    return dungeon



Snippet 2: The UI Logic (Paste this where it says [INSERT CODE SNIPPET HERE: The PyGame rendering loop Kiro generated])
Python

# Kiro generated this game loop using the PyGame docs context
running = True
while running:
    screen.fill((10, 10, 10)) # Dark mode background
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if we clicked (shot) a zombie
            mouse_pos = pygame.mouse.get_pos()
            for z_sprite in zombie_group:
                if z_sprite.rect.collidepoint(mouse_pos):
                    # KILL THE PROCESS
                    psutil.Process(z_sprite.pid).terminate()
                    play_shotgun_sound()
                    z_sprite.kill() # Remove from screen

    # Update and draw the undead horde
    zombie_group.update()
    zombie_group.draw(screen)
    pygame.display.flip()
