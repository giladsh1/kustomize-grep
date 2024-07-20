# k8grep


k8grep is a CLI tool for filtering specific resources from a collection of Kubernetes YAML manifests.


## Example usage:
```
usage: k8grep [options]

positional arguments:
  dir_path              Directory path to filter

options:
  -h, --help            show this help message and exit
  -ks, --kustomize      Use kustomize to render the manifests before
                        filtering.
  -n NAME, --name NAME  filter by name - can be passed multiple times.
  -xn XNAME, --exclude-name XNAME
                        exclude by name - can be passed multiple times.
  -k KIND, --kind KIND  filter by kind - can be passed multiple times.
  -xk XKIND, --exclude-kind XKIND
                        exclude by kind - can be passed multiple times.
  -g REGEX_LST, --grep REGEX_LST
                        filter by regexp match on yaml values (doesn't match
                        keys) - can be passed multiple times.
  -xg EXCLUDE_REGEX_LST, --xgrep EXCLUDE_REGEX_LST
                        exclude by regexp match on yaml values (doesn't match
                        keys) - can be passed multiple times.
```

### Examples:
`k8grep --name gateway dev/` - Outputs all objects with the name gateway in the dev directory.

`k8grep --name gateway --name web dev/` - Outputs all objects with the name `gateway` or `web` in the `dev` directory.

`k8grep --name gateway --kind service < dev/manifests.yaml` - Outputs all objects with the name `gateway` and kind `service` from the `dev/manifests.yaml` file.

`some-other-cmd | k8grep --exclude-name mobile` - Outputs all objects NOT named `mobile` from the standard input.

`k8grep --grep 'production-.*' dev/` - Outputs all objects matching the pattern from the dev directory.

You can pipe the output into kubectl: `./k8grep --directory dev --name console | kubectl [diff|apply] -f -`

### Flag parsing logic:
All property match flags are grouped by property. Positive matchers are logically ORed together, complementary matchers are ANDed together, and ANDed with the positive matchers. All property groups are then ANDed together:\
`( ( kind1 OR kind2 OR kind3...) AND (not kind4 AND not kind5...) ) AND ( ( name1 OR name2 OR name3...) AND (not name4 AND not name5...) ) AND ( ... )`

The default value for each property match group is `True`, so not passing (for example) any `-k` or `-xk` match flags will match all manifest kinds. Not passing any match flags will match all manifests.

## Installation
```
python3 -m pip install pyyaml # ensure Python YAML module is installed
git clone https://github.com/andreyzax/k8s-grep.git
sudo ln -s $(pwd)/k8grep/k8s_grep.py /usr/local/bin/k8grep
```
