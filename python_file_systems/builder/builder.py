"""
    * A Cookiecutter like app
    * That lets creates projects from predefined templates
    * this app supports only - Flask
"""
from distutils.util import strtobool
import unicodedata
import pathlib
import sys
import os
import re


DIRS = [
    '{project_slug}/',
    '{project_slug}/static/',
    '{project_slug}/static/img/',
    '{project_slug}/static/js/',
    '{project_slug}/static/css/',
    '{project_slug}/templates/',
]


def slugify(string):
    # strip out unicode characters and replace 'em with ASCI equivalent
    # so it makes sure that string are safe to use
    string = unicodedata.normalize('NFKC', string)
    string = re.sub(r'[^\w\s]', '', string).strip().lower()
    return re.sub(r'[_\-\s]+', '_', string)


def get_root():
    root = pathlib.PurePath(
        input("What's the full path where you'd the project? ")
    )
    if not root.is_absolute():
        return os.path.abspath(get_root())
    return root


def check_del_root(root):
    if os.path.exists(root):
        print('Path already exists.')
        try:
            delete = strtobool(input('Delete existing files/directories? [y/n]'))
        except ValueError:
            return check_del_root(root)
        else:
            if delete:
                try:
                    os.removedirs(root)
                except OSError:
                    print("Couldn't remove {}. Please delete it yourself.".format(root))
                else:
                    print('Deleted {}'.format(root))


def create_dirs(root, slug):
    try:
        os.makedirs(root)
    except OSError:
        print("Couldn't create the project root at {}.".format(root))
        sys.exit()
    else:
        for dir in DIRS:
            try:
                os.mkdir(os.path.join(root, dir.format(project_slug=slug)))
            except FileExistsError:
                pass


def main():
    """Entrypoint"""
    project_root = get_root()
    check_del_root(project_root)
    project_name = None
    # project_author = None
    while not project_name:
        project_name = input("What's the full name for the project? ").strip()
        # project_author = input("Who will be author of a project? ").strip()
    project_slug = slugify(project_name)
    create_dirs(project_root, project_slug)

    print("Creating '{}' project in {}".format(project_name, project_root))


if __name__ == '__main__':
    main()
