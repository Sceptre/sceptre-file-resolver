# File Resolver

A Sceptre resolver to get file contents. The returned value that gets
passed to the parameter can be a string, json, or yaml object.  The
file extension determines the return type.

## Syntax:

```yaml
parameters|sceptre_user_data:
  <name>: !file_contents /path/to/file.txt
```

## Examples

Get file content and pass it to the parameter as a string:
```yaml
parameters:
  iam_policy: !file /path/to/policy.txt
```

Get file contents and pass it to the parameter as a json object:
```yaml
parameters:
  iam_policy: !file /path/to/policy.json
```

Get file contents and pass it to the sceptre_user_data as a yaml object:
```yaml
sceptre_user_data:
  iam_policy: !file /path/to/policy.yaml
```
