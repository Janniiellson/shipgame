
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.setmode(
        (ai_settings.screen_width,
        ai_settings.screen.height))
    pygame.display.set_caption("Alien invasion")
    screen.fill(ai_settings.bg_color)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        Ship.blitme()
        pygame.display.flip()

run_game()