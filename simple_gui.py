import time

import pygame

from sj4000 import camera as Camera

class TimerApp:
    def __init__(self):
        pygame.init()
        
        self.running = False
        self.elapsed_time = 0
        self.start_time = 0
        self.status = ""
        self.camera = Camera()
        
        self.width, self.height = 300, 250
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("SJCAM4000 recorder")
        
        self.font = pygame.font.Font(None, 36)
        
        self.start_button = pygame.Rect(50, 150, 80, 30)
        self.stop_button = pygame.Rect(170, 150, 80, 30)
        
        self.run()
    
    def draw_text(self, text, position, color=(255, 255, 255)):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, position)
    
    def start_video_recording(self):
        stat, mode= self.camera.get_mode()
        if not stat:
            print(f'Failed get_mode! {mode}')
            return False, 'Not started'
        if mode != self.camera.MODE_MOVIE and mode != self.camera.MODE_TMOVIE:
            stat, info= self.camera.set_mode('MOVIE')
            if not stat:
                print(f'Failed set_mode! {info}')
                return False, 'Not started'
        stat, info= self.camera.start_stop_movie(self.camera.START)
        if stat:
            return True, ''
        else:
            print(f'Failed start_stop_movie! {mode}')
            return False, 'Not started'

    def stop_video_recording(self):
        stat, mode= self.camera.get_mode()
        if not stat:
            print(f'STOP failed at get_mode! {mode}')
            return False, 'Not stopped'
        if mode == self.camera.MODE_TPHOTO:
            stat, fname= self.camera.snap(None)
            if not stat:
                print(f'Failed snap! {fname}')
                return False, 'Not stopped'
        else:
            stat, info= self.camera.start_stop_movie(self.camera.STOP)
            if stat:
                return True, ''
            else:
                print(f'Failed start_stop_movie! {info}')
                return False, 'Not stopped'

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.screen.fill((0, 0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.collidepoint(event.pos):
                        if not self.running:
                            started, reason = self.start_video_recording()
                            if started:
                                self.running = True
                                self.start_time = time.time() - self.elapsed_time
                            else:
                                self.status = reason
                    elif self.stop_button.collidepoint(event.pos):
                        if self.running:
                            stopped, reason = self.stop_video_recording()
                            if stopped:
                                self.running = False
                                self.elapsed_time = time.time() - self.start_time
                                minutes, seconds = divmod(int(self.elapsed_time), 60)
                                hours, minutes = divmod(minutes, 60)
                                self.status = f"Last: {hours:02}:{minutes:02}:{seconds:02}"
                                self.elapsed_time = 0  # Reset timer
                            else:
                                self.status = reason
            
            if self.running:
                self.elapsed_time = time.time() - self.start_time
            
            minutes, seconds = divmod(int(self.elapsed_time), 60)
            hours, minutes = divmod(minutes, 60)
            timer_text = f"{hours:02}:{minutes:02}:{seconds:02}"
            
            self.draw_text(timer_text, (100, 50))
            if self.status:
                self.draw_text(self.status, (70, 90))
            
            pygame.draw.rect(self.screen, (0, 255, 0), self.start_button)
            pygame.draw.rect(self.screen, (255, 0, 0), self.stop_button)
            
            self.draw_text("Start", (65, 155))
            self.draw_text("Stop", (185, 155))
            
            pygame.display.flip()
            clock.tick(30)

if __name__ == "__main__":
    TimerApp()
