from git import Repo

import os
import sys
import subprocess
import shutil

def prompt(question):
    return input(question)

def create_python_project_structure(project_path):
    # Create basic Python project structure (customize as needed)
    os.mkdir(os.path.join(project_path, "src"))
    os.mkdir(os.path.join(project_path, "tests"))
    # ... add more directories as needed

def create_go_project_structure(project_name):
    git_url = 'https://github.com/golang-standards/project-layout'
    destination = os.path.join(os.getcwd(), project_name)
    try:
        Repo.clone_from(git_url, destination)
    except ValueError:
        sys.exit("An error occured...")


def create_vanilla_project_structure(project_name):
    src = 'templates/template_web'
    dest = os.path.join(os.getcwd(), project_name)

    shutil.copytree(src,dest)
    #os.rename(temp_path,project_name)

def create_nextjs_project_structure(project_name):
    # Create basic Next.js project structure (customize as needed)
    try:
        subprocess.run(f'npx create-next-app@latest {project_name}', shell=True)
    except subprocess.CalledProcessError:
        sys.exit("Command not found please install npm or ")
    # ... add more directories as needed

def open_vscode(project_path):
    try:
        subprocess.run(["code", project_path], check=True)
    except subprocess.CalledProcessError:
        print("Error: Unable to open VSCode. Make sure it's installed and in your PATH.")

def end_program(project_name):
    open_vscode(project_name)
    print("VSCode open...")
    sys.exit("Exiting the program...")

def main():
    # Interactively prompt the user for project information
    project_type = prompt("Enter the project type (python, go, vanilla, nextjs, etc.): ")
    project_name = prompt("Enter the project name: ")

    if project_type == "nextjs":
        create_nextjs_project_structure(project_name)
        end_program(project_name)
    elif project_type == "vanilla":
        create_vanilla_project_structure(project_name)
        end_program(project_name)
    elif project_type == "go":
        create_go_project_structure(project_name)
        end_program(project_name)



if __name__ == "__main__":
    main()
