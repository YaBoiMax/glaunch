# Glaunch
### A simple Python Script that you can set as a launch command for steam games
---
#### Usage:

in steam right click a game -> Properties -> Launch Options

Paste 
```
glaunch %command%
```

---

#### Configuring:
The script reads a yaml file which is located in `$HOME/.config/games.yml`

The available options are:
```yaml  
[appid]:
  gamemode: false # Wether to use gamemoderun, does nothing if gamemoderun not installed
  prelaunch: ""   # If you want to use a prelaunch command e.g. mangohud, gamescope
  flags: ""       # Any game specific flags you want, if a game for example has a flag called --skip-launcher you would add this here
  env:            # Any environment variables you need, like PROTON_ENABLE_WAYLAND=1, WINE_CPU_TOPOLOGY="24:0,1,2..." , etc...
    name1: value1
    name2: value2
```
The appid is read either from the environment variable `SteamAppId`. Or taken from steams start command which includes AppId in the command

Below is an example config
```yaml
---
default:
  gamemode: true
  env:
    WINE_CPU_TOPOLOGY: "30:0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29"

# The Finals
2073850:
  gamemode: true
  flags: "-useallavailablecores"
  prelaunch: "mangohud gamescope -W 1920 -H 1080 -f -b --force-grab-cursor --"
  env:
    SDL_VIDEODRIVER: 'wayland,x11,windows'
    __GL_THREADED_OPTIMIZATION: 1
    __GL_SHADER_DISK_CACHE: 1
    PROTON_USE_NTSYNC: 1
    PROTON_USE_EAC_LINUX: 1
    PROTON_ENABLE_NVAPI: 1
    PROTON_ENABLE_WAYLAND: 1
    WINE_CPU_TOPOLOGY: "30:0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29"

# Where Winds Meet
3564740:
  gamemode: true
  env:
    WINE_CPU_TOPOLOGY: "30:0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29"
    PROTON_ENABLE_HDR: 1
    DXVK_HDR: 1
    PROTON_ENABLE_WAYLAND: 1
    _GL_SHADER_DISK_CACHE_SKIP_CLEANUP: 1
    PROTON_USE_NTSYNC: 1
    NVPRESENT_ENABLE_SMOOTH_MOTION: 1

# Arma Reforger
1874880:
  gamemode: true
  flags: '-maxVRAM=16384'
  env:
    PROTON_USE_NTSYNC: 1
    __GL_THREADED_OPTIMIZATIONS: 1
```
