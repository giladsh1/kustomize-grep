# k8s-grep


k8s-grep is a tool that lets you filter specific resources from a collection of Kubernetes YAML manifests.


## Example usage:
```
usage: k8s-grep [options]

positional arguments:
  dir_path              directory path to filter

options:
  -h, --help            show this help message and exit
  -ks, --kustomize      Use kustomize to render the manifests before filtering
  -n NAME, --name NAME  filter by name - can be passed multiple times
  -xn XNAME, --exclude-name XNAME
                        exclude by name - can be passed multiple times
  -k KIND, --kind KIND  filter by kind - can be passed multiple times
  -xk XKIND, --exclude-kind XKIND
                        exclude by kind - can be passed multiple times
  -g REGEX_LST, --grep REGEX_LST
                        filter by regexp match on yaml values (doesn't match keys) - can be passed multiple times
  -xg EXCLUDE_REGEX_LST, --xgrep EXCLUDE_REGEX_LST
                        exclude by regexp match on yaml values (doesn't match keys) - can be passed multiple times
```

### Examples:
`k8s-grep --name gateway dev/` - will output all objects with the name `gateway` in `dev` directory.

`k8s-grep --name gateway --name web dev/` - will output all objects with the name `gateway` or `web` in `dev` directory.

`k8s-grep --name gateway --kind service < dev/mainfests.yaml` - will output all objects with the name `gateway` and kind `service` from the `dev/manifests.yaml` file.

`some-other-cmd | k8s-grep --exclude-name mobile` - will output all objects NOT named `mobile` from the standard input.

`k8s-grep --grep 'production-.*' dev/` - will output all objects matching the pattern from the dev directory.

You can pipe the output into kubectl: `./k8s-grep --directory dev --name console | kubectl [diff|apply] -f -`

## Installation
```
python3 -m pip install pyyaml # ensure Python YAML module is installed
git clone https://github.com/giladsh1/k8s-grep.git
sudo ln -s $(pwd)/k8s-grep/k8s-grep /usr/local/bin/k8s-grep
```
