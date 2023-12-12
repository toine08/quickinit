from git import Repo

import os
import sys
import subprocess
import shutil
import inquirer

questions = [
    inquirer.List('stack',
                message="What stack do you want to use?",
                choices=['Python', 'Vanilla', 'NextJS', 'Golang', 'Rust', 'More'],
                carousel=True,
            ),
]


def create_python_project_structure(project_name):
    src = 'templates/template_python'
    dest = os.path.join(os.getcwd(), project_name)

    shutil.copytree(src,dest)
    #os.rename(temp_path,project_name)

def create_go_project_structure():
    project_name = input("Enter the project name:")
    git_url = 'https://github.com/golang-standards/project-layout'
    destination = os.path.join(os.getcwd(), project_name)
    try:
        Repo.clone_from(git_url, destination)
    except ValueError:
        sys.exit("An error occured...")
    finally:
        end_program(project_name)


def create_vanilla_project_structure():
    project_name = input("Enter the project name:")
    src = 'templates/template_web'
    dest = os.path.join(os.getcwd(), project_name)

    shutil.copytree(src,dest)
    #os.rename(temp_path,project_name)

def create_nextjs_project_structure():
    project_name = input("Enter the project name:")
    # Create basic Next.js project structure (customize as needed)
    try:
        subprocess.run(f'npx create-next-app@latest {project_name}', shell=True)
    except subprocess.CalledProcessError:
        sys.exit("Command not found please install npm or your favorite package management ")

def create_rust_project_structure():
    project_name = input("Enter the project name:")
    try:
        subprocess.run(f'cargo new {project_name}', shell=True)
    except subprocess.CalledProcessError:
        sys.exit("Command not found please install rust & cargo to process ")

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

    
    answers = inquirer.prompt(questions)
    project_type = answers['stack']
    try:
        match project_type:
            case "NextJS":
                #ADD project name func
                create_nextjs_project_structure(input("Project name: "))
                end_program()
            case "Vanilla":
                create_vanilla_project_structure(input("Project name: "))
                end_program()
            case "Golang":
                create_go_project_structure(input("Project name: "))
                end_program()
            case "Python":
                create_python_project_structure(input("Project name: "))
                end_program()
            case "Rust":
                create_rust_project_structure(input("Project name: "))
                end_program()
            case "More":
                print(f"If there is not the language you want to use you can write an issue on this github: https://github.com/toine08/clitool")
                sys.exit()

    except KeyboardInterrupt:
        print("Exiting... thanks for using clitool")
        sys.exit()
        
if __name__ == "__main__":
    main()
