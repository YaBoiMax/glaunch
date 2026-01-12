#!/usr/bin/env python3
import sys, subprocess, os, yaml, re
from pathlib import Path
user_home=os.getenv('HOME')
steam_env = os.environ.copy()
config=False
appid=False


launch_params = {
  "command": sys.argv[1:],
  "flags": [],
  "prelaunch": [],
  "gamemode": [],
}


if "SteamAppId" in steam_env:
  # Try getting the AppId from steams environment
  appid=int(steam_env["SteamAppId"])
else:
  # Try getting the AppId from the start command
  appid=' '.join(sys.argv[1:])
  appid=re.sub(r'^.*AppId\s*\=\s*', '', appid) # Remove EVERYTHING before AppId
  appid=re.sub(r'\s.*$',            '', appid) # Remove EVERYTHING after AppId
  try:
    appid=int(appid)
  except ValueError as verr:
    appid=False


# Read Config file if it exists
if Path(user_home+"/.config/games.yml").exists():
  with open(user_home+"/.config/games.yml") as stream:
      try:
          config=yaml.safe_load(stream)
      except yaml.YAMLError as exc:
          print(exc)


def set_vars(_appid):
  # Set Environment
  if "env" in config[_appid] and isinstance(config[_appid]["env"], dict):
    for name, value in config[_appid]["env"].items():
      steam_env[name]=str(value)

  # Enable Gamemode
  if "gamemode" in config[_appid] and config[_appid]["gamemode"] ==  True:
    launch_prelaunch = ["gamemoderun"]

  # Set Game Flags
  if "flags" in config[_appid]:
    launch_params["flags"] = [str(config[_appid]["flags"])]

  # Set Pre Launch Commands
  if "prelaunch" in config[_appid]:
    launch_params["prelaunch"] = config[_appid]["prelaunch"].split()


# Set Game Specific Parameters from config
if config != False:
  if appid and appid in config:
    set_vars(appid)

  # Set Default Parameters if game not found in config
  elif appid == False or appid not in config:
    set_vars("default")


launch_command = launch_params["gamemode"] + launch_params["prelaunch"] + launch_params["command"] + launch_params["flags"]
output=subprocess.run(launch_command , env=steam_env, stderr=subprocess.STDOUT)
