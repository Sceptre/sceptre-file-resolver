# -*- coding: utf-8 -*-

import unittest
import json
import pytest
import tempfile
import yaml

from resolver.file import File

class TestFileResolver(unittest.TestCase):
    file_resolver = File(
        argument=None
    )

    # def setup_method(self, test_method):

    def test_resolving_with_existing_file(self):
        with tempfile.NamedTemporaryFile(mode='w+') as f:
            f.write("stuff")
            f.seek(0)
            self.file_resolver.argument = f.name
            result = self.file_resolver.resolve()

        assert result == "stuff"

    def test_resolving_with_non_existant_file(self):
        with pytest.raises(IOError):
            self.file_resolver.argument = "/non_existant_file"
            self.file_resolver.resolve()

    def test_resolving_with_no_file_path(self):
        with pytest.raises(ValueError):
            self.file_resolver.argument = None
            self.file_resolver.resolve()

    def test_resolving_with_empty_file_path(self):
        with pytest.raises(ValueError):
            self.file_resolver.argument = ""
            self.file_resolver.resolve()

    def test_resolving_with_existing_valid_json_file(self):
        file_content = '{"good": "json"}'
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.json') as f:
            f.write(file_content)
            f.seek(0)
            self.file_resolver.argument = f.name
            result = self.file_resolver.resolve()

        expected = json.loads(file_content)
        self.assertDictEqual(result, expected)

    def test_resolving_with_existing_invalid_json_file(self):
        file_content = '{"bad" "json"}'
        with pytest.raises(json.decoder.JSONDecodeError):
            with tempfile.NamedTemporaryFile(mode='w+', suffix='.json') as f:
                f.write(file_content)
                f.seek(0)
                self.file_resolver.argument = f.name
                self.file_resolver.resolve()

    def test_resolving_with_existing_valid_yaml_file(self):
        file_content = """
            type: object
            properties:
              testing:
                type: array
                items:
                  - A
                  - B
            """
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.yaml') as f:
            f.write(file_content)
            f.seek(0)
            self.file_resolver.argument = f.name
            result = self.file_resolver.resolve()

        expected = yaml.safe_load(file_content)
        self.assertDictEqual(result, expected)

    def test_resolving_with_existing_valid_yml_file(self):
        file_content = """
            type: object
            properties:
              testing:
                type: array
                items:
                  - A
                  - B
            """
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.yml') as f:
            f.write(file_content)
            f.seek(0)
            self.file_resolver.argument = f.name
            result = self.file_resolver.resolve()

        expected = yaml.safe_load(file_content)
        self.assertDictEqual(result, expected)

    def test_resolving_with_existing_invalid_yaml_file(self):
        file_content = """
          type: object
        properties: bad
        """
        with pytest.raises(yaml.parser.ParserError):
            with tempfile.NamedTemporaryFile(mode='w+', suffix='.yaml') as f:
                f.write(file_content)
                f.seek(0)
                self.file_resolver.argument = f.name
                self.file_resolver.resolve()

    def test_resolving_with_existing_valid_text_file(self):
        file_content = 'stuff'
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt') as f:
            f.write(file_content)
            f.seek(0)
            self.file_resolver.argument = f.name
            result = self.file_resolver.resolve()

        assert result == "stuff"
