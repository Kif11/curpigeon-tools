# Curpigeon Tools
Set of tools developed during production of Curpigeon 3D animated short. It include: 
* Scene Assembly
* Renderfarm submission
* Various project and scene cleanups
* User preferences management

# Scene Assembly

> /shot_builder/app.py

Maya Python application allows easy and fast assemble a scene for final lighting and rendering. 
It load appropriate alembic caches into the scene as well as V-Ray proxy files for big assets.

![curpigeon_scene_assembly_01](https://cloud.githubusercontent.com/assets/8003487/12374917/dbe6da4a-bc60-11e5-8aed-e41d6ecdd9c9.gif)

# Renderfarm Submission

> /qube/

Contains modified Qube scripts talored to meet the production needs.

# Project Cleanup

>  /cleaner/app.py

This tool search and remove junk files within specified project directory. It keep the project size tight and easy to manage.

