# linkrecurse
### Tool for scanning webpages for links recursively

### Installation:
#### Firstly, clone the repository:
```shell
git clone https://github.com/KickdeGans/linkrecurse.git --depth 1
```

#### Then, give the installer file permissions to be executed:
```shell
chmod +x ./install.sh
```

#### Finally, run the installer:
```shell
sudo ./install.sh
```

#### Testing:
Type ```linkrecurse```, the output should look like this:
```
No arguments given.
Type "linkrecurse --help".
```

### Usage:

Run a simple scan on www.exmaple.org:
```shell
linkrecurse --url "https://www.example.org"
```
```
┌ https://www.example.com
└─ https://www.iana.org/domains/example
```
Run a more deep scan:
```shell
linkrecurse --url "https://www.example.org" --depth 1
```
```
┌ https://www.example.org
└┌─ https://www.iana.org/domains/example
 ├─ http://pti.icann.org
 ├─ http://www.icann.org/
 ├─ https://www.icann.org/privacy/policy
 └─ https://www.icann.org/privacy/tos
```
