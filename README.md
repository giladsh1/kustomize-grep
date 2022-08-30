# k8s-grep


k8s-grep is a tool that lets you filter specific resources from a stream of Kubernetes YAML manifests, produced by tools such as [Kustomize](https://github.com/kubernetes-sigs/kustomize).


## Example usage:
```
usage: k8s-grep [options]

optional arguments:
  -h, --help            show this help message and exit
  -g GREP, --grep GREP  grep expression - can be passed multiple times
  -k KIND, --kind KIND  filter by kind - can be passed multiple times
  -o OVERLAY, --overlay OVERLAY
                        overlay name to build
  -xg XGREP, --exclude-grep XGREP
                        exclude grep expression - can be passed multiple times
  -xk XKIND, --exclude-kind XKIND
                        exclude by kind - can be passed multiple times
```

### Examples:
`./k8s-grep --overlay dev --grep gateway` -  
will output all objects their name contains `gateway`.  
`./k8s-grep --overlay dev --grep gateway --grep web` -  
will output all objects their name contains `gateway` or `web`.  
`./k8s-grep --overlay dev --grep gateway --kind service` -    
will output all objects their name contains `gateway` and their kind contains `service`.  
`./k8s-grep --overlay dev --grep gateway --exclude-grep mobile` -    
will output all objects their name contains `gateway` excluding objects containing `mobile`.  

You can pipe the output into kubectl:
`./k8s-grep --overlay dev --grep console | kubectl diff -f -`  
  
## Installation
```
python3 -m pip install pyyaml # ensure Python YAML module is installed
git clone https://github.com/giladsh1/k8s-grep.git
sudo ln -s $(pwd)/k8s-grep/k8s-grep /usr/local/bin/k8s-grep
```
