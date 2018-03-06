from grab import process_repo_commit
import json

def handler(event, context):

    print event
    #print context

    github_push_data_json = event['Records'][0]['Sns']['Message']

    github_push_data = json.loads(github_push_data_json)

    print github_push_data

    commit = github_push_data['head_commit']['id']

    repo_full_name = github_push_data['repository']['full_name']
    # looks like "DigitalGlobe/gbdxtools"

    contents_url = github_push_data['repository']['contents_url']
    # looks like https://api.github.com/repos/DigitalGlobe/gbdxtools/contents/{+path}

    process_repo_commit(contents_url, repo_full_name, commit)
