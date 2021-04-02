# -*- coding: utf-8 -*-

import os
import json
import yaml
import requests

from sceptre.resolvers import Resolver
from urllib.parse import urlparse


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


def get_url_content(path):
    """
    Gets file contents from a file at a URL location
    :param path: The URL reference to a file
    """
    url = urlparse(path)
    filename, file_extension = os.path.splitext(url.path)
    try:
        response = requests.get(path)
        content = response.text
        if response.status_code != requests.codes.ok:
            raise response.raise_for_status()
    except requests.exceptions.RequestException as e:
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
    """

    def __init__(self, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)

    def resolve(self):
        """
        Retrieves the contents of a file.

        :returns: Contents of file.
        :rtype: str, or json/yaml parsed object based on file extension
        """
        path = self.argument
        if not path:
            raise ValueError("Missing argument: path or URL reference to a file")

        if path.startswith('https') or path.startswith('http'):
            content = get_url_content(path)
        else:
            content = get_local_content(path)

        return content
