# File Resolver

A Sceptre resolver to get file contents. The returned value that gets
passed to a parameter can be a string, json, or yaml object.  The
file extension determines the return type.

Unlike the [file_contents resolver](https://sceptre.cloudreach.com/2.2.1/docs/resolvers.html#file-contents)
which can only pass strings to parameters this resolver can also pass json
and yaml objects to parameters.

## Syntax:

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
