import pygame


def main():
    try:
        input_data = input().strip()
        n = int(input_data)
        if n <= 0:
            print("Неправильный формат ввода")
            return

        size = 300
        pygame.init()
        screen = pygame.display.set_mode((size, size))
        pygame.display.set_caption("15.01.2025 | Сфера") # Дата для себя
        screen.fill((0, 0, 0))

        for i in range(1, n + 1): # Тут пришлось чуток разделить, чтобы ограничение символов не выдало
            pygame.draw.ellipse(
                screen,
                (255, 255, 255),
                (0, (size // 2) - (i * (size // (2 * n))), size, i * (size // n)),
                1
            )
            pygame.draw.ellipse(
                screen,
                (255, 255, 255),
                ((size // 2) - (i * (size // (2 * n))), 0, i * (size // n), size),
                1
            )

        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
    except:
        print("Неправильный формат ввода")


if __name__ == "__main__":
    main()