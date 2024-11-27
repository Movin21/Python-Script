import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATTERN = "game"
GAME_CODE_EXTENSION=".go"
GAME_COMPILATION_COMMAND=["go", "build"]

def find_all_game_paths(source):
    game_paths=[]
    for root,dirs,files in os.walk(source):
        for dir in dirs:
            if GAME_DIR_PATTERN in dir:
                game_paths.append(os.path.join(root,dir))
    return game_paths

def get_name_form_paths(paths,to_strip):
    new_names=[]
    for path in paths:
        _,dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip,"")
        new_names.append(new_dir_name)
    return new_names

def create_target_dir(target):
    if not os.path.exists(target):
        os.makedirs(target)

def copy_and_overwrite (source,target):
    if os.path.exists(target):
        shutil.rmtree(target)
    shutil.copytree(source,target)

def make_json_meta_data_file(path,game_dirs):
    meta_data = {}
    for game_dir in game_dirs:
        meta_data[game_dir] = {}
        meta_data[game_dir]["files"] = []
        for root,dirs,files in os.walk(os.path.join(path,game_dir)):
            for file in files:
                meta_data[game_dir]["files"].append(file)
    with open(os.path.join(path,"meta_data.json"),"w") as f:
        json.dump(meta_data,f,indent=4)

def compile_game_code(path):
    code_file_name=None
    for root,dirs,files in os.walk(path):
        for file in files:
            if file.endswith(GAME_CODE_EXTENSION):
                code_file_name = file
                break
        break

    if code_file_name is None:
        return
    command = GAME_COMPILATION_COMMAND + [os.path.join(path,code_file_name)]
    run_command(command,path)

def run_command (command,path):
    cwd=os.getcwd()
    os.chdir(path)

    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print(result)

    os.chdir(cwd)


def main(source_path,target_path):
    cwd=os.getcwd()
    source = os.path.join(cwd,source_path)
    target = os.path.join(cwd,target_path)

    game_paths = find_all_game_paths(source)
    new_game_dirs= get_name_form_paths(game_paths,"_game")
    create_target_dir(target)
    
    for src,dest in zip(game_paths,new_game_dirs):
        copy_and_overwrite(src,os.path.join(target,dest))
        compile_game_code(os.path.join(target,dest))
    
    make_json_meta_data_file(target,new_game_dirs)




if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("Usage: get_game_data.py <game_id> <output_dir>")
    
    source,target = args[1:]
    main(source,target)
