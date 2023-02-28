#!/bin/bash

echo "Starting bug bounty reconnaissance..."

# Enter the target domain name or IP address
read -p "Enter the target domain or IP address: " target

# Use subfinder to find subdomains
echo "Running subfinder..."
subfinder -d $target -o subdomains.txt

# Use MassDNS to resolve the subdomains
echo "Running MassDNS..."
massdns -r /usr/share/massdns/lists/resolvers.txt -t A -o S subdomains.txt -w resolved.txt

# Use GetJS to extract JavaScript files
echo "Running GetJS..."
cat resolved.txt | getjs > javascript.txt

# Use GoLinkFinder to find endpoints in JavaScript files
echo "Running GoLinkFinder..."
golinkfinder -i javascript.txt -o endpoints.txt

# Use dirsearch to find directories and files
echo "Running dirsearch..."
python3 /opt/dirsearch/dirsearch.py -u https://$target -e php,asp,aspx,jsp,html,txt -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -o directories.txt

# Use Sublist3r to find additional subdomains
echo "Running Sublist3r..."
python3 /opt/Sublist3r/sublist3r.py -d $target -o subdomains.txt

# Use nuclei to scan for vulnerabilities
echo "Running nuclei..."
nuclei -l resolved.txt -t /opt/nuclei-templates/cves/ -t /opt/nuclei-templates/takeovers/ -t /opt/nuclei-templates/vulnerabilities/ -o nuclei_results.txt

# Use parameth to find HTTP parameter vulnerabilities
echo "Running parameth..."
parameth -d $target -o parameters.txt

# Use XSSHunter to find XSS vulnerabilities
echo "Running XSSHunter..."
python3 /opt/XSS-Hunter/xsshunter.py -u https://$target -o xss_results.txt

# Use FFuF to fuzz for vulnerabilities
echo "Running FFuF..."
ffuf -w directories.txt:FUZZ -u https://$target/FUZZ -e .php,.html,.txt -fc 404 -mc 200 -o ffuf_results.txt

# Use SQLMap to scan for SQL injection vulnerabilities
echo "Running SQLMap..."
sqlmap -m resolved.txt --batch --level=5 --risk=3 --dbs --dbms=mysql -o sqlmap_results.txt

# Use XXEInjector to find XXE vulnerabilities
echo "Running XXEInjector..."
xxeinjector.py --file=xml_files.xml --url=https://$target -o xxe_results.txt

# Use SSRFDetector to find SSRF vulnerabilities
echo "Running SSRFDetector..."
python3 /opt/SSRFDetector/ssrfdetector.py -l resolved.txt -o ssrf_results.txt

# Use GitTools to find sensitive information in GitHub repositories
echo "Running GitTools..."
python3 /opt/GitTools/GitDumper/gitdumper.py https://github.com/$target.git

# Use git-all-secrets to find secrets in GitHub repositories
echo "Running git-all-secrets..."
docker run --rm -it abhartiya/tools:git-all-secrets -v -r $target -t all

# Use Waybackurls to find URLs from the Wayback Machine
echo "Running Waybackurls..."
cat subdomains.txt | waybackurls > wayback_urls.txt

# Use Waybackrobots to find robots.txt files from the Wayback Machine
echo "Running
