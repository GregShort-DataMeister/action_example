import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="Trigger a GitHub workflow by dispatch event")
    parser.add_argument("--repo", required=True, help="Repository in the format OWNER/REPO (e.g., octocat/Hello-World)")
    parser.add_argument("--token", required=True, help="GitHub Personal Access Token with 'workflow' permission")
    parser.add_argument("--workflow", default="execute.yml", help="Workflow filename in .github/workflows")
    parser.add_argument("--ref", default="main", help="Git reference (branch or tag) to run the workflow on")

    args = parser.parse_args()

    # Construct the API endpoint
    url = f"https://api.github.com/repos/{args.repo}/actions/workflows/{args.workflow}/dispatches"

    headers = {
        "Authorization": f"token {args.token}",
        "Accept": "application/vnd.github.v3+json"
    }

    payload = {
        "ref": args.ref
    }

    # Dispatch the workflow
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 204:
        print("Workflow dispatched successfully!")
    else:
        print(f"Failed to dispatch workflow. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    main()
