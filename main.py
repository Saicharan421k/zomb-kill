import pygame
import psutil
import random
import sys
import math

# --- CONFIGURATION ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (10, 15, 20)  # Dark Blue/Black
ZOMBIE_COLOR = (50, 205, 50)  # Lime Green
TEXT_COLOR = (0, 255, 0)      # Hacker Green
BLOOD_COLOR = (138, 3, 3)

# --- INITIALIZE PYGAME ---
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zomb-Kill: Process Hunter")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Courier New", 14, bold=True)
big_font = pygame.font.SysFont("Courier New", 30, bold=True)

class Zombie(pygame.sprite.Sprite):
    def __init__(self, process):
        super().__init__()
        self.pid = process['pid']
        self.name = process['name']
        self.ram = process['ram']
        
        # Create a "Zombie" visually (a blocky green sprite)
        self.image = pygame.Surface((40, 60))
        self.image.fill(ZOMBIE_COLOR)
        
        # Add 'eyes' to make it look like a monster
        pygame.draw.rect(self.image, (255, 0, 0), (8, 10, 8, 8))  # Left Eye
        pygame.draw.rect(self.image, (255, 0, 0), (24, 10, 8, 8)) # Right Eye
        
        self.rect = self.image.get_rect()
        
        # Spawn at random location
        self.rect.x = random.randint(50, SCREEN_WIDTH - 50)
        self.rect.y = random.randint(100, SCREEN_HEIGHT - 100)
        
        # Movement speed depends on PID (pseudo-random behavior)
        self.speed_x = random.choice([-2, -1, 1, 2])
        self.speed_y = random.choice([-2, -1, 1, 2])

    def update(self):
        # Move the zombie
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Bounce off walls
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top < 50 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed_y *= -1

def get_processes():
    """Scans system for processes using psutil."""
    process_list = []
    try:
        # Iterate over processes
        for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
            try:
                # Filter: Only show processes using > 50MB RAM to avoid clutter
                mem_mb = proc.info['memory_info'].rss / (1024 * 1024)
                if mem_mb > 50:
                    process_list.append({
                        'pid': proc.info['pid'],
                        'name': proc.info['name'],
                        'ram': int(mem_mb)
                    })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    except Exception as e:
        print(f"Error scanning processes: {e}")
    
    # Limit to 10 random zombies to keep game playable
    if len(process_list) > 10:
        return random.sample(process_list, 10)
    return process_list

def draw_ui(screen, score, killed_count):
    # Draw Top Bar
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, SCREEN_WIDTH, 50))
    pygame.draw.line(screen, TEXT_COLOR, (0, 50), (SCREEN_WIDTH, 50), 2)
    
    score_text = font.render(f"RAM SAVED: {score} MB", True, TEXT_COLOR)
    kill_text = font.render(f"ZOMBIES KILLED: {killed_count}", True, TEXT_COLOR)
    
    screen.blit(score_text, (20, 15))
    screen.blit(kill_text, (SCREEN_WIDTH - 200, 15))

def main():
    running = True
    all_sprites = pygame.sprite.Group()
    zombies = pygame.sprite.Group()
    
    # Initial Scan
    procs = get_processes()
    for p in procs:
        z = Zombie(p)
        all_sprites.add(z)
        zombies.add(z)
        
    total_ram_saved = 0
    zombies_killed = 0
    
    print("Zomb-Kill Started... Hunting processes.")

    while running:
        # 1. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # SHOOT!
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in zombies if s.rect.collidepoint(pos)]
                
                for z in clicked_sprites:
                    # KILL THE PROCESS (Simulated for safety in demo mode)
                    # To make it real, uncomment: psutil.Process(z.pid).terminate()
                    print(f"Boom! Killed {z.name} (PID: {z.pid})")
                    
                    total_ram_saved += z.ram
                    zombies_killed += 1
                    z.kill()
                    
                    # Spawn a 'blood' effect (simple red flash)
                    pygame.draw.circle(screen, BLOOD_COLOR, pos, 30)
                    pygame.display.flip()
                    pygame.time.delay(50) # Impact pause

        # 2. Update
        all_sprites.update()
        
        # Respawn if empty
        if len(zombies) == 0:
            text = big_font.render("WAVE CLEARED! RESCANNING...", True, (255, 255, 255))
            screen.blit(text, (SCREEN_WIDTH//2 - 200, SCREEN_HEIGHT//2))
            pygame.display.flip()
            pygame.time.delay(1000)
            
            new_procs = get_processes()
            for p in new_procs:
                z = Zombie(p)
                all_sprites.add(z)
                zombies.add(z)

        # 3. Draw
        screen.fill(BG_COLOR)
        
        # Draw Zombies
        all_sprites.draw(screen)
        
        # Draw Name Tags above Zombies
        for z in zombies:
            tag = font.render(f"{z.name}", True, (255, 255, 255))
            ram_tag = font.render(f"{z.ram}MB", True, (255, 100, 100))
            screen.blit(tag, (z.rect.x, z.rect.y - 20))
            screen.blit(ram_tag, (z.rect.x, z.rect.y - 10))

        # Draw UI
        draw_ui(screen, total_ram_saved, zombies_killed)
        
        # Custom Cursor (Crosshair)
        mx, my = pygame.mouse.get_pos()
        pygame.draw.line(screen, (255, 0, 0), (mx-10, my), (mx+10, my), 2)
        pygame.draw.line(screen, (255, 0, 0), (mx, my-10), (mx, my+10), 2)
        pygame.mouse.set_visible(False)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
