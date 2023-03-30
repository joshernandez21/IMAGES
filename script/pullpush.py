
import subprocess
import wget
import argparse
import os


def upload_git(version):
    try:
        command("git add --all")
        command("git status")
        command("git commit -m 'Adding new version'")
        command("git status")
        command("git push")
        command("git status")
    except Exception as error:
        print("Unable to push to git")
    return True


def download_split(filename, version):
    path = "../" + version
    os.makedirs(path)
    print("Creating folder .. Success")
    url = "https://cdn.devolutions.net/download/Mac/{}"
    wget.download(url.format(filename))
    print("Dowloading file .. Success")
    split_cmd = "split --bytes=90M {}"
    command(split_cmd.format(filename))
    print("Splitting file .. Success")
    os.remove(filename)
    print("Removing original .. Success")
    move_cmd = "find . -maxdepth 1 -mindepth 1 -not -name pullpush.py -print0 | xargs -0 mv -t ../{}"
    command(move_cmd.format(version))
    print("Copying files to version folder .. Success")
    upload_git(version)
    print("Upload files to Git .. Success")


def get_args():
    parser=argparse.ArgumentParser(description="Args")
    parser.add_argument('-filename', required=True)
    parser.add_argument('-version', required=True)
    return parser
    
def command(cmd):
    try:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,universal_newlines=True)
        subprocess_return = process.stdout.read()
        process.kill()
    except Exception as error:
        print("Unable to execute command")
    return subprocess_return

def main():
    try:
        parser = get_args()
        args = parser.parse_args()
        download_split(args.filename, args.version)
    except Exception as error:
        print(error)

if __name__ == '__main__':
    main()





