# -*- coding: utf-8 -*-

import os
import json
import yaml

from sceptre.resolvers import Resolver


def get_local_content(path):
    """
    Gets file contents from a file on the local machine
    :param path: The absolute path to a file
    """
    try:
        filename, file_extension = os.path.splitext(path)
        with open(path, "r") as file:
            content = file.read()
    except (EnvironmentError, TypeError) as e:
        raise e

    if content:
        if file_extension == '.json':
            content = json.loads(content)
        if file_extension == '.yaml' or file_extension == '.yml':
            content = yaml.safe_load(content)

    return content


class File(Resolver):
    """
    Resolver for the contents of a file.

    :param argument: Absolute path to file.
    :type argument: str
    """

    def __init__(self, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)

    def resolve(self):
        """
        Retrieves the contents of a file at a given absolute file path.

        :returns: Contents of file.
        :rtype: str, or json/yaml parsed object based on file extension
        """
        path = self.argument
        if not path:
            raise ValueError("Missing argument: path to a file")

        content = get_local_content(path)

        return content
