import pygame
import cv2
import numpy as np



class LoseScreen:
    def __init__(self, main, video_path="assets/perdeu.mp4", bg_sound=None):
        self.video_path = video_path
        self.bg_sound_path = bg_sound
        self.main = main
        pygame.init()
        pygame.mixer.init()

        if self.bg_sound_path:
            self.bg_sound = pygame.mixer.Sound(self.bg_sound_path)
        else:
            self.bg_sound = None

    def draw(self, window=None):
        self.play_video()

    def play_video(self):
        if self.bg_sound:
            self.bg_sound.stop()

        cap = cv2.VideoCapture(self.video_path)

        if not cap.isOpened():
            print("Erro ao abrir o vídeo!")
            return False

        largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        altura = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        screen = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Ahh! você perdeu!")

        clock = pygame.time.Clock()

        fonte = pygame.font.SysFont("arial", 16, bold=True)
        texto1 = fonte.render("VOCÊ PERDEU!", True, (0, 0, 0))
        texto2 = fonte.render("Para jogar novamente", True, (0, 0, 0))
        texto3 = fonte.render("Pressione a letra R", True, (0, 0, 0))

        playing = True
        restart = False 
        while playing:
            success, frame = cap.read()
            if not success:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    self.main.quit()
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        restart = True
                        playing = False
                        self.main.updategamestatus(1)
                        print("updategamestatus(1)")
                        self.main.game.restart()
                        print("reinicia o jogo")


            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_rgb = np.rot90(frame_rgb)
            surface = pygame.surfarray.make_surface(frame_rgb)
            surface = pygame.transform.flip(surface, True, False)
            screen.blit(surface, (0, 0))

            screen.blit(texto1, (largura // 2 - texto1.get_width() // 2, altura - 90))
            screen.blit(texto2, (largura // 2 - texto2.get_width() // 2, altura - 60))
            screen.blit(texto3, (largura // 2 - texto3.get_width() // 2, altura - 40))

            pygame.display.flip()
            clock.tick(fps)

        cap.release()
        cv2.destroyAllWindows()
        #pygame.quit() removido para retornar ao jogo principal
        return restart  # retorna para reiniciar o jogo
    print("reiniciar")

