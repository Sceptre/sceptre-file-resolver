# File Resolver

A Sceptre resolver to get file contents.  The returned value can be
passed into a parameter as a string, json, or yaml object.  The
file extension determines the return type.  By default, contents from
any files that do not end in `.json` or `.yaml` will be passed in as
a string.

## Motivation

Unlike the [file_contents resolver](https://sceptre.cloudreach.com/latest/docs/resolvers.html#file-contents)
which can only pass strings to parameters this resolver can also pass file
content in as json and yaml object.

## Syntax

```yaml
parameters|sceptre_user_data:
  <name>: !file /path/to/local/file
```

## Examples

### Local file

#### text
Get file content and pass it to the parameter as a text string:

tags/departments.txt
```text
"HR, Governance, Engineering, Marketing"
```

```yaml
parameters:
  departments: !file tags/departments.txt
```

### json
Get file contents and pass it to the parameter as a json object:

tags/departments.json
```json
[
  "HR",
  "Governance",
  "Engineering",
  "Marketing"
]
```

```yaml
parameters:
  departments: !file tags/departments.json
```

### yaml
Get file contents and pass it to the sceptre_user_data as a yaml object:

tags/departments.yaml
```yaml
- "HR"
- "Governance"
- "Engineering"
- "Marketing"
```

```yaml
sceptre_user_data:
  departments: !file tags/departments.yaml
```

__Note__: will do the same for files with `.yml` extension.