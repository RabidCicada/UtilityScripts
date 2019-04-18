#!/usr/bin/env python
"""
This module harvests 6 digit hex color codes from a target file and displays
their color and their hex value in a swatch table using pygame
"""
import re
import sys
import pygame
import pygame.freetype

DEFAULT_TEXT_COLOR = '#000000'
HEX_CODE_RE = r'.*(#\w+)'

WIDTH = 1280
HEIGHT = 960

SWATCH_WIDTH = 60
SWATCH_HEIGHT = 60


def display_in_bounds(lines,locx,locy,bndx,bndy, display):
    surfsandrects = list()
    font = pygame.freetype.SysFont('comicsansms', 12, bold=True)
    #currlocx = locx
    currlocy = locy
    for line in lines:
        #logger.debug("Drawing %s at (%s,%s)", line, locx, currlocy)
        TextSurf, TextRect = font.render(line, pygame.Color('black'))
        TextRect.left=locx
        TextRect.top=currlocy
        surfsandrects.append((TextSurf, TextRect))
        currlocy = currlocy + TextRect.height
        if bndy:
            if currlocy > bndy:
                logger.error("currlocy %s bndy %s",currlocy, bndy)
                raise ValueError("Lines exceed vertical size")

    for TextSurf, TextRect in surfsandrects:
        #logger.debug("blitting at (%s,%s)",TextRect.left, TextRect.top)
        display.blit(TextSurf, TextRect)



def render_sample(colorcode):
    color = fg(colorcode)
    print(color + " SAMPLE TEXT" + reset)

    color = bg(colorcode)
    print(color + " SAMPLE TEXT" + reset)


def find_color_codes(filename):
    with open(filename,'r') as f:
        results = re.findall(r'#[a-f,A-F,0-9]{6}',f.read(),re.MULTILINE)
    return results

def render_found_codes(colorcodes, display):
    currwidth = 0
    currheight = 0
    for colorcode in colorcodes:
        print("colorcode: {}, x:{}, y:{}".format(colorcode,currwidth,currheight))
        #render_sample(colorcode)
        if currwidth+SWATCH_WIDTH > WIDTH:
            currheight += SWATCH_HEIGHT
            currwidth = 0

        if currheight +SWATCH_HEIGHT> HEIGHT:
            print("Couldn't fit all swatches on the surface")
            break

        pygame.draw.rect( display, pygame.Color(colorcode) , (currwidth,currheight,SWATCH_WIDTH,SWATCH_HEIGHT) )
        display_in_bounds((colorcode,),currwidth, currheight,0,0,display)
        currwidth += SWATCH_WIDTH



    return



if __name__ == "__main__":
    from pygame.locals import QUIT
    pygame.init()
    display = pygame.display.set_mode( (1280,960))
    display.fill( pygame.Color( 'white' ) )
    font = pygame.freetype.SysFont('comicsansms',10)

    colorcodes = find_color_codes(sys.argv[1])
    render_found_codes(colorcodes, display)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
