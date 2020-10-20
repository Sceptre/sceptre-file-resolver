# -*- coding: utf-8 -*-

import os
import json
import yaml

from sceptre.resolvers import Resolver


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
        try:
            file_path = self.argument
            filename, file_extension = os.path.splitext(file_path)
            with open(file_path, "r") as file:
                content = file.read()

            if file_extension == '.json':
                return json.loads(content)
            if file_extension == '.yaml' or file_extension == '.yml':
                return yaml.safe_load(content)
            else:
                return content
        except (EnvironmentError, TypeError) as e:
            raise e
