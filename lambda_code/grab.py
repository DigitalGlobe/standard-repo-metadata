import requests
import base64
import yaml
from jsonschema import validate as jsonschema_validate
from github import Github
import os

# get from env var
token = os.environ.get('GITHUB_TOKEN')
request_headers = {'Authorization': 'token %s' % token}

backlink_url = 'https://github.com/DigitalGlobe/standard-repo-metadata'


def find_yaml_files(contents_url, commit):
    url = contents_url.replace('{+path}','') + '?ref=' + commit
    r = requests.get(url, headers=request_headers)
    r.raise_for_status()
    urls = []
    for result in r.json():
        name = result['name']
        if name.endswith('.info.yml'):
            urls.append(result['url'])
    return urls

def get_yaml_file(url):
    r = requests.get(url, headers=request_headers)
    encoded_content = r.json()['content']
    return base64.b64decode(encoded_content)

def validate_info_yaml(data):
    # attempt to yaml_decode the file (will throw exception if it fails):
    data = yaml.load(data)

    print data

    with open(os.path.join('..', 'schemas', 'info_schema.yml','r') as f:
        yaml_schema = yaml.load(f.read())

    jsonschema_validate(data, yaml_schema)

    return True

def set_github_status(repo,commit,status,url,description,context):
    allowed_statuses = ['pending', 'success', 'error', 'failure']
    if not status in allowed_statuses:
        raise Exception('Invalid status: %s' % status)
    g = Github(token)
    r = g.get_repo(repo)
    c = r.get_commit(commit)
    s = c.create_status(status, target_url=url, description=description, context=context)
    return s

def process_repo_commit(contents_url, repo_full_name, commit):

    set_github_status(    repo_full_name,
                          commit,
                          'pending',
                          backlink_url,
                          'Checking for valid <service-name>.info.yml file...',
                          'DG Best Practice')

    urls = find_yaml_files(contents_url, commit)

    if not urls:
        #record_nonexistent_yaml_file()
        set_github_status(repo_full_name,
                          commit,
                          'failure',
                          backlink_url,
                          '<service-name>.info.yml file not found.',
                          'DG Best Practice')
        return

    for url in urls:
        print "getting url: %s" % url
        data = get_yaml_file(url)
        try:
            validate_info_yaml(data)
            #record_valid_yaml_file_info()
            set_github_status(repo_full_name,
                      commit,
                      'success',
                      backlink_url,
                      'Valid <service-name>.info.yml found & validated.  Please remember to keep it up to date!',
                      'DG Best Practice')
        except:
            #record_invalid_yaml_file()
            set_github_status(repo_full_name,
                              commit,
                              'failure',
                              backlink_url,
                              '<service-name>.info.yml file is invalid.  Please adhere to spec: %s' % backlink_url,
                              'DG Best Practice')



    
