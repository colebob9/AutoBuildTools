"""
AutoBuildTools
v0.2
colebob9

Requirements:
python3
java


Commands to run:
git config --global --unset core.autocrlf
curl -o BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar

TODO:


"""

import subprocess, shlex
import os, shutil

# Config

# Where to download jar files from. Don't need to change unless the URLs are wrong.
buildToolsURL = "https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar"
bungeeCordURL = "https://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar"

# Whether to enable using BungeeCord or Spigot (BuildTools)
useBuildTools = True
useBungeeCord = False

# Directories
jarDir = "Result"   # Where to store the resulting JAR files.
buildDir = "BTbuild"    # Where BuildTools should work.

# Delete Directories
delJarDir = True   # Whether to delete
delBuildDir = True    # Whether to delete files that BuildTools generates.


# End Config

print("AutoBuildTools v0.2")
print("colebob9")

if delJarDir:
    if os.path.exists(jarDir):
        shutil.rmtree(jarDir) # Deleting in case of last build.
        print("Deleting last JAR directory.")

# Create jarDir
if not os.path.exists(jarDir):
    os.mkdir(jarDir)
    print("Made %s directory. All resulting JAR files will be stored here." % (jarDir))

# BungeeCord
if useBungeeCord:
    os.chdir(jarDir)
    print("Downloading BungeeCord...")
    subprocess.call(shlex.split("curl -o BungeeCord.jar %s" % (bungeeCordURL)))
    os.chdir("..") # tweak this so it will change back to the scripts current dir

# BuildTools
if useBuildTools:
    if delBuildDir:
        if os.path.exists(buildDir):
            shutil.rmtree(buildDir) # Deleting in case of last build.
            print("Deleting last build directory.")

    os.mkdir(buildDir)
    os.chdir(jarDir)
    print("Made \'%s\' folder and moved BuildTools into it." % (buildDir))

    print("Downloading BuildTools...")
    subprocess.call(shlex.split("curl -o BuildTools.jar %s" % (buildToolsURL))) # Download BuildTools
    print("Done with download!")

    print("Starting build process...")
    subprocess.call(shlex.split("git config --global --unset core.autocrlf"))
    subprocess.call(shlex.split("java -jar BuildTools.jar")) # Execute BuildTools

    # Move jar files to jarDir

    os.chdir("..") # tweak this so it will change back to the scripts current dir
