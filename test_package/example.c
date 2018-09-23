#include <stdio.h>
#include <SDL.h>
#include <SDL_sound.h>

int main() {
    Sound_Version compiled;
    Sound_Version linked;
    SDL_version sdl_compiled;
    SDL_version sdl_linked_ver;
    const SDL_version *sdl_linked = &sdl_linked_ver;

    SOUND_VERSION(&compiled);
    Sound_GetLinkedVersion(&linked);
    SDL_VERSION(&sdl_compiled);
    SDL_GetVersion(&sdl_linked_ver);

    printf("Compiled against SDL_sound version %d.%d.%d,\n"
           "and linked against %d.%d.%d.\n"
           "Compiled against SDL version %d.%d.%d,\n"
           "and linked against %d.%d.%d.\n\n",
           compiled.major, compiled.minor, compiled.patch,
           linked.major, linked.minor, linked.patch,
           sdl_compiled.major, sdl_compiled.minor, sdl_compiled.patch,
           sdl_linked->major, sdl_linked->minor, sdl_linked->patch);

    return 0;
}
