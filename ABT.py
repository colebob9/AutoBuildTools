"""
AutoBuildTools
v0

Requirements:
python3
java


Commands to run:
git config --global --unset core.autocrlf
curl -o BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
"""

import subprocess, shlex
import os, shutil

# Config

# Where to download BuildTools from.
url = "https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar"

# End Config

print("AutoBuildTools v0")
print("colebob9")

if os.path.exists("build"):
    shutil.rmtree("build") # Deleting in case of last build.
    print("Deleting last build directory.")

print("Downloading BuildTools...")
subprocess.call(shlex.split("curl -o BuildTools.jar %s" % (url))) # Download BuildTools
print("Done with download!")

print("Starting build...")
os.mkdir("build")
shutil.move("BuildTools.jar", "build/BuildTools.jar")
print("Made \'build\' folder and moved BuildTools into it.")

print("Starting build process.")
subprocess.call(shlex.split("git config --global --unset core.autocrlf")) 
subprocess.call(shlex.split("java -jar build/BuildTools.jar")) # Execute BuildTools
