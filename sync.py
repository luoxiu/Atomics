#!usr/bin/env python

import urllib.request
import json
import zipfile
import shutil
import os 

url = "https://api.github.com/repos/apple/swift-nio/releases/latest"

release = json.loads(urllib.request.urlopen(url).read())

tag_name = release['tag_name']
download_url = release["zipball_url"]

print(f'latest release is: {tag_name}')

latest_file = open('.sync/latest', 'r+')

local_tag_name = latest_file.read()

if local_tag_name == tag_name:
    print(f'no need to sync, return!')
    exit(0)

print('need sync')

workdir = f'.sync/{tag_name}'

if not os.path.exists(workdir):
    os.makedirs(workdir) 

zip_file = f'{workdir}/swift-nio.zip'

print(f'download "{download_url}" to "{zip_file}"...')
urllib.request.urlretrieve(download_url, zip_file)

print(f'unzip "{zip_file}"...')
with zipfile.ZipFile(zip_file, 'r') as zf:
    zf.extractall(workdir)

def sync_subdir(dirname, subdir):
    path = f'Sources/{subdir}'
    if os.path.exists(path):
        shutil.rmtree(path)
    from_dir = os.path.join(workdir, dirname, path)
    to_dir = path
    print(f'copy "{from_dir}" to "{to_dir}"...')
    shutil.copytree(from_dir, path)

for filename in os.listdir(workdir):
    if filename.startswith('apple-swift-nio'):
        sync_subdir(filename, 'CNIOAtomics')
        sync_subdir(filename, 'NIOConcurrencyHelpers')

latest_file.seek(0)        
latest_file.write(tag_name)
latest_file.truncate()

latest_file.close()

print('done!')
